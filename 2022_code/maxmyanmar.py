import imp
from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import date, datetime,timedelta
from bs4 import BeautifulSoup
import re
import sqlite3
conn = sqlite3.connect("price.db")

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
    
if __name__ == "__main__":
    scrape_daily_max()

