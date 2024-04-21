from sympy.logic.boolalg import Or, And

def entailment(clauses):
    while True:
            new_clauses = set()
            for clause1 in clauses:
                for clause2 in clauses:
                    resolvents = resolve(clause1, clause2)
                    for resolvent in resolvents:
                        if resolvent not in clauses and resolvent not in new_clauses:
                            new_clauses.add(resolvent)
            if new_clauses.issubset(set(clauses)):
                return False
            for c in new_clauses:
                clauses.append(c)

def resolve(c1, c2):
    clause1 = disjuncts(c1)
    clause2 = disjuncts(c2)
    resolvents = []
    for literal1 in clause1:
        for literal2 in clause2:
            if literal1 == ~literal2:
                resolvents = removeitem(literal1, clause1) + removeitem(literal2, clause2)
    return resolvents


def removeitem(item, seq):
    return [x for x in seq if x != item]

def disjuncts(clause):
    return dissociate(Or, [clause])

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
