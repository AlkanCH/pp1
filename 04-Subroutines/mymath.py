import random

def read_number():
    x=input("Enter a number: ")
    return int(x)

def generate_number():
    return random.randrange(1,10,1)