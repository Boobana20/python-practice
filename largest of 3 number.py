A=int(input("enter the number 1"))
B=int(input("enter the number 2"))
C=int(input("enter the number 3"))
if((A>B) and (A>C)):
    print("A is greater")
elif((B>A) and(B>C)):    
     print("B is greater")
elif((C>A)and(C>B)):
     print(" C is greater")     
elif((A==B)and(C>A)):
     print("C is greater and A and B are equal")
 
elif((A==C)and (B>C)):
     print("B is greater and A and C are equal")
elif((A==C)and(C>B)):
     print(" A and C are equal and greater")     
elif((B==C)and(C<A)):
    print("A is greater and C and B are equal")
elif((B==C)and(A<C)):
    print("B and C are equal and greater")    
else:
    print(" A and B  and C are equal")
    
