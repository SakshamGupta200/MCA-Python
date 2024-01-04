l = int(input("Enter lower limit: "))

r = int(input("Enter upper limit: "))
for a in range(l, r + 1):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        print(a, end=" ")











"""
Program Explanation
1. User must enter the upper limit of the range and store it in a different variable.
2. The first for loop ranges till the upper limit entered by the user.
3. The count variable is first initialized to 0.
4. The for loop ranges from 2 to the half of the number so 1 and the number itself aren’t counted as divisors.
5. The if statement then checks for the divisors of the number if the remainder is equal to 0.
6. The count variable counts the number of divisors and if the count is lesser or equal to 0, the number is a prime number.
7. If the count is greater than 0, the number isn’t prime.
8. The final result is printed.
"""
