import random

dice=random.randrange(1,6,1)

guess=input("Guess the number: ")

if int(guess) == dice:
    print("True")
#print(dice)