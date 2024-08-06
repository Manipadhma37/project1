# a=['mani','jega','lokki']
# b=['logsh']
# a.extend(b)
# s=[]
# for i in range(len(a)-1,-1,-1):
#     s=a[i]
#     print(s)

# a=[1,22,11,23]
# b=[33,44,22,88]
# a.extend(b)
# a.sort(reverse=True)

# print(a)  


#................................ swapping...............................
a=[2,1,2,8,90,100,23,24]

for i in range(0,len(a)-1,2):
        s=a[i]
        a[i]=a[i+1]
        a[i+1]=s
print(a)