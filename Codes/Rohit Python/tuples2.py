#pirnt tuples one by one
t1=10,20,30,40,50,60
c=0
for i in t1:
    print("t1[%d]-%d"%(c,i))
    c+=1
print("max=",max(t1))
print("min=",min(t1))
print(t1*3)
del t1
print(t1)
