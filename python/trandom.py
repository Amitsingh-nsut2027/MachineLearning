import random

num = random.randint(1,10)

while True:
    guess = int(input("Guess a number between 1 - 10 :- "))

    if num == guess:
        print