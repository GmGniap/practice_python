import pandas as pd 
data = pd.read_csv('./skill_tree.csv')

child = data.Child.tolist()
parent = data.Parent.tolist()

nodes = child + parent 
nodes = list(dict.fromkeys(nodes))
# print(nodes)

node_positions = [i for i in range(len(nodes))]

pairs = []
i = 0 
while i < len(child):
    pairs.append([child[i], parent[i]])
    i += 1 

weights = []
for i in pairs:
    weights.append(pairs.count(i)) 

count = 0 
for i in pairs: 
    i.append(weights[count])
    count += 1 

unique = []
c = 0 
while c < len(child):
    if pairs[c] not in unique:
        unique.append(pairs[c])
    else:
        pass 
    c += 1

links = dict(zip(node_positions, unique))
# print("\n :Links: \n")
# print(links)

node_list = []
for i in nodes:
    text = "{\"data\":" + "{\"id\":" + "\"" + i + "\"" + "," +"\"label\":" + "\"" + i + "\"" + "}" + "}"
    # print(text)
    node_list.append(text)
# print(node_list)
link_list = []
for key,value in links.items():
    # print(key)
    # print(value)
    # source = str(key)
    # target = str(nodes.index(value[1]))
    source = str(value[0])
    target = str(value[1])
    weight = str(value[2])
    text = "{\"data\":" + "{\"source\": "+ "\"" + source + "\"" + ",\"target\":" + "\"" + target + "\"" +",\"weight\":" + "\"" +weight + "\""+ "}" + "}"
    # print(text)
    link_list.append(text)
    # print("\n ------ \n")
# print(link_list)
# print(links)

with open("./test.json", "w") as test:
    test.writelines("[")
    z = 0 
    while z < (len(node_list) - 1):
        test.writelines(node_list[z] + ",")
        z += 1
    test.write(node_list[-1])
    test.write(",")
    z = 0 
    while z < (len(link_list) - 1):
        test.writelines(link_list[z] + ",")
        z += 1
    test.write(link_list[-1])
    test.write("]")
