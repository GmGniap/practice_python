## Relational Database Tutorial with COVID19 dataset

import pandas as pd 
import sqlite3
from tqdm import tqdm



def create_place_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS place(
            place_id INTEGER PRIMARY KEY,
            location TEXT NOT NULL UNIQUE,
            iso_code TEXT NOT NULL UNIQUE,
            continent TEXT
        )
        """
    )

    sn_place = 0
    for index, row in df[['iso_code','continent','location']].iterrows():
        print('\n')
        print(f'record {index}/{len(df)}')
        try:
            cur.execute(
                'INSERT INTO place(location,iso_code,continent) VALUES (?, ?, ?)',        
                (row['location'], row['iso_code'], row['continent']))
            sn_place += 1
            print(f"One record added to table place : {row['location']}")
        except Exception as e:
            print(f"No change : {row['location']} | {e}")
    conn.commit()
    print(f'{sn_place} records added.')

def create_gov_table(cur,conn):
    csv_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    # req = requests.get(csv_url)
    # s = req.content 
    df = pd.read_csv(csv_url)
    print(df.shape)
    sn_gov = 0
    cur.execute("""
                DROP table IF EXISTS gov_response;
                """)
    
    # conn.commit()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS gov_response(
                gov_resp_id INTEGER PRIMARY KEY,
                place_id INTEGER NOT NULL,
                date NOT NULL,
                stringency_index,
                FOREIGN KEY (place_id) REFERENCES place (id))
            """)
    dict_place = create_key_dict(cur)
    print(dict_place['Myanmar'])
    for index in tqdm(range(len(df))):
        row = df.iloc[index]
        try:
            cur.execute(
                """INSERT INTO gov_response(place_id,date,stringency_index)
                VALUES
                (?,?,?)""",
                (dict_place[row['location']], row['date'], row['stringency_index']))
            sn_gov += 1
        except Exception as e:
            print(f"No change : {row['location']} | {e} ")
            pass
    conn.commit()
    conn.close()
    print(f"{sn_gov} records added to table!")
def create_key_dict(cur):
    cur.execute("""
        SELECT place_id, location, iso_code, continent FROM place    
            """ 
    )
    rows = cur.fetchall()
    # print(rows)
    # print(rows[0])
    dict_place = {}
    for row in rows:
        location = row[1]
        if location not in dict_place:
            dict_place[location] = row[0]
    
    return dict_place

if __name__ == "__main__":
    # csv_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    # # req = requests.get(csv_url)
    # # s = req.content 
    # df = pd.read_csv(csv_url)
    # print(df.shape)

    db_name = 'covid19.db'
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    # test = create_key_dict(cur)
    # print(test["Myanmar"])
    create_gov_table(cur,conn)