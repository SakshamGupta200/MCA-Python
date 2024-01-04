n=int(input("enter the term="))
s=0
i=1
while(i<=n):
    
#for i in range(1,n+1):
    j=1
    while(j<=i):
        
    #for j in range(1,i):
        print(end=" ")
        j+=1
    #for j in range(i,n+1):
    j=i
    while(j<=n):
        print(j,end=" ")
        j+=1
    i+=1
        
    print("")
s=n
#for i in range(1,n):
i=1
while(i<n):
    s-=1
    #for j in range(n,i,-1):
    j=n
    while(j>i):
        
        print(end=" ")
        j-=1
    #for j in range(s,n+1):
    j=s
    while(j<=n):
        print(j,end=" ")
        j+=1
    i+=1
        
    print("")
    
        
        
    
