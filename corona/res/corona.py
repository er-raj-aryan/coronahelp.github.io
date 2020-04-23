import json
from urllib.request import urlopen


with urlopen("https://api.covid19india.org/data.json")as response :
    source = response.read()

data =json.loads(source)

for item in data['cases_time_series']:
    total=item['totalconfirmed']
    print(total)