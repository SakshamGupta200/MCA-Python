list1=[]
n=int(input("enter length="))
for i in range(1,n+1):
    list1.append(int(input("enter number in list=")))
print(list1[:])
print(list1[:7])
print(list1[0:])
print(list1[2:6])
print(list1[1:7:2])
