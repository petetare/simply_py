import random

x = random.randint(1,5)
y = int(input("Guess a number between 1 and 5: "))
while y != x:
    y = int(input("INCORRECT! Guess Again: "))
    
print ("CORRECT! The number was", x)
