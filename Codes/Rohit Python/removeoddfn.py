list1=[]
list2=[]
list3=[]
n=int(input("enter list length="))
for i in range(1,n+1):
    list1.append(int(input("enter your number=")))
for i in list1:
    if i not in list2:
        list2.append(i)
for i in list2:
    if i%2!=0:
        list2.remove(i)
        
print("first list=",list1)
print("my list=",list2 )
