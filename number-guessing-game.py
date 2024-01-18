import random


print("---WELCOME TO THE GAME MY FRIEND---\n")

right_number = random.randint(1,10)

while True:

    try:
        their_number = int(input("Pick a number between 1-10:    "))
        break


    except ValueError:
        print("I need a number between 1 and 10 please.")
        

while True:

    while their_number != right_number:
        print("Ooooooo not quite, try again!!!    ")
        their_number = int(input("Pick another number between 1-10:    "))
        
    
    print(f"You got it!!! The number was {right_number}. Great job!!!")
    break
