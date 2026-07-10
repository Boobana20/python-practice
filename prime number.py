count=0
B=int(input("enter the number"))
for i in range(1,B+1):
  if(B%i==0):
      count=count+1
if(count==2):
     print(" prime")
else:
    print("not prime") 
