n=int(input("enter your number"))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")
for i in range(3,n+3):
    for j in range(i+3,n+3):
        print(" ",end="")
    for j in range(3,i+3):
        print("* ",end="")
    print("")
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")

