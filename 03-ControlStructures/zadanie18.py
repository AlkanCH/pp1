amount=input("Enter the amount in PLN: ")
total=int(amount)
c5=0
c2=0
c1=0

if total>=5:
    c5=total//5
    total=total-c5*5
if total>=2:
    c2=total//2
    total=total-c2*2
c1=total


print(f"The amount of PLN {amount} in coins: \n5 zł - {c5}\n2 zł - {c2}\n1 zł - {c1}")