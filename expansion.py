from sympy.logic.boolalg import to_cnf


def expand(belief_base, new_belief):
    # check if the new_belief is already in the belief base
    if to_cnf(new_belief) in to_cnf(belief_base):
        # if it is, return the belief base unchanged
        pass
    else:
        # otherwise, add the new belief to the belief base
        belief_base.append(new_belief)
    return belief_base
