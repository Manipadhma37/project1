a = input("Enter the gender: ")

if a == "male":
    b = int(input("Enter the age: "))
    if b >= 12 and b <= 18:
        c = float(input("Enter the hemo lvl: "))
        if c >= 13.0 and c <= 16.0:
            print("Hemo lvl is good")
        else:
            print("Hemo lvl is in bad condition")
    elif b > 18:
        c = float(input("Enter the hemo lvl: "))
        if c >= 13.6 and c <= 17.7:
            print("Hemo lvl is good")
        else:
            print("Hemo lvl is in bad condition")
    else:
        print("Wrong age")

elif a == "female":
    b = int(input("Enter the age: "))
    if b >= 12 and b <= 18:
        c = float(input("Enter the hemo lvl: "))
        if c >= 12.0 and c <= 16.0:
            print("Hemo lvl is good")
        else:
            print("Hemo lvl is in bad condition")
    elif b > 18:
        c = float(input("Enter the hemo lvl: "))
        if c >= 12.1 and c <= 15.1:
            print("Hemo lvl is good")
        else:
            print("Hemo lvl is in bad condition")
    else:
        print("Wrong age")

elif a == "child":
    b=input("month or year:")
    if b=="month":
        b1=int(input("enter month:"))
        if b1<1:
            c=int(input("enter hemo lvl:"))
            if c>10.0 and c<=20.0:
                print("hemo lvl is normal")
            else:
                print("hemo lvl is abnoraml")
        elif b1>=1 and b1<=2:
            c=int(input("enter hemo lvl:"))
            if c>10.0 and c<=18.0:
                print("hemo lvl is normal")
            else:
                print("hemo lvl is abnoraml")
        elif b1>2 and b1<=6:
            c=int(input("enter hemo lvl:"))
            if c>10.5 and c<=13.5:
                print("hemo lvl is normal")
            else:
                print("hemo lvl is abnoraml")
        else:
            print("wrong month:")
    
    elif b=="year":
        b1=int(input("enter year:"))
        if b1>=1 and b1<=2:
            c=int(input("enter hemo lvl:"))
            if c>10.5 and c<=13.5:
                print("hemo lvl is normal")
            else:
                print("hemo lvl is abnoraml")
        elif b1>=2 and b1<=6:
            c=int(input("enter hemo lvl:"))
            if c>11.5 and c<=13.5:
                print("hemo lvl is normal")
            else:
                print("hemo lvl is abnoraml")
        elif b1>6 and b1<=12:
            c=int(input("enter hemo lvl:"))
            if c>11.5 and c<=15.5:
                print("hemo lvl is normal")
            else:
                print("hemo lvl is abnoraml")
        else:
            print("wrong year:")
else:
    print("invalid character")
    
                    
    
    
  
