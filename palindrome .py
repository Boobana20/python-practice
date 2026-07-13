# Online Python compiler (interpreter) to run Python onl
n="madam"

m=True
for i in range(len(n)//2):
  if(n[i]!=n[len(n)-1-i]):
    m=False
    break
if(m):
 print(" palindrome")
else:
   print(" not")     
