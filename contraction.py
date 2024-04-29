from AGM_postulates_contraction import *
from AGM_postulate_consistency import *


def contract(belief_base, new_belief):
    base = []
    for priority, belief in belief_base.beliefs:
        belief_cnf_friendly = belief_base.string_to_cnf_friendly(belief)
        base += [to_cnf(belief_cnf_friendly, True)]
    print("Consistency check of belief set:", not is_consistent(base))  # consistency check,

    if belief_base.is_in_belief_base(new_belief):
        contracted_belief = belief_base.V2_find_Contracting_belief(belief_base,
                                                                   new_belief)  # version 2 updates exisitng belief base after contraction

    else:
        # else, return the base as it is.
        print("The Belief to Contract is not found in Belief Base")
        contracted_belief = belief_base

    AGM_check(belief_base, new_belief, contracted_belief)
    return belief_base


def AGM_check(belief_base, new_belief, contracted_belief):
    print("AGM postulates verification for Contraction:")
    success_postulate = is_success(belief_base, new_belief, contracted_belief)
    print("Success Postulate check:", success_postulate)
    inclusion_postulate = is_inclusion(belief_base, new_belief, contracted_belief)
    print("Inclusion Postulate check:", inclusion_postulate)
    vacuity_postulate = is_vacuity(belief_base, new_belief, contracted_belief)
    print("Vacuity Postulate check:", vacuity_postulate)


def contract2(belief_base, new_belief, new_belief2):
    extensionality_postulate = is_extensionality(new_belief, new_belief2)
    print("Extensionality Postulate check:", extensionality_postulate)
