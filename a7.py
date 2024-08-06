a = int(input("enter the no:"))
for i in range(1,a+1):
    for j in range(i,a):
        print("-",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for m in range(2,i+1):
        print(m,end="")
    print()
 
