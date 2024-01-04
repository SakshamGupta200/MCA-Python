num1=[]
num2=[]

n=int(input("enter list length"))
for i in range(1,n+1):
    num1.append(int(input("enter list number=")))
for i in range(1,n+1):
    num2.append(int(input("enter second list number=")))
#print all the list----
print(num1)
#print list in multiply number which is given by the user
print(num1*3)
#print both list in a single list using concate(+)
print(num1+num2)
#print max number using max function
print("max=",max(num1))
print("max2=",max(num2))
#print minimum number in a list using min function
print("min=",min(num1))
print("min2=",min(num2))

#it will delete the list and if we pass the index no than its delete the value
del num1[2]
print(num1)
