# if condition

age = 15

if age < 18:
    print("You are young")

# if...else condition

age = 20
if age < 18:
    print("You are young")
else:
    print("You can drive vehicle")


# else if condition

age = 60

if age <= 18:
    print("You are young")
elif age == 60:
    print("Wow, you are 60")
else:
    print("You can drive vehicle")


# and

age = 80

if age <= 18:
    print("You are young")
elif age >= 60 and age <= 80:
    print("You are old drive safely")
else:
    print("You can drive vehicle")

# NOTE: for using or logical operator we use or keyword in python just like and

# Boolean values with conditionals

isLoggedIn = True

if isLoggedIn:
    print("Welcome user")
else:
    print("Please log in")


# Falsy values in Python

# Falsy values => 0, ""(empty string), [](empty array)
