from datetime import datetime
from unittest import result
from requests_html import HTMLSession
session = HTMLSession()

from requests_html import AsyncHTMLSession
import pandas as pd
from datetime import datetime,timedelta
import sqlite3
conn = sqlite3.connect("price.db")

async def scrape_max():
    
    asession = AsyncHTMLSession()
    
    url = "https://www.maxenergy.com.mm/fuel-prices-list/"
    # r = session.get(url)
    r = await asession.get(url)
    await r.html.arender()
    # title = r.html.find('title', first=True)
    # print(title.text)
    return r.html.text


if __name__ == "__main__":
    asession = AsyncHTMLSession()
    
    result = asession.run(scrape_max)
    # print(result)
    dfs = pd.read_html(result[0])
    print("---- xx ----")
    print(type(dfs))
    print(len(dfs))
    print("----- x ----")
    print(dfs[1])
    print("----- x ----")
    print(dfs[2])

