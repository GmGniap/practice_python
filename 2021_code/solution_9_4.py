name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
count = 0
dic = {}
for line in handle:
    if line.startswith("From:"):
        count += 1
        x = line.split()
        for n in x:
            dic[n] = dic.get(n, 0) +1
sort_dic = sorted(dic.values())
num = sort_dic[-2]

for a,b in dic.items():
    if b == num:
        print(a, b)