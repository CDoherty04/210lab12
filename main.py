"""
Name: Charlie Doherty
KUID: 3115329
EECS 210 Lab Session: Thursday 4-6
Lab: 12
Description: Program for converting an arithmetic expression from prefix to postfix form
Collaborators: None
"""

def convert(expression):
    # Split the expression into a list
    characters = expression.split()
    stack = []

    # Process characters in reverse order
    for c in reversed(characters):
        if c in "+-*/^":  # Operator
            # Pop two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Create the postfix expression and push back to the stack
            stack.append(f"{operand1} {operand2} {c}")
        else:
            stack.append(c)

    # The final result is the only element left in the stack
    return stack[0]


def main():
    expression = input("Enter an expression with spaces (Example - \"^ - x y 2\"):\n")

    print(f"Prefix: {expression}")
    print(f"Postfix: {convert(expression)}\n")


main()
