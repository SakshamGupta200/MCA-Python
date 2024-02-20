# Accept three integers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the greatest number using a nested if statement
if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3

# Print the greatest number
print("The greatest number is:", greatest)