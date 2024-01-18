import random


# Create a welcome message that will be printed to the console. 

print("---WELCOME TO THE GAME MY FRIEND---\n")


# A random number should be chosen in the range 1-10.

# right_number = random.randint(1,10)
# their_number = int(input("Pick a number between 1-10:    "))

# As a player of the game, I should be continuously prompted for a guess until I get it right.




right_number = random.randint(1,10)

while True:


    print(right_number)

    try:
        their_number = int(input("Pick a number between 1-10:    "))
    except ValueError:
        their_number = int(input("I need a number between 1 and 10 please."))
        

    # except ValueError:
    #     their_number = print("Please print a number.")

    if their_number != right_number:
        print("Ooooooo not quite, try again!!!    ")
        their_number = int(input("Pick another number between 1-10:    "))
        
    else:
        print(f"You got it!!! The number was {right_number}. Great job!!!")
        break
