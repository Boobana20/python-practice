# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

p=0
n=0
z=0
e=0
o=0
for i in range(0,11):
    B=int(input("Enter the number"))
    if(B>0):
      p=p+1
      if(B%2==0):
         e=e+1
      else:
          o=o+1 
    if(B<0): 
        n=n+1
        if(B%2==0):
         e=e+1
        else:
          o=o+1 
    if(B==0):
       z=z+1
print("positive",p)
print("negative",n)
print("zero",z)
print("even",e)
print("odd",o)
