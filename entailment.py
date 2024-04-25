import sys
from sympy.logic.boolalg import Or, And
from sympy.logic.boolalg import to_cnf
"""
1. First, KB ∧ ¬ϕ is converted into CNF.
2. Then, the resolution rule is applied to the resulting clauses.
3. Each pair that contains complementary literals is resolved to produce a
new clause, which is added to the set if it is not already present.
	The process continues until one of two things happens:
    a there are no new clauses that can be added, in which case KB does not
    entail ϕ; or,
    b two clauses resolve to yield the empty clause, in which case KB entails ϕ
"""
def entailment(base,new_belief):
    clauses = []
    ## Generate a set of clauses and remove "&"
    for f in base:
        clauses += conjuncts(f)
    print("clauses:",clauses)
    ## Add the negative new belief to clauses
    clauses += conjuncts(to_cnf(~new_belief))
    print("clauses+(~new_belief):",clauses)
    new_clauses = set()
    while True:
        for clause1 in clauses:
            for clause2 in clauses:
                ## Eash of the clauses is paired with each of the rest clauses, and the resolution rule is applied to yield the clauses
                resolvents = resolve(clause1, clause2)
                ## If resolvents contains the empty clause, so belief_base can entail new_belief
                if False in resolvents:
                    return True
                ## Generated resolvents will be added to new clauses list
                for resolvent in resolvents:
                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.add(resolvent)
        ## No any new clauses generated,  reture False to exist the loop, so belief_base doesn't entail new_belief
        if new_clauses.issubset(set(clauses)):
            return False
        ##Fine the new clauses and add into clauses list
        for c in new_clauses:
            clauses.append(c)

#Resolution-based
def resolve(c1, c2):
    clauses = []
    ## Remove "|" from each clauses
    clause1 = disjuncts(c1)
    clause2 = disjuncts(c2)
    resolvents = []
    for literal1 in clause1:
        for literal2 in clause2:
            ## if p == ~(~p)
            if literal1 == ~literal2:
                ## Remove the p from the clause1 and remove ~p from the clause2
                resolvents = removeitem(literal1, clause1) + removeitem(literal2, clause2)
                ## generate the new clause
                new_clause = associate(Or, resolvents)
                clauses.append(new_clause)
    return clauses


def removeitem(item, seq):
    return [x for x in seq if x != item]

# convert q | ~p to  [q, ~p] 
def disjuncts(clause):
    return dissociate(Or, [clause])
# convert (q | ~p) & (r | ~p) to [q | ~p, r | ~p]
def conjuncts(clause):
    return dissociate(And, [clause])

def associate(op, args):
    args = dissociate(op, args)
    if len(args) == 0:
        return op.identity
    elif len(args) == 1:
        return args[0]
    else:
        return op(*args)

def dissociate(op, args):
    result = []
    def collect(subargs):
        for arg in subargs:
            if isinstance(arg, op):
                collect(arg.args)
            else:
                result.append(arg)

    collect(args)
    return result
