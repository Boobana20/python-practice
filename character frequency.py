a="banana"


for i in range(len(a)):
    n=0
    
    if a[i]in a[:i]:
    
        continue
        
    for j in range(len(a)):
           if(a[i]==a[j]):
             n=n+1
    print(n)  
   
