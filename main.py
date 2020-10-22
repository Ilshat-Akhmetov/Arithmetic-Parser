# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from GetTokens import GetTokens
from Solver import solve_expression





if __name__ == '__main__':
    expression = input()
    tokens = GetTokens(expression)
    print(solve_expression((tokens)))
