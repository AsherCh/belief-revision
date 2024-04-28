from sympy.logic.boolalg import Or, And
from sympy.logic.boolalg import to_cnf

def entailment_consist(base):
    clauses = []
    for f in base:
        clauses += conjuncts(f)
    print(clauses)
    new_clauses = set()
    while True:
        for clause1 in clauses:
            for clause2 in clauses:
                resolvents = resolve(clause1, clause2)
                if False in resolvents:
                    return True
                for resolvent in resolvents:
                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.add(resolvent)
        if new_clauses.issubset(set(clauses)):
            return False
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
