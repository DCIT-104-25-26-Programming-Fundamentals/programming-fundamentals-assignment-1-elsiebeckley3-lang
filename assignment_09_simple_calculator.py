# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# Function definitions for arithmetic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return round(num1 / num2, 2)

def modulus(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 % num2

def exponentiate(num1, num2):
    return num1 ** num2

def display_menu():
    print("\n==================================")
    print("       SIMPLE CALCULATOR          ")
    print("==================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()
        
        choice = input("\nSelect an operation (1-7): ").strip()
        
        if choice == '7':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please select a valid option from 1 to 7.")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid numeric input. Please enter valid numbers.")
            continue

        # Perform calculation based on user selection
        if choice == '1':
            res = add(num1, num2)
            print(f"Result: {num1} + {num2} = {res}")
        elif choice == '2':
            res = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {res}")
        elif choice == '3':
            res = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {res}")
        elif choice == '4':
            res = divide(num1, num2)
            if isinstance(res, str):
                print(res)
            else:
                print(f"Result: {num1} / {num2} = {res}")
        elif choice == '5':
            res = modulus(num1, num2)
            if isinstance(res, str):
                print(res)
            else:
                print(f"Result: {num1} % {num2} = {res}")
        elif choice == '6':
            res = exponentiate(num1, num2)
            print(f"Result: {num1} ** {num2} = {res}")


if __name__ == "__main__":
    main()
