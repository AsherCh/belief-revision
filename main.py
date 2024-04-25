from Validator import *


if __name__ == "__main__":
    validator = Validator()

    def get_expression():
        exp = validator.validate(input())
        if exp:
            return exp
        else:
            print("Enter the expression")
            return get_expression()

    print("Enter your belief")
    expression = get_expression()  # Use this funcction to get the expression

    print("the expression you entered is valid", expression)
