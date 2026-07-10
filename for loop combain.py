n=int(input("how many number"))
if(n<=0):
  print("enter the number greater then zero")
else:
   positive=0
   negative=0
   zero=0

   A=int(input("enter the number"))
   total=A
   greater=A
   smaller=A
   if(A>0):
       positive=positive+1
   if(A<0):
       negative=negative+1
   if(A==0):
       zero=zero+1

   for i in range(1,n):
      B=int(input("enter the number"))
      total=total +B
      if(greater<B):
       greater=B
      if(smaller>B):
       smaller=B
      if(B>0):
       positive=positive+1
      if(B<0):
       negative=negative+1
      if(B==0):
       zero=zero+1   
   print("total",total)    
   print("average",total/n)
   print("smaller num",smaller)
   print("largest num",greater)
   print("positive ",positive)
   print("negative",negative)
   print("zero",zero)
    

   
   
   
