import requests

url = "http://www.omdbapi.com/?apikey=310d3aea&s=Silicon&page=1"

resp = requests.get(url)

print(resp.encoding)

## Object methods
if resp.status_code == 200:
    print("Data is here")
    print(resp.json())
else:
    print("Error something happended")
