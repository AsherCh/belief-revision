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

    print("Belief revision system")
    print("Enter your initial belief:")
    expression = get_expression()  # Use this function to get the expression

    while 1:
        print("What would you like to do? Enter an integer (1-3)")
        print("1 - Check logical entailment")
        print("2 - Contraction of belief base")
        print("3 - Expansion of belief base")

        choice = input()
        is_correct = False
        while not is_correct:
            # check if the input is an integer between 1 and 3
            if choice.isdigit() and 1 <= int(choice) <= 3:
                choice = int(choice)
                is_correct = True
            else:
                print("Invalid input. Please enter an integer between 1 and 3")
                choice = input()

        text = "Please enter expression that you would like to "
        if choice == 1:
            text += "check for logical entailment: "
        elif choice == 2:
            text += "contract from the belief base: "
        else:
            text += "expand the belief base with: "

        print(text)
        # this should also validate the input
        expression = get_expression()

        if choice == 1:
            print("Checking for logical entailment")
            # check for logical entailment

        elif choice == 2:
            print("Contraction of belief base")
            # contraction of belief base

        else:
            print("Expansion of belief base")
            # expansion of belief base

    #print("the expression you entered is valid", expression)


