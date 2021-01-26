from math import sqrt 

def eucl_distance(row1, row2):
    distance = 0.0 
    #print(len(row1))
    for i in range(len(row1)-1):
        #print(i)
        distance += (row1[i] - row2[i])**2 
    return sqrt(distance)

dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]

row0 = dataset[0]
#print(row0)
#print(len(row0))

for row in dataset:
    distance = eucl_distance(row0 , row)
    print(distance)