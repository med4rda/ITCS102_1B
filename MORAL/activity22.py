#MODULES -- Python management

import random

print("GUESSING GAME . . . . . ")
print("======================\n")

#Setting up random values
random_value = random.randint(1,5) #Generate random integer value (start m stop)
tries = 0
go = True

while go == True:
    num = eval(input("Guess a random number from 1 to 50 -->"))
    
    tries += 1
    if num == random_value:
        print("Win! Send Gcash!")
        print(f"Random Values is {random_value}")
        break
    else:
        print("Incorrect. Please try again")
        continue
print(f"You guessed {tries} times")