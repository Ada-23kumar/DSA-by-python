from array import *
a1 = array("i",[112, 23, 45, 10, 12, 9, 50])
for x in range(len(a1)):
    for y in range(x+1,len(a1)):
        if(a1[x]>a1[y]):
            temp = a1[x]
            a1[x] = a1[y]
            a1[y] = temp
print(a1)