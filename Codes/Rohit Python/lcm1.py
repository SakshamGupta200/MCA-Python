a=int(input("enter first number"))
b=int(input("enter second number"))
x=0
lcm=0
if a>b:
    x=a
else:
    x=b
while(x):
    if x%a==0 and x%b==0:
        lcm=x
         break
    x+=1
print("lcm=",lcm)

