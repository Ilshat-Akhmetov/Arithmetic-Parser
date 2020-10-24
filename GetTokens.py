from Parameters_and_utilities import AllowedOperators, is_number


def GetTokens(expr):
    # get rid of spaces
    expr = expr.replace(" ", "")
    # . sign is allowed to determine a number as well as the ,
    expr = expr.replace(",", ".")
    curr_number = ""
    tokens = []
    for i in range(len(expr)):
        if expr[i].isdigit() or expr[i] == ".":
            curr_number += expr[i]
        if expr[i] in AllowedOperators:
            tokens.append(curr_number)
            tokens.append(expr[i])
            curr_number = ""
    tokens.append(curr_number)
    tokens=list(filter(lambda a: a != '', tokens))
    return tokens


def FixTokens(tokens):
    if is_number(tokens[0]) or tokens[0]=="(":
        tokens.insert(0, "+")
