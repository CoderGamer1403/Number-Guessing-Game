import random
import math
# Number guessing game
count=0
print("Welcome To The Game")  #Starts message of the Game
lower=int(input("Select the lower number")) # Enter range of lower no.
upper=int(input("Select the upper number")) # Enter range of upper no.
number=random.randint(lower,upper) # Chooses a Random no.
print("\n Let's Start Guessing")
total_chances= math.ceil(math.log(upper - lower + 1, 2))  # Calculate the Chances
print("\n We are giving you",total_chances, "chances")
flag=0
while count<total_chances:
    count+=1
    x=int(input("Enter your guess"))
    if x>number:
        print("\nTry Again ! You guess high")
        print("\nYou left with",total_chances-count,"chances")
    elif x<number:
        print("\nTry Again ! You guess less")
        print("\nYou left with",total_chances-count,"chances")
    else:
        print("\nCongratulations !!!!  You Win ")
        print("\n You guessed in ",count,"th chances")
        flag=1
        break
if flag==0:
    print("\n YOU LOSS TRY AGAIN ")
    print("\n THE RIGHT ANSWER IS ",number)