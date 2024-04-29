def is_success(old_belief_base, new_belief_base, new_belief):
    # new_belief_base = expand(old_belief_base, new_belief)
    # Expansion is success if the outcome contains the new_belief
    return new_belief_base.is_in_belief_base(new_belief)


def is_inclusion(old_belief_base, new_belief_base, new_belief):
    # new_belief_base = expand(old_belief_base, new_belief)
    # Inclusion is success if the new belief base contains the old belief base
    return old_belief_base.is_subset_of(new_belief_base)


def is_vacuity(old_belief_base, new_belief_base, new_belief):
    # if the incoming sentence is already in the set, there is no effect (old and new belief base are the same)
    # new_belief_base = expand(old_belief_base, new_belief)
    if old_belief_base.is_in_belief_base(new_belief):
        return new_belief_base.is_subset_of(old_belief_base) & old_belief_base.is_subset_of(new_belief_base)
    else:
        return True
