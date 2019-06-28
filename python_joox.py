import re
import urllib.request
#with open("C:\\Users\\User\\Desktop\\test.txt", "r", encoding="utf8") as file:

def search(word, sentences):
    return [i for i in sentences if re.search(r'\b%s\b' % word, i)]

#joox = "https://www.joox.com/mm/single/TdWPTjFLqphCV43Y04IlnA=="
joox = input("Input URL Here!")
id = joox.split('/')[-1]
final = ('http://api.joox.com/web-fcgi-bin/web_get_songinfo?songid=' + id)
urllib.request.urlretrieve(final, './Download/test.txt')
print(id)
print(final)

with open("./Download/test.txt", "r", encoding="utf8") as file:
    for line in file:
        #urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        #news = re.findall('"((http|ftp)s?://.*?)"', line)
        #for new in news:
            #print(new[0])
        #print(urls)'''

        news = re.split('"((http|ftp)s?://.*?)"', line)
        text = search('mp3', news)
        break

    #print(type(text))
    url = text[0]
    urllib.request.urlretrieve(url, './Download/app.mp3')
