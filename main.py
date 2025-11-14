import requests

url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=ibao9Xte7MmWeJG8TdVq07bfA85pNKWFeTUzwwwA"

response = requests.get(url)
data = response.json()

print(data)