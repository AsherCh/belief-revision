from Validator import *
from expansion import *
from entailment import *
from contraction import *

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
    # create a new BeliefBasePriority object with the initial belief
    belief_base = BeliefBasePriority()
    belief_base.add_belief(expression, 1)
    
    while 1:
        print("\nWhat would you like to do? Enter an integer (1-3)")
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
        new_belief = get_expression()

        if choice == 1:
            print("Checking for logical entailment")
            base = []
            for priority, belief in belief_base.beliefs:
                belief_cnf_friendly = belief_base.string_to_cnf_friendly(belief)
                base += [to_cnf(belief_cnf_friendly, True)]
            # check for logical entailment
            new_belief_cnf_friendly = belief_base.string_to_cnf_friendly(new_belief)
            if entailment(base, new_belief_cnf_friendly):
                print("Belief_base can entail new_belief")
            else:
                print("Belief_base doesn't entail new_belief")
            # check the consistency
            if is_consistent(base):
                print("Belief base is inconsistent")
            else:
                print("Belief base is consistent")

        elif choice == 2:
            print("Contraction of belief base")
            # contraction of belief base
            belief_base = contract(belief_base, new_belief)
            print("Belief base after contraction:")
            belief_base.print_beliefs()

        else:
            # expansion of belief base
            belief_base = expand(belief_base, new_belief)
            print("Belief base after expansion:")
            belief_base.print_beliefs()

    #print("the expression you entered is valid", expression)


