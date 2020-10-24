def get_enclosing_bracket_ind(s,opening_bracket_ind):
    stack = []
    for i in range(len(s)):
        if s[i]=="(":
            stack.append("(")
        elif s[i]==")":
            stack.pop()
            if len(stack) == 0:
                return i+opening_bracket_ind
    return False