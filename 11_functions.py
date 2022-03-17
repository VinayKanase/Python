def greetUser():
    name = input("Enter your name: ")
    print("Hello " + name)


greetUser()

# Parameters in functions


def greetUser2(_name):
    print("Hello " + _name)


greetUser2("Vinay")

# return value in functions


def sum(num1, num2):
    return num1 + num2


sumOfNumbs = sum(4, 6)
print(sumOfNumbs)

# Default parameters


def increment(num, stepValue=1):
    return num + stepValue


print(increment(5))
