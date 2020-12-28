new_dic = {}
#test = input().split()

'''
# using for loop 
for n in test:
    if n not in new_dic:
        new_dic[n] = 1
    else:
        new_dic[n] = new_dic[n] + 1


# using Get method 
for name in test:
    new_dic[name] = new_dic.get(name, 0) + 1
print(new_dic)
'''

jjj = { "Thet" : 96, "Paing" :8, "Shwe" : 100, "Myo": 95}
print(list(jjj))
print(jjj.keys())
print(jjj.values())

new = sorted(jjj.values())
print(new[-1])

new_jjj = sorted(jjj.values())
print(new_jjj)