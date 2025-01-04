import random

tries = 0
print ("please enter a number between 1 and 100")

random = random.randint(1,100)
guess = int(input())
while guess != random:
    tries = tries + 1
    if guess < random:
         print ("too low")
    else:
        print ("too high")
    guess = int(input())
print ("you got it! tries: ", tries)
    