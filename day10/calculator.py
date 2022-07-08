# Calculator
from art import logo
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


def calculator():
    print(logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    keep_going = True
    num1 = float(input("What's the first number?: "))
    while keep_going:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        func = operations[operation_symbol]
        answer = func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"If you want to continue with {answer}, type 'y' or type 'n' if you want to start a new calculation: ")
        if should_continue == 'n':
            keep_going = False
            calculator()
        else:
            num1 = answer


calculator()
