x = 5
# for i in range(x):
#     for j in range(x - i -1):
#         print(" ", end="")
#     print("*", end="")
#     for j in range(1,2*i):
#         print("+", end="")
#     if i >=1 :
#         print("*", end="")
#     print()
for i in range(x - 2, -1, -1):
    for j in range(x - i - 1):
        print(" ", end="")
    print("*", end="")
    for j in range(1,2 * i):
        print(" ", end="")
    if i >= 1:
        print("*",end="" )
    print() 