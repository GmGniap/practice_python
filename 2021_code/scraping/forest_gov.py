## Scraping research reports list from Forest Department MM
## October 20,2021
## Writer - TPM

from requests_html import HTMLSession
import pandas as pd 
s= HTMLSession()

query = 'yangon'
#url = f'https://www.ecosia.org/search?q=weather+{query}'
#url2 = f'https://www.google.com/search?q=weather+{query}'
url3 = 'https://www.forestdepartment.gov.mm/researchbook?page=1'

header = {
    'Accept-Language':'en-US,en;q=0.9',
    'User-Agent':'Chrome/94.0.4606.81',
}

output = {}

col_names = ['Title','Filename','PDF Link']
out = pd.DataFrame()

for n in range(1,16):
    page = f'https://www.forestdepartment.gov.mm/researchbook?page={n}'
    r = s.get(page, headers=header, verify=False)
    name = [i.text for i in r.html.find("span.field-content")]
    f_name = [i.text for i in r.html.find("span.file")]
    l = [i.absolute_links for i in r.html.find("span.file > a")]
    if len(name) == len(f_name) and len(f_name) == len(l):
        print('Length Equal')
    else:
        print('Not equal')
        print(r.html.url)
    
    for i in range(len(name)):
        try:
            output = {
                'Title':name[i] , 
                'Filename':f_name[i],
                'PDF Link':list(l[i])[0]
            }
            out = out.append(output,ignore_index=True)
            #print(output)
        except:
            print("List out of Length")
out.to_csv("./forest_research.csv")
    
