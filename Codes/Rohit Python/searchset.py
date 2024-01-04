n=int(input("enter set length="))
num=set([])
s=0
for i in range(1,n+1):
    num.add(int(input("enter value in set=")))

print(num)
m=int(input("enter search number="))
for i in num:
    if i==m:
        s+=1
    else:
        num.add(m)
        break


if s!=0:
    print("data found")
    print(m)
else:
    print("data not found but successfully added in set")
    print(num)
