print("enter any key")
n=input()
if n>=48 or n<=57:
    print("numeric key")
else if n>=65 or n<97:
    print("upper key")
else if n>=97 or n<124:
    print("lower case")
else:
    print("special symbol")
