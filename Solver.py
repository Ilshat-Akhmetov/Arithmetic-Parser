from Parameters_and_utilities import AllowedOperators
from StackForBrackets import get_enclosing_bracket_ind
from GetTokens import FixTokens


def arithm_parser(curr_token,next_token,general_sum, curr_variable):
    if curr_token in AllowedOperators:
        if curr_token == "-" or curr_token == "+":
            general_sum += curr_variable
            number_sign = int(curr_token + "1")
            curr_variable = float(next_token) * number_sign
        elif curr_token == "*":
            curr_variable *= float(next_token)
        elif curr_token == "/":
            curr_variable /= float(next_token)

    return general_sum, curr_variable

def solve_expression(tokens):
    FixTokens(tokens)
    general_sum = 0
    curr_variable = 0
    i=0
    while i<(len(tokens)-1):
        current_token = tokens[i]
        next_token = tokens[i + 1]
        if next_token=="(":
            closing_bracket_ind = get_enclosing_bracket_ind(tokens[i:],i)
            if (closing_bracket_ind!=False):
                value_in_brackets = solve_expression(tokens[i+2:closing_bracket_ind])
                next_token = value_in_brackets
                i=closing_bracket_ind
        general_sum, curr_variable = arithm_parser(current_token,next_token,general_sum,curr_variable)
        i+=1
    general_sum += curr_variable
    return float(general_sum)
