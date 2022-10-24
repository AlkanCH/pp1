humanY=input("Enter the dog's age in human years: ")
humanY=int(humanY)
dogY=0

if humanY>=2:
    dogY=4*(humanY-2)+2*10.5
    dogY=int(dogY)
else:
    dogY=humanY*10.5

print(f"The dog's age in dog's years is {dogY} years.")