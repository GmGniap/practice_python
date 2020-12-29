import re
handle = open("mbox-short.txt")
count = 0
myRegex = re.compile(r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})')
myList = []
result = {}
hr = {}
for line in handle:
    if line.startswith("From"):
        count += 1
        # val = myRegex.findall(line)
        for m in myRegex.finditer(line):
            result = m.groupdict()
            for (k,v) in result.items():
                if k == 'hour':
                    # print(k,v)
                    myList.append(v)
#print(myList)
for x in myList:
    hr[x] = hr.get(x,0) + 1
for (a,b) in sorted(hr.items()):
    print(a,b)
#print(len(myList))