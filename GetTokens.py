from Parameters_and_utilities import ArithmeticOperations, is_number

def GetTokens(expr):
    # get rid of spaces
    expr = expr.replace(" ","")
    # . sign is allowed to determine a number as well as the ,
    expr = expr.replace(",",".")
    curr_number=""
    tokens = []
    for i in range(len(expr)):
        if expr[i].isdigit() or expr[i]== ".":
            curr_number += expr[i]
        if expr[i] in ArithmeticOperations:
            tokens.append(curr_number)
            tokens.append(expr[i])
            curr_number=""
    tokens.append(curr_number)
    if is_number(tokens[0]):
        tokens.insert(0,"+")
    elif tokens[0]=="":
        tokens.pop(0)
    return tokens