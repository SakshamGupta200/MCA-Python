name=[]
name2=[]
name3=[]
name4=[]

n=int(input("enter your length="))
for i in range(1,n+1):
    name.append(int(input("enter first list")))
m=int(input("enter your second list length="))
for j in range(1,m+1):
    name2.append(int(input("enter second list")))
print("first list=",name)
print("first list=",name2)
for i in name:
    for j in name2:
        if i not in name2:
            name3.append(i)
            break
        else:
            name3.append(j)
for i in name3:
    
    if i not in name4:
        name4.append(i)
   
            

print("new list=",name4)
