
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("YES")
        else: 
            print("NO")
    else:
        print("YES")
else:
    print("NO")

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("YES") 
elif year % 4 == 0 and year % 100 != 0:
    print ("YES")
else:
    print("NO")