AllowedOperators = ["+", "-", "*", "/", "(", ")"]
AllowedCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
AllowedCharacters = AllowedCharacters + AllowedOperators


def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    return True
