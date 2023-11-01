bs = float(input("Enter the Basic Salary :"))
if bs < 15000:
    hra = bs * 0.1
    da = bs * 0.9
else:
    hra = 5000
    da = bs * 0.98

gs = bs + hra + da
print("Gross Salary Rs :", gs)
