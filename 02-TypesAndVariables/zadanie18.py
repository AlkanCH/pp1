import math

a=input("a=")
b=input("b=")
c=input("c=")

a=float(a)
b=float(b)
c=float(c)

p=(a+b+c)/2
a=math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Area = {a}")