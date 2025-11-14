import requests
import datetime
import pprint

API_KEY = "DEMO_KEY"   # Replace with your own key if you have one
ENDPOINT = "https://api.nasa.gov/neo/rest/v1/feed"

# The feed endpoint supports up to 7 days per request
# We'll pull 4 weeks (28 days) in 7-day chunks
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

# Pretty-print the raw data (list of 4 JSON payloads)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(all_data)
