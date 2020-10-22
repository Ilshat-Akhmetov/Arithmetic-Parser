from Parameters_and_utilities import ArithmeticOperations




def arithm_parser(curr_token,next_token,general_sum, curr_variable):
    if curr_token in ArithmeticOperations:
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
    general_sum = 0
    curr_variable = 0
    for i in range(len(tokens)-1):
        current_token = tokens[i]
        next_token = tokens[i+1]
        general_sum, curr_variable = arithm_parser(current_token,next_token,general_sum,curr_variable)
    general_sum += curr_variable
    return float(general_sum)
