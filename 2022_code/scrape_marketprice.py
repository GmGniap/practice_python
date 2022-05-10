from requests import session
from requests_html import HTMLSession
import pandas as pd
# from sqlalchemy import create_engine
# engine = create_engine('sqlite://price.db',echo=True)
# conn = engine.connect()
wisarra_table = "wisarra"

import sqlite3
conn = sqlite3.connect("price.db")
# c = conn.cursor()
i = 0

## Scraping date from web page

def scrape_date(url):
    session = HTMLSession()
    r = session.get(url)
    # find_class = r.html.find("span.container pageContent", first=True)
    find_class = r.html.xpath("//div[@class='pageContentCon']/div[@class='container pageContent']/*/following::span[1]")
    page_date = find_class[0].text
    return page_date

def scrape_wisarra():
    for i in range(9):
        url = f"https://wisarra.com/en/market-price?page={i}"
        # url = "https://wisarra.com/en/market-price?page=2"
        df = pd.read_html(url)
        save_df = df[0]
        save_df['scraping_date'] = pd.to_datetime('today').normalize()
        page_date = scrape_date("https://wisarra.com/en/market-price")
        save_df['page_date'] = page_date
        print(save_df.columns)
        print(save_df.head())
        save_df.to_sql(wisarra_table,conn,if_exists='append')
        print(f"Page {i} is done!")
    print("Everything updated to SQLite")

if __name__ == "__main__":
    scrape_wisarra()
