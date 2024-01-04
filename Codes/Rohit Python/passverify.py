a=input("enter your password=")
b=len(a)
x=0
y=0
z=0
k=0

if b>5 and b<17:
    for i in range(0,b):
        d=ord(a[i])
        #number
        if d>47 and d<58:
            x+=1
       
        #upper  
        if d>64 and d<91:
            y+=1
        
        #lower  
        if d>96 and d<123:
            z+=1
       
        #symbol
        if d==35 or d==64 or d==36:
            k+=1
       
    if x==0:
        print("enter atleast one number")
    if y==0:
        print("enter atleast one capital letter")
    if z==0:
        print("enter atleast one lower case")
    if k==0:
        print("enter atleast one symbol")

    if x!=0 and y!=0 and z!=0 and k!=0:
        print("valid password")
        
       
    else:
         
         
         print("invalid password")
   
else:
    print("it should be minimum 6 letter and maximum 16 letter")


