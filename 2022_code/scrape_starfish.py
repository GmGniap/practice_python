from datetime import datetime
import requests
import pandas as pd
from datetime import datetime,timedelta
import sqlite3
conn = sqlite3.connect("price.db")

url = "https://starfishmyanmar.com/market-price/history?datelist=2019-12-28,2022-05-19"
single_url = "https://starfishmyanmar.com/market-price/history?datelist={i}"

header = {
    "referer": "https://starfishmyanmar.com/market-price/graph",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "x-csrf-token": "gAo5t1slQKnVFkemJOKeeXgzyylVfDbD7j1IpHnh",
    "x-requested-with" : "XMLHttpRequest"
}

def scrape_starfish(url):
    r = requests.get(url, headers=header)
    x = r.json()

    head_df = pd.json_normalize(x['data']['head'])
    cols = head_df.columns
    body = pd.DataFrame(x['data']['body'], columns=cols)
    transpose_df = (body.melt(id_vars=['title','unit'],var_name='Date',value_name='Price'))

    print("Shape : {}".format(transpose_df.shape))
    # print(transpose_df.head())
    return transpose_df

def update_starfish():
    ## Add old data into price.db - need to run only one time
    # old_data = scrape_starfish(url)
    # old_data['scraping_date'] = pd.to_datetime('today').normalize()
    # old_data.to_sql("starfish",conn,if_exists="replace")
    # print(old_data[old_data['Date']=='2020-12-01'])
    # print("Old data updated")
    # print("----- x -----")

    ## Daily data update
    t = datetime.strftime(datetime.today(), '%Y-%m-%d')
    y = datetime.strftime(datetime.today() - timedelta(days=1),'%Y-%m-%d')
    single_url = f"https://starfishmyanmar.com/market-price/history?datelist={t}"
    daily_data = scrape_starfish(single_url)
    if daily_data.shape[0] != 0:
        daily_data['scraping_date'] = pd.to_datetime('today').normalize()
        daily_data.to_sql("starfish", conn, if_exists="append")
        print(daily_data.head())
        print("Starfish daily data updated!")
        print("----- x -----")
    else:
        print(f"{t} data shape is empty!")

if __name__ == "__main__":
    update_starfish()