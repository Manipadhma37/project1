a=("bayerisch motoren werke aG commonly abbreviated to bmw")
b=a.split(" ")
s=0


for i in b:
   if s % 2 == 0:
      
      print(i.upper())
   else:
      print(i.lower())
   s=s+1







