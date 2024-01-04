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
print("second list=",name2)
for i in name:
    for j in name2:
        if i not in name2:
            name3.append(i)
            break
        
           

print("new list=",name3)
