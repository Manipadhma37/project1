c=5
for i in range(c):
    for j in range(c -i -1):
        print(" ",end="")
    print("*",end="")
    for j in range(1,2*i):
        print("*",end="")
    if i>=1:
     print("*",end="")
    
    print()
    
    
for i in range(c-2,-1,-1):
    for j in range(c -i -1):
        print(" ",end="")
    print("*",end="")
    for j in range(1,2*i):
        print("*",end="")
    if i>=1:
     print("*",end="")
    
    print()