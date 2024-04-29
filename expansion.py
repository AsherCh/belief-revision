from AGM_postulates_expansion import *
from AGM_postulate_consistency import *


def expand(belief_base, new_belief):
    old_belief_base = belief_base
    # check if the new_belief is already in the belief base
    if belief_base.is_in_belief_base(new_belief):
        pass
    else:
        # get the last element's in the belief base priority
        last_priority = belief_base.get_last_priority()
        new_belief_cnf = belief_base.string_to_cnf_friendly(new_belief)
        belief_base.add_belief(new_belief_cnf, last_priority + 1)

    AGM_check(old_belief_base, belief_base, new_belief)

    return belief_base


def AGM_check(old_belief_base, belief_base, new_belief):
    print("AGM postulates verification for Expansion:")
    success_postulate = is_success(old_belief_base, belief_base, new_belief)
    print("Success Postulate check:", success_postulate)
    inclusion_postulate = is_inclusion(old_belief_base, belief_base, new_belief)
    print("Inclusion Postulate check:", inclusion_postulate)
    vacuity_postulate = is_vacuity(old_belief_base, belief_base, new_belief)
    print("Vacuity Postulate check:", vacuity_postulate)

    base = []
    for priority, belief in belief_base.beliefs:
        belief_cnf_friendly = belief_base.string_to_cnf_friendly(belief)
        base += [to_cnf(belief_cnf_friendly, True)]
    consistency_postulate = not is_consistent(base)
    print("Consistency check of the new belief set:", consistency_postulate)
