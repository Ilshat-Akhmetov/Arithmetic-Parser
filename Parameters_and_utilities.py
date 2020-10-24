AllowedOperators = ["+", "-", "*", "/", "(", ")"]

def is_number(s):
    try:
        if float(s):
            return True
    except ValueError:
        return False