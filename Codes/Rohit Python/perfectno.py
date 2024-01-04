n=int(input("enter your number"))
m=n
a=1

s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==m:
       print("perfect number")
else:
    print("not a perfect number")
   
   
    

