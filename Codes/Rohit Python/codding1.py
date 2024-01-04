import codding as cd
n=int(input("enter your number for getting ramse="))
d=cd.ramse(n)
if d==n:
    print("ramse no=",n)
else:
    print("not a ramse no=",n)


m=int(input("enter your number for geting armstrong number="))
s=cd.armstrong(m)
if m==s:
    print("armstrong number=",m)
else:
    print("not armstrong number=",m)


m=int(input("enter your number for checking prime number="))
e=cd.prime(m)
if e!=0:
    print("prime number=",m)
else:
    print("not a prime number=",m)


p=int(input("enter your first number for LCM ="))
k=int(input("enter your second number for LCM ="))
f=cd.lcm(p,k)
print("LCM =",f)
