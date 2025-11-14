import requests
import datetime
from tabulate import tabulate

API_KEY = "ibao9Xte7MmWeJG8TdVq07bfA85pNKWFeTUzwwwA"  
ENDPOINT = "https://api.nasa.gov/neo/rest/v1/feed"

today = datetime.date.today()
start_date = today - datetime.timedelta(days=28)

def fetch_range(start, end):
    params = {
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "api_key": API_KEY,
    }
    resp = requests.get(ENDPOINT, params=params)
    resp.raise_for_status()
    return resp.json()

all_data = []
chunk_start = start_date

while chunk_start < today:
    chunk_end = min(chunk_start + datetime.timedelta(days=6), today)
    print(f"Fetching {chunk_start} → {chunk_end}...")
    data = fetch_range(chunk_start, chunk_end)
    all_data.append(data)
    chunk_start = chunk_end + datetime.timedelta(days=1)

neos = []
for chunk in all_data:
    for date_str, daily_neos in chunk.get("near_earth_objects", {}).items():
        for obj in daily_neos:
            neos.append({
                "Name": obj.get("name"),
                "Hazardous": "Yes" if obj.get("is_potentially_hazardous_asteroid") else "No",
                "Diameter (m)": f'{obj["estimated_diameter"]["meters"]["estimated_diameter_min"]:.1f} - {obj["estimated_diameter"]["meters"]["estimated_diameter_max"]:.1f}',
                "Close Approach": obj["close_approach_data"][0]["close_approach_date"],
                "Velocity (km/s)": f'{float(obj["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]):.2f}',
                "Miss Distance (km)": f'{float(obj["close_approach_data"][0]["miss_distance"]["kilometers"]):.0f}',
                "URL": obj.get("nasa_jpl_url")
            })


print(tabulate(neos, headers="keys", tablefmt="fancy_grid"))
