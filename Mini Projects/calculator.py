print(" ### CALCULATOR ###".center(100))


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
exit = False


def operations(choice):
    if choice == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"{num1} x {num2} = {num1 * num2}")
    elif choice == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
    elif choice == 5:
        exit = True


while not exit:
    print("\n")
    print(" # Menu #".center(100))
    print("\t\t\t\t\t    1. Addition")
    print("\t\t\t\t\t    2. Subtraction")
    print("\t\t\t\t\t    3. Multiplication")
    print("\t\t\t\t\t    4. Division")
    print("\t\t\t\t\t    5. Exit")

    operationChoice = int(input("\t\t\t\tEnter choice: "))
    operations(operationChoice)
