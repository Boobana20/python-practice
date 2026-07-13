# Write Python 3 code in this online editor and run it.
n=5
for i in range(1,n+1):
  m=0
  for j in range(n-i):
      print(" ",end="")
  for k in range(i): 
      m=m+1
      print(chr(64+m),end="")
  for l in range(i-1): 
      m=m-1
      print(chr(64+m),end="")   
  print()     
