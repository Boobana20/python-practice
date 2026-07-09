A=int(input("Enter the number"))
N=A

for i in range(1,11):
   B=int(input("Enter the number"))
   if(A<B):
      A=B
      
   if(B<N):
      N=B
      
print("Greatest",A)
print("Smallest",N)
print("sum of greatest and smallest",A + N)
