n=int(input("enter your number"))
if n%4==0 and n%100!=0 or n%400==0:
    print("leap year")
else:
    print("not a leap year")
