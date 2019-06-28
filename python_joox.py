import re

with open("C:\\Users\\User\\Desktop\\test.txt", "r", encoding="utf8") as file:
    for line in file:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        new = re.findall('http[s]?://mm.stream.music.joox.com(<a +href="(.mp3+?)" *>)', line)
        print(new)
        print(urls)
