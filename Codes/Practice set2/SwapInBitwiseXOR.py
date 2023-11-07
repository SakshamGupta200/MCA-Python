x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))

x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)
