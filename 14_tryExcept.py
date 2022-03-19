

from cmath import e


try:
    # If here instead of number user enters aphabet then it breaks the code with error that's why we use try/except.
    num = int(input("Enter a number: "))
    print(num)
except:
    print("Invalid Input")

# For different type of errors in try block we can have different except


try:
    value = 10 / 0
    # If here instead of number user enters aphabet then it breaks the code with error that's why we use try/except.
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError:
    print("Trying to divide number by zero is invalid")
except ValueError:
    print("Invalid Input")

#  Trying to print out default error messages


try:
    value = 10 / 0
except ZeroDivisionError as error:
    print(error)
