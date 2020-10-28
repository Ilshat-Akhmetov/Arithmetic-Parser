class GeneralError(Exception):
    def __init__(self,message):
        super(GeneralError, self).__init__()
        self.message=message
    def __str__(self):
        return self.message

class NotAllowedSymbol(GeneralError):
    def __init__(self, charachter, position):
        #super().__init__()
        self.message="At the position with index {} there is not allowed symbol {}".format(position,charachter)
class CannotConvertToNumber(GeneralError):
    def __init__(self, token, position):
        # super().__init__()
        self.message = "At the position with index {} " \
                       "there is an arithmetic error: Token {} cannot be converted to number".format(position, token)

class UnapplicableOperator(GeneralError):
    def __init__(self, token, position):
        # super().__init__()
        self.message = "At the position with index {} " \
                       "there is an arithmetic error: Token {} cannot be converted to operator".format(position, token)

class LackOfBrackets(GeneralError):
    def __init__(self, position):
        # super().__init__()
        self.message = "The bracket with index {} does not have enclosing one".format(position)