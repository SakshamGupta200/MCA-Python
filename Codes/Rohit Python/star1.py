n=int(input("enter your number"))
s=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or i==1 or j==1 or j==i:
            print("*",end="")
        else:
            print(end=" ")
    print("")
for i in range(1,n+1):
    for j in range(1,n+1):
        s=j/2
        if j==1 or j==s:
            print("*",end="")
        else:
            print(end=" ")
    print("")
