n=[10,40,20,30,60]
x=40
found = False
n.sort()
print(n)
low=0
high=len(n)-1

while  low<=high:
    mid= (low+high)//2
    if(n[mid]==x):
     print("found in ",mid)
     found = True
     break
    elif(x>n[mid]): 
     low=mid+1
    else:
     high=mid-1 
if  found==False:
    print("not found")
