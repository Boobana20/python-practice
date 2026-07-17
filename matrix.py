a=[[10,20,30],
[40,50,60],
[70,80,90]]
total=0
for i in range(len(a)):
    R=[]
    for j in range(len(a[i])): 
        total=a[i][j]+total
        print(a[i][j],end="  ")
    print()

print("total",total)    
