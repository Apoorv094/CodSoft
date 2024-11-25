# Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            choice = input("Enter the operation number (1-4): ")
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please select a number between 1 and 4.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != "yes":
                print("Thank you for using the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
