n=int(input("enter your number"))
for i in range(1,n):
    if i==5:
        print("terminated")
        break
    print(i,end="\t")
else:
    print("loop completed")
 
