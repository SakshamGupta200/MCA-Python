n=int(input("enter your number"))
m=int(input("enter your number"))
x=0
hcf=0
if n<m:
    x=n
else:
    x=m
for i in range(1,x+1):
    if n%i==0 and m%i==0:
        hcf=i
print("hcf=",hcf)
    
    
    

