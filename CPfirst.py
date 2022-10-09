#assuming only incrementation is allowed and not decrementation

print("Input a")
a=int(input())
print("Input b")
b=int(input())

if(a%b==0):
    print ("0 moves, already divisible")
ctr=1
for i in range(a+1,a+b):
    if((i%b)!=0):
        ctr+=1
    else:
        print(ctr," moves")
