# logical operator(and , or, not) = used to check if two or more conditional statement 

temp = int(input("What is the temperature outside : ?"))

if temp>0 and temp<=30 : 
    print("The Weather is great and good today ")
    print("Go outside")
elif temp<0 or temp>30:
    print("Dont go outside")


