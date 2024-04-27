from sympy.logic.boolalg import to_cnf
from belief_base import *


def expand(belief_base, new_belief):
    # check if the new_belief is already in the belief base
    if belief_base.is_in_belief_base(new_belief):
        pass
    else:
        # get the last element's in the belief base priority
        last_priority = belief_base.get_last_priority()
        belief_base.add_belief(new_belief, last_priority + 1)
    return belief_base
