salary=[]
salary1=[]

n=int(input("enter the list length"))
s=0
for i in range(1,n+1):
    salary.append(int(input("enter the salary in list")))
for i in range(0,n):
    if salary[i]>2000:
        salary[i]=salary[i]+salary[i]*.30

print(salary)



