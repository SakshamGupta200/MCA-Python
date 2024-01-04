name=[]
m=0
n=int(input("enter your length="))
for i in range(1,n+1):
    name.append(int(input("enter number")))
m=name[0]
for i in range(0,n):
    if m<name[i]:
        m=name[i]


    
print("result=",m)
    
