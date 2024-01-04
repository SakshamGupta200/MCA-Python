# Swapping two variables without a third variable using arithmetic operations
# def swap_variables(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b


# Example usage
x = int(input("Enter 1st number :"))
y = int(input("Enter 2nd number :"))

print("Before Swapping :")
print("x =", x)
print("y =", y)

x = x + y
y = x - y
x = x - y

# x, y = swap_variables(x, y)

print("After swapping:")
print("x =", x)
print("y =", y)
