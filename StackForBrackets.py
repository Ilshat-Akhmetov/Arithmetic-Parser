def get_enclosing_bracket_ind(s: list, start_ind: int) -> int:
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        elif s[i] == ")":
            stack.pop()
            if len(stack) == 0:
                return i+start_ind
    return False
