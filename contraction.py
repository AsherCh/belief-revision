from sympy.logic.boolalg import Or, And, Implies
from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable
from sympy.abc import Q, P, R, C, A, B, D, i
from belief_base import *
from AGM_postulate_consistency import *
from AGM_postulates_contraction import *



def contract(belief_base, new_belief):
    #print("COnsistency checK",is_consistent(belief_base))  #consistency check, not working rn
    if belief_base.is_in_belief_base(new_belief):
    
        #belief_base.find_Contracting_belief(belief_base,new_belief)   #version 1 creates a new belief base after contraction
        #belief_base.print_Neo_beliefs(belief_base,new_belief)         #To print results after version 1 contraction
        belief_base.V2_find_Contracting_belief(belief_base,new_belief) #version 2 updates exisitng belief base after contraction

    else:
        # else, return the base as it is.
        #is_vacuity(belief_base,new_belief)  #AGM postulate check
        print("The Belief to Contract is not found in Belief Base")
        pass
    return belief_base
