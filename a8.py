a=int(input("enter no:"))
for i in range(1,a+1):
    for j in range(i,a):
        print("-",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for m in range(2,i+1):
        print(m,end="")
    print()



for i in range(a-1,0,-1):
    for j in range(i,a):
        print("-",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for m in range(2,i+1):
        print(m,end="")
    print()
 



