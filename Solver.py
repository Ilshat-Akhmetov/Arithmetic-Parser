from Parameters_and_utilities import AllowedOperators
from StackForBrackets import get_enclosing_bracket_ind
from GetTokens import fix_tokens
from CustomExceptionClass import (
    CannotConvertToNumber,
    UnapplicableOperator,
    LackOfBrackets,
)
from Parameters_and_utilities import is_number


def perform_current_operation(
    curr_token, next_token, general_sum, curr_variable, current_token_index
):
    if curr_token in AllowedOperators:
        if not is_number(next_token):
            raise CannotConvertToNumber(next_token, current_token_index + 1)
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
    fix_tokens(tokens)
    general_sum = 0
    curr_variable = 0
    curr_token_index = 0
    while curr_token_index < (len(tokens) - 1):
        current_token = tokens[curr_token_index]
        next_token = tokens[curr_token_index + 1]
        if next_token == "(":
            if is_number(current_token):
                raise UnapplicableOperator(current_token, curr_token_index)
            closing_bracket_ind = get_enclosing_bracket_ind(
                tokens[curr_token_index:], curr_token_index
            )
            if closing_bracket_ind != False:
                value_in_brackets = solve_expression(
                    tokens[curr_token_index + 2 : closing_bracket_ind]
                )
                next_token = value_in_brackets
                curr_token_index = closing_bracket_ind
            else:
                raise LackOfBrackets(curr_token_index)

        general_sum, curr_variable = perform_current_operation(
            current_token, next_token, general_sum, curr_variable, curr_token_index
        )
        curr_token_index += 1
    general_sum += curr_variable
    return float(general_sum)
