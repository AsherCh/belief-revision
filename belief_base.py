import heapq

class BeliefBasePriority:
    def __init__(self):
        self.beliefs = []

    def add_belief(self, belief, priority):
        heapq.heappush(self.beliefs, (priority, belief))

    def remove_belief(self, belief):
        for i, (p, b) in enumerate(self.beliefs):
            if b == belief:
                del self.beliefs[i]
                heapq.heapify(self.beliefs)
                return
        print("Belief not found in the belief base.")

    def query_belief(self, belief):
        for p, b in self.beliefs:
            if b == belief:
                return True
        return False

    def print_beliefs(self):
        print("Belief Base with Priority Order:")
        for priority,  belief in self.beliefs:
            print(f"- Priority {priority}: {belief}")

    def to_cnf(self):
        print("Belief Base in CNF:")
        self.print_as_conjunction()

        # replace bi-implication with conjunction of implications
        self.replace_bi_implication()

        # replace implication with disjunction
        self.replace_implication()


    def print_as_conjunction(self):
        cnf = ""
        for i, (priority, belief) in enumerate(self.beliefs):
            if i == len(self.beliefs) - 1:
                # concatenate to cnf
                cnf += "(" + belief + ")"
            else:
                cnf += "(" + belief + ")&"
        print(cnf)

    def replace_bi_implication(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            if "<->" in belief:
                # split bi-implication into two implications
                a, b = belief.split("<->")
                self.beliefs[i] = (priority, f"({a}->{b})&({b}->{a})")
        self.print_as_conjunction()

    def replace_implication(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            # while there is "->" in belief, replace by disjunction

            while "->" in belief:
                # split implication into two parts, finding the first occurrence of "->"
                a, b = belief.split("->", 1)

                # if a has more than one character
                if len(a) > 1:
                    # adding brakcets before and after a if there are any
                    # example: a = "p&q" -> "(p&q)"
                    # check if there are any ")" in a
                    if not ")" in a:
                        a = f"({a})"

                    # iterate over a from right to left
                    bracket = 0
                    bracket_break = -1
                    for j in range(len(a)-1, -1, -1):
                        if bracket < 0:
                            bracket_break = j
                            break
                        if a[j] == "(":
                            bracket -= 1
                        if a[j] == ")":
                            bracket += 1
                    bracket_break += 2
                    # save a before bracket_break and after bracket_break index into separate variables
                    a_before = a[:bracket_break]
                    a_after = a[bracket_break:]
                    self.beliefs[i] = (priority, f"{a_before}~{a_after}|{b}")
                else:
                    self.beliefs[i] = (priority, f"~{a}|{b}")
                belief = self.beliefs[i][1]
        self.print_as_conjunction()

    def count_parentheses(self, belief):
        # return 0 if the same number of opening and closing parentheses
        # return < 0 if more closing parentheses than opening parentheses
        # return > 0 if more opening parentheses than closing parentheses
        return belief.count("(") - belief.count(")")



# Example usage:
bbp = BeliefBasePriority()
# bbp.add_belief("p", priority=2)
# bbp.add_belief("q", priority=1)
bbp.add_belief("p->q", priority=3)
bbp.add_belief("p<->q", priority=2)
bbp.add_belief("p&r<->q", priority=2)
bbp.add_belief("(p&r)<->q", priority=2)

bbp.to_cnf()

#print("Querying belief 'p':", bbp.query_belief("p"))
#print("Querying belief 'p->q':", bbp.query_belief("p->q"))
#bbp.remove_belief("q")
#bbp.to_cnf()
