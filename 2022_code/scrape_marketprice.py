from curses import echo
import pandas as pd
# from sqlalchemy import create_engine
# engine = create_engine('sqlite://price.db',echo=True)
# conn = engine.connect()
wisarra_table = "wisarra"

import sqlite3
conn = sqlite3.connect("price.db")
# c = conn.cursor()
i = 0

for i in range(9):
    url = f"https://wisarra.com/en/market-price?page={i}"
    # url = "https://wisarra.com/en/market-price?page=2"
    df = pd.read_html(url)
    save_df = df[0]
    save_df['scraping_date'] = pd.to_datetime('today').normalize()
    # print(save_df.columns)
    # print(save_df.head())
    save_df.to_sql(wisarra_table,conn,if_exists='append')
    print(f"Page {i} is done!")
print("Everything updated to SQLite")