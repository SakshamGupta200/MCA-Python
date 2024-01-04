import os
k=input("enter your file name")
pt=open(k,'r')
st=pt.read()
print(st)

l=input("enter your file name=")
jj=open(l,'w')
jj.write(st)
print("DONE")
pt.close()
q=input("enter your file name")
os.remove(q)

jj.close()
