quantity=0
sum=0
mean=0
x=1

while x!=0:
    x=input("Enter number: ")
    x=int(x)

    quantity+=1
    sum+=x
quantity-=1
mean=sum/quantity
print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")