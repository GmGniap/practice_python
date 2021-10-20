import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen,Request,urlretrieve 
import urllib
import re 

site = "https://www.myanmar-ecosystems.org/myanmar-ecosystems"
def getdata(url):
    r = requests.get(url)
    return r.text 

htmldata = getdata(site)
soup = BeautifulSoup(htmldata, 'html.parser')

img_list = []

for item in soup.find_all('div', class_="t3iYD"):
    try:
        na = item.a['href']
        filename = re.search(r'\/myanmar-ecosystems\/([\w\d-]+)',na,re.IGNORECASE)
        if filename:
            title = filename.group(1)
        li = item.img['src']
        print(title)
        print(li + "\n")
        img_list.append(li)
        with open(title, 'wb') as f:
            im = requests.get(li)
            f.write(im.content)
    except:
        print("Some Error")
        print(len(img_list))
    

