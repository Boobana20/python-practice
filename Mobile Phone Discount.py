A= int(input("enter the amount of purchase"))

if(A>=10000):
  B=(input("member YES or NO:")) 
  if(B=="YES"):
       discount = (A * 20) / 100
       print("20% Discount")
       print("Discount Amount =", discount)
       
  else: 
       discount = (A * 10) / 100
       print("20% Discount")
       print("Discount Amount =", discount)
      
else:
    print("no discount")
