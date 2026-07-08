A = int(input("Enter the PIN: "))

if A == 1234:
    B = int(input("Enter the amount to withdraw: "))

    if B <= 5000:
        print("Transaction Successful")
    else:
        print("Insufficient Limit")
else:
    print("Invalid PIN")
