import random
x = random.randint(1, 100)
tries = 0
guess = 0
while(guess != x):
    guess = int(input("Enter a number between 1 and 100: "))
    tries += 1
    if(guess == x):
        print("You got it in " + str(tries) + " tries!")
    elif(guess > x):
        print("Too high!")
    else:
        print("Too low!")
