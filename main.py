# This is a sample Python script.
from CustomExceptionClass import GeneralError

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from GetTokens import get_tokens
from Solver import solve_expression


if __name__ == "__main__":
    expression = input()
    try:
        tokens = get_tokens(expression)
        print(solve_expression(tokens))
    except GeneralError as x:
        print(x)
