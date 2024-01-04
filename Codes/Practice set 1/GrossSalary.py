bs = float(input("Enter the Basic Salary :"))
if bs < 15000:
    hra = bs * 0.1
    da = bs * 0.9
    print("HRA = ", hra)
    print("DA = ", da)
else:
    hra = 5000
    da = bs * 0.98
    print("HRA = ", hra)
    print("DA = ", da)

gs = bs + hra + da
print("Gross Salary Rs :", gs)
