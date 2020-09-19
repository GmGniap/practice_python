X = int(input("Enter X value: "))
Y = int(input("Enter Y value: "))
arr = []
arr.append(X)
#print(arr)

#if (a+b) >= Y:
a = X//Y
b = X%Y
X = a + b
#print("Upper: %d" %X)
arr.append(a)
#print(arr)

while X >= Y:
    a = X // Y
    b = X % Y
    arr.append(a)
    X = a + b
    #print("Inner: %d" %X)
    #print(arr)

print("Total: ")
print(arr)
print(sum(arr))
