from lxml import html
import requests

#page = requests.get('https://www.google.com/maps/d/viewer?mid=19WkWkS-_ahnDOFJPZmQMx0ArOyg&ll=37.51593831115094%2C-76.29079050000001&z=9')
page = requests.get('https://www.google.com/maps/d/u/0/viewer?mid=19UMzdgRnnmZMIgKupdHr9P_adco-81tp&ll=25.394860000000005%2C97.39547&z=8')

tree = html.fromstring(page.content)

vars = tree.xpath('//script/text()')
print(vars)