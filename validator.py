from pyparsing import (
    infixNotation,
    opAssoc,
    Keyword,
    Word,
    alphas,
    ParserElement,
    ParseException,
)

ParserElement.enablePackrat()
ParserElement.setDefaultWhitespaceChars(" \t")


class Validator:
    def __init__(self):
        operand = Word(alphas, max=1)
        true = Keyword("True")
        false = Keyword("False")
        operand |= true | false
        self.expr = infixNotation(
            operand,
            [
                ("~", 1, opAssoc.RIGHT),  # NOT
                ("&", 2, opAssoc.LEFT),  # AND
                ("|", 2, opAssoc.LEFT),  # OR
                ("->", 2, opAssoc.LEFT),  # IMPLIES
                ("<->", 2, opAssoc.LEFT),  # EQUIVALENT
            ],
        )

    def validate(self, expression):
        """
        Validates and returns the expression if it is correct, otherwise returns an error message.
        """
        if not self.check_parentheses(expression):
            print("Invalid expression: Mismatched or improperly nested parentheses")
            return False

        try:
            self.expr.parseString(expression, parseAll=True)
            return expression
        except ParseException as pe:
            print(f"Invalid expression: {pe}")
            return False
        except Exception as e:
            print(f"Invalid expression: {str(e)}")
            return False

    def check_parentheses(self, s):
        """
        Check if parentheses are correctly nested and paired.
        """
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != "(":
                    return False
        return not stack
