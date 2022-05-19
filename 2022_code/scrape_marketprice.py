import requests
import sqlite3
from sqlite3 import Error
from datetime import datetime,timedelta
from requests_html import HTMLSession
import pandas as pd
import numpy as np
# from sqlalchemy import create_engine
# engine = create_engine('sqlite://price.db',echo=True)
# conn = engine.connect()
wisarra_table = "wisarra"

import sqlite3
conn = sqlite3.connect("price.db")

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

def scrape_mpta(url):
    r = requests.get(url)
    x = r.json()
    # print(x["iTotalRecords"])
    df = pd.DataFrame(x["aaData"],columns=['No','Date','Type','Method','Min_Price','Max_Price'])
    return df

## Getting the past data from May 10,2022 to Jan 01,2015
def scrape_old_mpta():
    for i in range(1,3):
        mpta_url = f"https://www.mpta.org.mm/prices_getlist.php?division_id={i}&sEcho=1&iColumns=6&sColumns=%2C%2C%2C%2C%2C&iDisplayStart=0&iDisplayLength=1000000000000000000&mDataProp_0=0&sSearch_0=&bRegex_0=false&bSearchable_0=true&bSortable_0=false&mDataProp_1=1&sSearch_1=&bRegex_1=false&bSearchable_1=true&bSortable_1=true&mDataProp_2=2&sSearch_2=&bRegex_2=false&bSearchable_2=true&bSortable_2=false&mDataProp_3=3&sSearch_3=&bRegex_3=false&bSearchable_3=true&bSortable_3=false&mDataProp_4=4&sSearch_4=&bRegex_4=false&bSearchable_4=true&bSortable_4=false&mDataProp_5=5&sSearch_5=&bRegex_5=false&bSearchable_5=true&bSortable_5=false&sSearch=%7B%22cri_txt_fromdate%22%3A%2201-01-2014%22%2C%22cri_txt_todate%22%3A%2210-05-2022%22%2C%22cri_fuel_type_name%22%3Anull%7D&bRegex=false&iSortCol_0=1&sSortDir_0=desc&iSortingCols=1&_=1652176286790"
        if i == 1:
            df_y = scrape_mpta(mpta_url)
            df_y['Region'] = "Yangon"
            print("Yangon shape : {}".format(df_y.shape))
        if i == 2:
            df_m = scrape_mpta(mpta_url)
            df_m['Region'] = "Mandalay"
            print("Mandalay shape : {}".format(df_m.shape))
    all_old = pd.concat([df_y,df_m])
    print("All shape : {}".format(all_old.shape))
    print(all_old.columns)
    # print(all_old.head(5))

    ## Save scrape_date for old data
    all_old['scraping_date'] = pd.to_datetime('today').normalize()

    ## Connect db file & Create table
    sql_cmd = """ CREATE TABLE mpta(No INTEGER,Date TEXT,Type TEXT,Method TEXT,Min_Price DOUBLE,Max_Price DOUBLE,Region TEXT,Scraping_date TEXT) """
    create_table("price.db",sql_cmd)

    ## Check tables from db
    check_table("price.db")

    ## Insert data into database , if exist - Replace
    all_old.to_sql("mpta",conn,if_exists='replace')
    print("MPTA old data updated into DB file!")

def scrape_daily_mpta():
    t,y = find_dates()
    print(f"Today : {t}")
    print(f"Yesterday : {y}")

    for i in range(1,3):
        ## Yangon Region - id 1 , Mandalay Region - id 2
        # print(i)
        modify_url = f"https://www.mpta.org.mm/prices_getlist.php?division_id={i}&sEcho=1&iColumns=6&sColumns=%2C%2C%2C%2C%2C&iDisplayStart=0&iDisplayLength=1000000000000000000&mDataProp_0=0&sSearch_0=&bRegex_0=false&bSearchable_0=true&bSortable_0=false&mDataProp_1=1&sSearch_1=&bRegex_1=false&bSearchable_1=true&bSortable_1=true&mDataProp_2=2&sSearch_2=&bRegex_2=false&bSearchable_2=true&bSortable_2=false&mDataProp_3=3&sSearch_3=&bRegex_3=false&bSearchable_3=true&bSortable_3=false&mDataProp_4=4&sSearch_4=&bRegex_4=false&bSearchable_4=true&bSortable_4=false&mDataProp_5=5&sSearch_5=&bRegex_5=false&bSearchable_5=true&bSortable_5=false&sSearch=%7B%22cri_txt_fromdate%22%3A%22{y}%22%2C%22cri_txt_todate%22%3A%22{t}%22%2C%22cri_fuel_type_name%22%3Anull%7D&bRegex=false&iSortCol_0=1&sSortDir_0=desc&iSortingCols=1&_=1652176286790"
        if i == 1:
            df_1 = scrape_mpta(modify_url)
            df_1['Region'] = "Yangon"
            print("Daily Yangon shape : {}".format(df_1.shape))
        if i == 2:
            df_2 = scrape_mpta(modify_url)
            df_2['Region'] = "Mandalay"
            print("Daily Mandalay shape : {}".format(df_2.shape))
    
    ## Check dfs shape isn't zero to continue work
    if(df_1.shape[0] != 0 and df_2.shape[0] != 0):
        combined_df = pd.concat([df_1,df_2])

        ## Save scraping_date
        combined_df['scraping_date'] = pd.to_datetime('today').normalize()
        # print("Combined : {}".format(combined_df.shape))
        # print(combined_df.columns)

        ## Add to DB file
        combined_df.to_sql("mpta", conn, if_exists="append")
        print("MPTA Daily Data Update!")
    else:
        print("Dataframe shapes are showing blank!")

def find_dates():
    ## date format - 10-05-2022
    today = datetime.today()
    today_format = datetime.strftime(today, '%d-%m-%Y')
    yesterday = datetime.strftime(today - timedelta(days=1),'%d-%m-%Y')
    return today_format , yesterday


## Create initial table
def create_table(db_file, sql_cmd):
    """ create database connection
    :param db_file: database file
    :sql_cmd: to execute sql commands
    :return: Connection object
    """
    conn = None 
    try:
        conn = sqlite3.connect(db_file)
        print("Successful Connected!")
        cur = conn.cursor()
        ## Create initial table
        cur.execute(sql_cmd)

        ## Need to understand why to have commit()
        conn.commit()  
    except Error as e:
        print(e)

## Check how many tables existing in the db file
def check_table(db_file):
    """ create database connection
    :param db_file: database file
    :sql_cmd: to execute sql commands
    :return: Connection object
    """
    conn = None 
    try:
        conn = sqlite3.connect(db_file)
        # print("Successful Connected!")
        cur = conn.cursor()
        ## Create initial table
        cur.execute("SELECT name from sqlite_master WHERE type='table';")
        print(cur.fetchall())
    except Error as e:
        print(e)

## Check today date include in table dataframe

### Read into dataframe
def check_wisarra_date():
    query = "SELECT * from wisarra"
    test_df = pd.read_sql_query(query, conn)
    # print(test_df.dtypes)

    test_df['page_date'] = pd.to_datetime(test_df['page_date'].astype(str),format='%B %d, %Y')
    # print(test_df['page_date'].head())
    # print(test_df.dtypes)
    check_today = datetime.today().strftime('%Y-%m-%d')
    # print(check_today)
    # check_today = "2022-05-09"

    if(test_df.page_date == check_today).any():
        print("Included {}!".format(check_today))
        return False
        
    else:
        print("Not Include!")
        return True

## Scrape Denko price
def scrape_denko():
    url = "https://denkomyanmar.com/all-denko-station-daily-fuel-rates/"

    ## Without header and direct pd.read_html got http 403 forbidden error
    ## that's why to use requests + header
    header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, header)
    print("Successful request!")
    den_df = pd.read_html(r.text , encoding='utf-8', header=0)
    print("Read HTML success!")
    denko = den_df[0]
    print("Put df success!")
    print(denko)
    print(denko.columns)
    denko['Division_clean'] = denko['Division'].replace(r'^\s*$',np.nan,regex=True)
    denko['Division_clean'].fillna(method='ffill',inplace=True)
    denko['page_date'] = scrape_denko_date(url)
    print("Daily Denko shape : {}".format(denko.shape))
    # print(denko.columns)
    # print(denko.head())

    ## Add dataframe into db file
    # denko.to_sql("denko",conn,if_exists="append")
    print("Denko daily update done!")

## Scrape page_date from Denko page
def scrape_denko_date(url):
    # url = "https://denkomyanmar.com/all-denko-station-daily-fuel-rates/"
    session = HTMLSession()
    r = session.get(url)
    # find_class = r.html.find("span.container pageContent", first=True)
    find_class = r.html.xpath("//section[contains(@class,'elementor-element elementor-element-a3b83a1 elementor-section-full_width elementor-section-height-default elementor-section-height-default elementor-section elementor-top-section')]//div[contains(@class,'elementor-widget-container')]//div[1]")
    
    # print(find_class)
    raw_date = find_class[0].text
    page_date = raw_date.replace("Effective on ","").strip()
    # print(page_date)
    return page_date

## Check duplicated rows in table & remove if exist


if __name__ == "__main__":

    ## Check today date is included in wisarra table or not.
    ## If not - do scraping. If yes , skip.
    # if check_wisarra_date() == True:
    #     scrape_wisarra()
    #     print("Done Wisarra Scraping!")
    # else:
    #     print("Data already existing!!!")
    
    ## Need to run only one time to scrape old data
    #scrape_old_mpta()

    ## Scrape daily MPTA data
    # scrape_daily_mpta()

    ## Scrape Denko
    scrape_denko()
    print("All Tasks done!")
    

