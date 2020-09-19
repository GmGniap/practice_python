import urllib.request
from bs4 import BeautifulSoup

url = "http://tenders.yangon.gov.mm/companies.html"

with urllib.request.urlopen("http://tenders.yangon.gov.mm/companies.html") as url:
    s = url.read()
    soup = BeautifulSoup(s, "html.parser")
    '''for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        #print("Nome: %s, Cognome: %s, Email: %s") %\(tds[0].text, tds[1].text, tds[2].text)
        print(tr)'''
    quotes=[]  # a list to store quotes

    table = soup.find('div', attrs = {'id':'container'})

    for row in table.findAll('div', attrs = {'class':'quote'}):
        quote = {}
        quote['theme'] = row.h5.text
        quote['url'] = row.a['href']
        quote['img'] = row.img['src']
        quote['lines'] = row.h6.text
        quote['author'] = row.p.text
        quotes.append(quote)


