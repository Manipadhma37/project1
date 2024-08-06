a=int(input("enter the no:"))
for i in range(a):
    for k in range(a,i,-1):
        print(k,end="")
    for j in range(i*2):
        print(" ",end="")
    for j in range(i+1,a+1):
        print(j,end="")
    print()
     
    
for i in range(a,0,-1):
    print('',end="")
    for k in range(a,i-1,-1):
        print(k,end="")
    for j in range(i*2-2):
        print(" ",end="")
    for j in range(i,a+1):
        print(j,end="")
    print()