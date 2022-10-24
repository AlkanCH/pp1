PIN="0805"

for i in range(3):
    x=input("Enter the PIN code: ")
    if x==PIN:
        print("Correct!")
        break
    else:
        print("Incorrect")
        if i==2:
            print("Sorry, your payment card has been blocked.")