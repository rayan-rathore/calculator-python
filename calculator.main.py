# calculator.py

from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def exponent(n1, n2):
    return n1 ** n2
def square(n1):
    return n1 ** 2

method = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
    "^": square

}

history= []
def valid_input():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("❌ Please enter a valid number. without any symbol or letter (digits only).")


def valid_operator():
    while True:
        print("Available operators:", " ".join(method.keys()))

        operator = input("Choose the operator: ")

        if operator not in method:
            print("❌ Invalid input. Please choose valid operator.")
            continue
        return operator


def valid_input2():

    while True:
        try:
            return int(input("Enter the second number: "))
        except ValueError:
            print("❌ Please enter a valid number. Without any symbol or letter (digits only).")


user_input = valid_input()

def calculator(input, input2, operator):
    return method[operator](input, input2)

while True:
    operator = valid_operator()

    if operator == "^":
        result = user_input ** 2
    else:
        user_input2 = valid_input2()

        if operator == "/" and user_input2 == 0:
            print("Can not divide by zero")
            continue

        result= calculator(user_input, user_input2, operator)
    history.append(result)
    print(result)
    print("History:", history)
    user_input = result

    continue_result= input("Do you want to continue with last result? (y = yes, n = reset, q = quit): ?\n").lower()
    if continue_result == "q":
        print("Thank you for using Calculator!")
        print("👋 Calculator closed. Goodbye!")
        break
    if continue_result.lower() != "y":
        print("\n" * 200)
        print(logo)
        history.clear()
        user_input=int(input("Enter a new number: "))



