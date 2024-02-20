def find_greatest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
greatest = find_greatest(num1, num2)
print("The greatest number is:", greatest)
