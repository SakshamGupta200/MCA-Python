a=input("enter your mobile number=")
b=len(a)
c=ord(a[0])
s=0
f=0

if b==10:
    
        
        if c<54 or c>58:
            print("invalid number \n start should be between 6 to 9")
               
        else:
            #print("valid number")
            for i in range(1,10):
                   d=ord(a[i])
                   if d>47 and d<58:
                       s+=1
                       
                      
                   else:
                        s=0
                        break
            if s!=0:
                 print("valid number")
            else:
                print("charecter not allowed")
else:
    print("it should be 10 digit")
