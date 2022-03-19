from operator import not_
import random

number = random.randint(0, 9)

stop = False

while not stop:
    userChoice = input("Enter any single digit number: ")

    if userChoice == "e":
        print("Thank You for playing!")
        stop = True
    else:
        userChoice = int(userChoice)
        if userChoice == number:
            print("Congrats, You guessed it correct")
            stop = True
        elif number < userChoice:
            print("Number you choosed is greater")
            print("enter 'e' to exit game")
        elif number > userChoice:
            print("Number you choosed is smaller")
            print("enter 'e' to exit game")
