print("enter any key")
m=input()
n=ord(m)
if n>=48 and n<=57:
    print("numeric key")
elif n>=65 and n<97 :
    print("upper key")
elif n>=97 and n<124:
    print("lower case")
elif n>57 and n<65:
    print("special symbol")
else:
    print("special symbol")
    
