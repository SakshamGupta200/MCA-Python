list1=[]
list2=[]
list3=[]
n=int(input("enter your length="))
for i in range(1,n+1):
    list1.append(int(input("enter element in list=")))
for j in range(1,n+1):
    list2.append(int(input("enter element in second list=")))
print("first list=",list1)
print("second list=",list2)
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
            break
print("new list=",list3)
