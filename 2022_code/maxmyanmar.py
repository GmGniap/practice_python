from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import date, datetime,timedelta
# from bs4 import BeautifulSoup
import requests
import json
import re
import time
from tqdm import tqdm
import sqlite3
from scrape_marketprice import run_sql, check_table

# conn = sqlite3.connect("price.db")
conn = sqlite3.connect("test.db")

def scrape_daily_max():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://www.maxenergy.com.mm/fuel-prices-list/")
        print(page.title())
        
        ## Scrape page date
        raw_date = page.inner_text('//div[@class="col-md-6 col-xs-12"]')
        page_date = re.search('(\d{2}\/\d{2}\/\d{4})',raw_date).group(1)
        print("Page Date:{}".format(page_date))
        
        page.is_visible('div#collapseRegion_2')
        print("Page is visible!")
        # div_loc = page.inner_html('div#accordionExample')
        
        ## Button count - No used in the code
        # button_count = page.locator('button[type=button]').count()
        # print(f"Button count : {button_count}")
        
        location = ['Yangon','Mandalay','Naypyitaw','Bago','Ayeyarwady','Mon','Sagaing']
        
        ## MaxMyanmar used different codes for regions
        region_code = ['1','2','3','5','6','184','262']
        
        combined_df = pd.DataFrame()
        for i in range(len(location)):
            temp_df = pd.DataFrame()  ## Need to reset temp_df every round
            vars()[f"data_{i}"]= page.inner_html(f'div#collapseRegion_{region_code[i]}')
            
            ## create dataframe names from list - use vars()
            vars()[location[i]] = scrape_table(vars()[f"data_{i}"])
            vars()[location[i]]['division'] = location[i]
            # print(vars()[location[i]].head())
            print(vars()[location[i]].shape)
            # print(type(vars()[location[i]]))
            
            ## Add to temp_df to store temporarily 
            temp_df = pd.concat([combined_df,vars()[location[i]]], ignore_index=True)
            
            ## Assigned temp_df into combined_df to use in next rounds
            combined_df = temp_df
            print("--- x ----")
        # combined_df = pd.concat(location,ignore_index=True)
        print(" ==== x ==== ")
        combined_df['page_date'] = datetime.strptime(page_date, "%d/%m/%Y")
        combined_df['scraping_date'] = pd.to_datetime('today').normalize()
        print(combined_df.head())
        print(combined_df.shape)
        print(" ==== x ==== ")
        # print(combined_df.tail())
        browser.close()
        # return combined_df

## We need to create custom scrape_table function , 
## we can't use pd.read_table because there're extra rows inside td in MaxMyanmar page
def scrape_table(table):
    soup = BeautifulSoup(table, "html.parser")
    body = soup.find_all("tr")
    head = body[0]
    body_rows = body[1:]
    heading = []
    for item in head.find_all("th"):
        item = (item.text).rstrip("\n")
        heading.append(item)
    print(f"Header row : {heading}")
    
    all_rows = []
    
    for row_num in range(len(body_rows)):
        row = []
        selected_row = []  
        for row_item in body_rows[row_num].find_all("td"):
            selected_row.append(row_item)
        ## take only odd number to skip extra class="d-none" rows
        for i in selected_row[::2]:
            row.append(i.text)
        # print(row)
        # print("--- x ---")
        all_rows.append(row)
    # print(all_rows)
    df = pd.DataFrame(data=all_rows, columns=heading)
    return df

def scrape_old_data():
    ## Drop table for error
    # drop_cmd = """ DROP TABLE IF EXISTS max_myanmar """
    # run_sql("test.db", drop_cmd)
    ## first_time table creation
    sql_cmd = """ CREATE TABLE IF NOT EXISTS max_myanmar(index_label INTEGER PRIMARY KEY,gradename TEXT,regionid INTEGER,stationid INTEGER,station_code TEXT,effectivedate TEXT,pretransactiondate TEXT,price REAL,transactiondate TEXT) """
    run_sql("test.db", sql_cmd)
    check_table("test.db")
    
    ## set the first date
    first_date = datetime.strptime('2020-01-14', '%Y-%m-%d').date()
    ## get today date
    t = datetime.today().date()
    for daily in tqdm(daterange(first_date, t)):
        daily_date = daily.strftime("%Y-%m-%d")
        print(f"\n Scraping : {daily_date}")
        try:
            url = "https://app.maxenergy.com.mm/maxapi/webapi/Price/GetPriceList"

            payload = json.dumps({
            "apikey": "R2wwQjRBdTFIbUY4OUFXRTZpbWZuYzhtVkxXd3NBYXdqWXI0Unh6YUNFTGdM",
            "fromdate": f"{daily_date} 12:00:00 AM",
            "todate": f"{daily_date} 11:00:00 PM"
            })
            headers = {
            'content-type': 'application/json',
            'Cookie': '.AspNetCore.Session=CfDJ8B0ta%2BbvQ0RLgbpaxcGdndgbCvK8BQSCNXPXosRd%2BsHPqTu3gVO7Z%2FTID1K2qyncCqw53HbvlUzTyAVYixfNnnZgMYT2siiOV1L0gzKGdYEe%2BYMldYcAlsYqWyohDi4g8t3Y49A%2FKGPoF4BHk1179zRtsuFT6ujfa6Zg8J%2Fxtzeg'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            x = response.json()
            raw_data = x['data']
            raw_df = pd.json_normalize(raw_data)
            
            ## Generate CSV and JSON to check raw data
            # raw_df.to_csv('./raw1.csv')
            # with open('raw_data.json', 'w') as output:
            #     json.dump(x, output)
            
            ## Take rows that not price Zero and reset index
            clean_df = raw_df[raw_df['price'] != 0.0].reset_index(drop=True)
            print("Done!")
            
            print(clean_df.shape)
            # print(clean_df.columns)
            # print(clean_df.head(10))
            clean_df.to_sql("max_myanmar",conn, if_exists="append")
            time.sleep(3)
        except ValueError as e:
            print(f"Error : {e}")
            continue
        print("====x====")
    print("Add old data into Max Myanmar db!")    
    

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

if __name__ == "__main__":
    # scrape_daily_max()
    scrape_old_data()
    
    
    
