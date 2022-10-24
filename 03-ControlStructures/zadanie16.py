x=input("Enter first number: ")
y=input("Enter second number: ")

x=int(x)
y=int(y)

if x > y:
    z=x
    x=y
    y=z

print(f"Numbers in ascending order: {x}, {y}")