class GeneralError(Exception):
    def __init__(self, message):
        super(GeneralError, self).__init__()
        self.message = message

    def __str__(self):
        return self.message


class NotAllowedSymbol(GeneralError):
    def __init__(self, charachter, position):
        # super().__init__()
        self.message = "At index {} there is not allowed symbol {}".format(
            position, charachter
        )


class CannotConvertToNumber(GeneralError):
    def __init__(self, token, position):
        self.message = (
            "At index {} "
            "there is an arithmetic error: Token {} cannot be converted to number".format(
                position, token
            )
        )


class UnapplicableOperator(GeneralError):
    def __init__(self, token, position):
        self.message = (
            "At  index {} "
            "there is an arithmetic error: Token {} cannot be converted to operator".format(
                position, token
            )
        )


class LackOfBrackets(GeneralError):
    def __init__(self, position):
        self.message = "The bracket at index {} does not have enclosing pair".format(
            position
        )
