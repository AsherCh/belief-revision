from belief_base import *


def is_success(old_belief_base, new_belief, new_belief_base):
    # new_belief_base = contract(old_belief_base, new_belief)
    # Contraction is success if the outcome does not contain the new_belief
    return not new_belief_base.is_in_belief_base(new_belief)


def is_inclusion(old_belief_base, new_belief, new_belief_base):
    # new_belief_base = contract(old_belief_base, new_belief)
    # Inclusion is success if the old belief base contains the new belief base
    return new_belief_base.is_subset_of(old_belief_base)


def is_vacuity(old_belief_base, new_belief, new_belief_base):
    # new_belief_base = contract(old_belief_base, new_belief)
    if old_belief_base.is_in_belief_base(new_belief):
        return True
    else:
        # return true if the old and new belief base are the same
        return new_belief_base.is_subset_of(old_belief_base) & old_belief_base.is_subset_of(new_belief_base)


def is_extensionality(new_belief1, new_belief2):
    if new_belief1 == new_belief2:
        print("Extension is valid")
    else:
        print("not valid")
    return True
