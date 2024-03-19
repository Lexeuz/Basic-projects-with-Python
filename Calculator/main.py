from art import logo
import os

print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

while True:
    num1 = float(input("+ "))

    for symbol in operations:
        print(symbol)
    symbol = input("Pick a symbol: ")

    num2 = float(input("Next number: "))
    result = operations[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {result}")

    while input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new operation: ") == 'y':
            symbol = input("Pick a symbol: ")
            num2 = int(input("Next number: "))
            new_result = result
            result = operations[symbol](result, num2)
            print(f"{new_result} {symbol} {num2} = {result}")

    os.system('cls')

# Alexander E. Adarme, 03.2024.