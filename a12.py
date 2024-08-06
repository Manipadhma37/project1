a=5
for i in range(1,a+1):
    for j in range(i,a):
        print("-",end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()
    
for i in range(a-1,0,-1):
    for j in range(i,a):
        print("-",end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()