def main(n,perm):
    
    if(n==1):
        print("-1")
        return 0

    sl=[]    
    for i in range(1,n+1):
        sl.append(i)
    
    
        
    fl=[]
    i=0
    while (i<n-1):
        if(sl[i]!=perm[i]):
            fl.append(sl[i])
            #print(sl[i], "from 1")
            i+=1
        else:
            fl.append(sl[i+1])
            #print(sl[i+1], "from2")
            fl.append(sl[i])
            #print(sl[i], "from2")
            i+=2
    if(len(fl)!=n):
        fl.append(sl[n-1])
        #print(sl[n-1], " from bahar")
    if(fl[n-1]==perm[n-1]):
        temp=0
        temp=fl[n-1]
        fl[n-1]=fl[n-2]
        fl[n-2]=temp
        #print("hua swap")
        
    print(fl)
    return 0
        
print("Enter n")    
n=int(input())
print("Input the permutation using spaces: ")
perm = [int(x) for x in input().split()]

main(n,perm)
