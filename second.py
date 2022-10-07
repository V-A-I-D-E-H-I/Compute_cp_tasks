a=str(input())
b=str(input())
l1=list(a)
l2=list(b)

for i in range(0,len(l1)):
    e=l1[i]
    l2.remove(e)

print (l2[0])