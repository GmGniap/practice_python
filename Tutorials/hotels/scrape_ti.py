# from requests_html import HTMLSession
# session = HTMLSession()
# r = session.get("./Taninthahyi.html")

# # print(r.status)
# t = r.html.find('table', first=True)
# print(t.html)

# url = "https://www.myanmarhotelier.org/index.php/en/member/taninthahyi-zone"
# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=50)
#         page = browser.new_page()
#         page.goto(url)
#         print(page.title())

import pandas as pd
from bs4 import BeautifulSoup 
import re

def scrape_table():
    with open("./Taninthahyi.html") as page:
        soup = BeautifulSoup(page, "html.parser")
        body = soup.find_all("tbody")
        # print(type(body))
        # print(len(body))
        
        tables = soup.find_all('table')
        for row_num in range(len(body)):
            row = []
            locate = []
            hotel = []
            for item in body[row_num].find_all("tr"):
                columns = item.find_all("td")
                
                hotel_name_list = [i.text.strip() for i in item.select('p',{'class':'jutooltip'})]
                if hotel_name_list != []:
                    hotel.append(str(hotel_name_list[0]))
    
            print(hotel)
            print("===|===")
                #     regex1 = r"(.*?)(?=\s?[Oo]wner\s?Name)"
                #     location_list = [re.match(regex1,i.text.strip()).group(0) for i in item.select('div')]
                    
                #     regex2 = r"(?<=[Oo]wner\sName:\s).*(?=\sSr\.No)"
                #     owner_list = [re.findall(regex2,i.text) for i in item.select('div')]
                #     tooltip_list = [i.text.strip() for i in item.select('div')]
                
                # m = re.match(regex, tooltip_list[0])
                # location = m.group(0)
                # locate.append(location)
                # item = (item.text).rstrip()
                # print(tooltip_list[0])
                    # print(tooltip_list)
                    
                        
                #     print(owner_list)
                #     print("---x---")
                    
    # head = body[0]
    # body_rows = body[1:]
    # heading = []
    # for item in head.find_all("th"):
    #     item = (item.text).rstrip("\n")
    #     heading.append(item)
    # print(f"Header row : {heading}")
    
    # all_rows = []
    
    # for row_num in range(len(body_rows)):
    #     row = []
    #     selected_row = []  
    #     for row_item in body_rows[row_num].find_all("td"):
    #         selected_row.append(row_item)
    #     ## take only odd number to skip extra class="d-none" rows
    #     for i in selected_row[::2]:
    #         row.append(i.text)
    #     # print(row)
    #     # print("--- x ---")
    #     all_rows.append(row)
    # # print(all_rows)
    # df = pd.DataFrame(data=all_rows, columns=heading)
    # return df
    
if __name__ == "__main__":
    # page = BeautifulSoup(open('./Taninthahyi.html','r').read())
    # print(table)
    scrape_table()