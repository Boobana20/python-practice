n=[10,40,20,30,60]
s=0
a=1
la=n[0]
sm=n[0]
for i in range(len(n)):
    
    if n[i]>la:
      la=n[i]
    if n[i] < sm:
       sm=n[i]
s=s+n[i]
a=s/len(n)       
print("sum",s)
print("average",a)
print("largest",la)
print("smallest",sm)
