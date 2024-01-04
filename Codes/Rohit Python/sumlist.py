name=[]
m=0
n=int(input("enter your length="))
for i in range(1,n+1):
    name.append(int(input("enter number")))
for i in range(0,n):
    m=m+name[i]
print("result=",m)
    
