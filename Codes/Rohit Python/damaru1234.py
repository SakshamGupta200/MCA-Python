n=int(input("enter the term="))
s=0
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
        
    print("")
s=n
for i in range(1,n):
    s-=1
    for j in range(n,i,-1):
        
        print(end=" ")
    for j in range(s,n+1):
        print(j,end=" ")
        
    print("")
    
        
        
    
