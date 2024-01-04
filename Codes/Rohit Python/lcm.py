a=int(input("enter first number"))
b=int(input("enter second number"))
x=0
lcm=0
hcf=0
if a<b:
    x=a
else:
    x=b
for i in range(1,x+1):
    if a%i==0 and b%i==0:
        hcf=i
lcm=(a*b)/hcf
print("hcf=",hcf)
print("lcm=",lcm)

    
        
    
    
