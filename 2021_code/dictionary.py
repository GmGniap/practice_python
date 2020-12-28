new_dic = {}
test = list(input().split())
for n in test:
    if n not in new_dic:
        new_dic[n] = 1
    else:
        new_dic[n] = new_dic[n] + 1
print(new_dic)