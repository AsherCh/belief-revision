from sympy.logic.boolalg import to_cnf


def is_consistent(belief_base):
    if to_cnf(belief_base.belief_base_to_cnf_friendly(belief_base)) == False:
        return False
    else:
        # still have to figure out how to check for consistency if to_cnf returns p&~p
        return True