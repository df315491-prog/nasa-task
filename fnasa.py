import requests
import datetime
import pprint

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

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(all_data)
