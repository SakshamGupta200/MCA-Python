n=int(input("enter your number"))
m=n




s=0
for i in range(n):
    rem=n%10
    s=s+(rem*rem*rem)
    n=int(n/10)
    
    
if(m==s):
    print("armstrong")
else:
    print("not a armstrong number")
