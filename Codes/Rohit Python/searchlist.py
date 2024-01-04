name=[]
m=0
x=0
n=int(input("enter your length="))
for i in range(1,n+1):
    name.append(int(input("enter number")))
m=int(input("enter your search number="))
for i in range(0,n):
    if m==name[i]:
        x+=1
        break
    else:
        name.append(m)
        break
    


if x!=0:
    print("your number=",m)
print(name)
    
#print("result=",m)
    
