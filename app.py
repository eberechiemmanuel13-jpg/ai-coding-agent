
# Calculator App
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def calculator():
    print("Simple Calculator App\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    choice = input("Choose an operation: ")
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=" , add(num1, num2))
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=" , subtract(num1, num2))
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=" , multiply(num1, num2))
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(num1, "/", num2, "=" , divide(num1, num2))
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice. Please choose a valid operation.")
