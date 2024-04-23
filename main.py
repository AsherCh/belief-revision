from Validator import *


if __name__ == "__main__":
    validator = Validator()

    def get_expression():
        exp = validator.validate(input())
        if exp:
            return exp
        else:
            print("Enter the expression")
            get_expression()

    print("Enter your belief")
    expression = get_expression()

    print("the expression you entered is valid", expression)
