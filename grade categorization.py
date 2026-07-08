A= int(input("enter the score 1: "))
B= int(input("enter the score 2: "))
C= int(input("enter the score 3: "))
D=(A+B+C)/3
if(D>=90):
    print("Excellent")
elif(75<=D<90):  
    print("Good")
elif(50<=D<75): 
    print("Average")
else:
    print("Needs")
