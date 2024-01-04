name=[]
name2=[]

n=int(input("enter your length="))
for i in range(1,n+1):
    name.append(int(input("enter number")))
print("my list=",name)
for i in name:
    if i not in name2:
        name2.append(i)
print("new list=",name2)
 
