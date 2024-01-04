def ramse(a):
    sum=0
    while(a>0):
        rem=a%10
        sum=sum+fact(rem)
        a=int(a/10)
    return sum
    #it will return value where its call and that place we check the ramse number
def fact(b):
    factt=1
    for i in range(1,b+1):
        factt=factt*i
    return factt

def armstrong(a):
    c=0
    while(a>0):
        rem=a%10
        c=c+(rem*rem*rem)
        a=int(a/10)
    return c
    #it will retuen value where its call and that place we check the armstrong number
def prime(a):
    flag=0
    for i in range(2,a):
        if a%i==0:
            flag+=1
    return flag
    #it will retuen value where its call and that place we check the prime number
def lcm(a,b):
    hcf=0
    
    x=0
    if a>b:
        x=a
    else:
        x=b
    for i in range(1,x+1):
        if a%i==0 and b%i==0:
            hcf=i
    lcm=(a*b)/hcf
    return lcm
    #it return the value and we print the result on that place
        

            
