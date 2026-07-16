n=[10,20,30,40,10,20,50] 
x=[]
for i in range(len(n)):
    if n[i] in n[:i]:
        continue
    else:
        x.append(n[i])
        
print(x)  
