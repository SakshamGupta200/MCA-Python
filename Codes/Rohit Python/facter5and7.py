#n=int(input("enter your number"))

count=0

for i in range(1500,2700):
    
    if i%5==0 and i%7==0:
        print("divisible of 5 and 7=",i)
        count+=1
print("total number =",count)
    

