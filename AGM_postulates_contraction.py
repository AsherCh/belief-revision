def is_success(old_belief_base, new_belief):
    new_belief_base = old_belief_base.contract(new_belief)
    # Contraction is success if the outcome does not contain the new_belief
    return not new_belief_base.is_in_belief_base(new_belief)


def is_inclusion(old_belief_base, new_belief):
    new_belief_base = old_belief_base.contract(new_belief)
    # Inclusion is success if the old belief base contains the new belief base
    return new_belief_base.is_subset_of(old_belief_base)


def is_vacuity(old_belief_base, new_belief):
    new_belief_base = old_belief_base.contract(new_belief)
    if old_belief_base.is_in_belief_base(new_belief):
        return True
    else:
        # return true if the old and new belief base are the same
        return new_belief_base.is_subset_of(old_belief_base) & old_belief_base.is_subset_of(new_belief_base)


def is_extensionality(new_belief1, new_belief2, old_belief_base):
    if new_belief1.is_in_belief_base(new_belief2) and new_belief2.is_in_belief_base(new_belief1):
        new_belief_base1 = old_belief_base.contract(new_belief1)
        new_belief_base2 = old_belief_base.contract(new_belief2)
        return new_belief_base1.is_subset_of(new_belief_base2) & new_belief_base2.is_subset_of(new_belief_base1)
    return True
