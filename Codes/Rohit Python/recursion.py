def fun(n):
    if n==1:
        return 1
    else:
        return n*fun(n-1)

a=int(input("enter your number="))
fact=fun(a)
print("factorial=",fact)

