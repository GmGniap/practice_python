## Code to scrape coal plant individual pages from GEM 
## Oct 11, 2021 
## Writer - TPM 

import requests_html 
from requests_html import HTMLSession
session = HTMLSession()

url = "https://www.gem.wiki/Vung_Ang_power_station"
r = session.get(url)
collect = {}
t = r.html.find("title", first=True).text
h = r.html.find("h2")
h2 = [h[i].text for i in range(len(h))]
u = r.html.url

collect = {
    "Title" : t ,
    "Headers" : h2,
    "Link" : u 
}

print(collect["Title"])
print(collect["Headers"])
print(collect['Link'])

