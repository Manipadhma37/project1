a=("a-ab-bc-abc")
l=list(a)
d="".join(l)
s2=d.replace("-","")

s1=s2[::-1]
k=0
for i in d:
    if i!='-':
        repr=s1[k]
        k+=1
    else:
        repr=i
    print(repr, end='')
        






