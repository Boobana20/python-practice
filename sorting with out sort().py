n=[10,40,20,30,60]
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
       if n[i]>n[j]:
           x=n[i]
           n[i]=n[j]
           n[j]=x
print(n)  
