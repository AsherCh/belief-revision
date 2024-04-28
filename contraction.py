from sympy.logic.boolalg import Or, And, Implies
from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable
from sympy.abc import Q, P, R, C, A, B, D, i



def contract(belief_base, new_belief):

    if belief_base.AGM_postulate_consistency.is_consistent(belief_base):
    # check if the new_belief is already in the belief base
        if belief_base.is_in_belief_base(new_belief):
        
            #belief_base.find_Contracting_belief(belief_base,new_belief)   #version 1 creates a new belief base after contraction
            #belief_base.print_Neo_beliefs(belief_base,new_belief)         #To print results after version 1 contraction
            belief_base.V2_find_Contracting_belief(belief_base,new_belief) #version 2 updates exisitng belief base after contraction

        else:
            # else, return the base as it is.
            belief_base.AGM_postulates_contraction.is_vacuity(belief_base,new_belief)
            print("The Belief to Contract is not found in Belief Base, Vacuity Postulate Satisfied")
            pass
        return belief_base
    else:
        print("The belief base is inconsistent")
        return



"""
# trail and error to figure how to make it work :(

A = ((P>>~Q) & (Q>>R))
B = (~(P|Q)|R)
C = (P>>(Q & R))
D = (P>>Q)
E = (~P)
G = D & E
#F=[]
#que = to_cnf(P)
F.extend([A,B,C])
#print("Regular",F)
#f6 = to_cnf((P>>Q),(~(P | Q) | R))
#f1=to_cnf(P>>Q)

#f5=to_cnf(~(P | Q) | R)
#f2=to_cnf("q")
#f3=to_cnf("p>>q")
#f4=to_cnf(P>>(Q & R))
#imp = Implies(f1,que)
#answer = not satisfiable(imp)
#is_subset = all(not satisfiable(imp.subs(model)) for model in f1.iter_models())

#print(answer)
#print(to_cnf(G))
#print(to_cnf(F[0]))

#print("next",f6)
#print (to_cnf(A))
#print (f5)
#print (f5 & f4)  # to verify
#print(f1)
#print(f4)
contract_belief = Q
CB= to_cnf(contract_belief)
bc = None
#for i in F:
  #  bc=to_cnf(i)
   # print("cnf of ind0",bc)
    #if CB in bc:
        #i='*'+i
     #   print("this is i",i)
     #   exit
   # exit

A=P>>Q
B = Q
C = A & B
f1=to_cnf(((P & Q) | R) & ((~Q | R) & P)) 
print("f1=",f1)
que = to_cnf(R & Q)
impli = f1>>que

print("que:",que)
#print("C=", to_cnf(C)) # cnf of C = A&B
print("check imp:", to_cnf(impli)) # cnf of beliefs implication
imp = Implies(f1,que)
print("Implies:",imp) #op of implies fn
print("cnf_implies", to_cnf(imp))
bonser = satisfiable(imp) 
print("satisfyable",bonser)
answer = not satisfiable(imp)
print("not satisfy",answer)
"""
