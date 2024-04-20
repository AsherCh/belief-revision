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

        # resolve negation before ()
        self.resolve_negation()


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

                # if b has more than one character, it should go into ()
                # example: "a -> b & c" -> "a -> (b & c)" -> "~a | (b & c)"
                # & has priority over ->, priority should be kept when changing -> to |
                # if b is more than one character and has no brackets, add brackets
                # if first character of b is not "("
                # if b has any character from the set {"&", "|"}

                if len(b) > 1:
                    # iterate over a from right to left
                    bracket = 0
                    bracket_break = len(b)

                    for j, char in enumerate(b):
                        if bracket < 0:
                            bracket_break = j
                            break
                        if b[j] == "(":
                            bracket += 1
                        if b[j] == ")":
                            bracket -= 1
                    bracket_break -= 1
                    # save a before bracket_break and after bracket_break index into separate variables
                    b_before = b[:bracket_break]
                    b_after = b[bracket_break:]

                if ("&" in b_before or "|" in b_before) and (b_before[0] != "(" and b_before[-1] != ")"):
                    b_before = f"({b_before})"
                    b = f"{b_before}{b_after}"


                # if a has more than one character
                if len(a) > 1:
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

                    if (a_after[0] == "(" and a_after[-1] == ")") or len(a_after) == 1:
                        self.beliefs[i] = (priority, f"{a_before}~{a_after}|{b}")

                    # adding brakcets before and after a if there are any
                    # example: a = "p&q" -> "(p&q)"
                    # check if there are any ")" in a
                    else:
                        self.beliefs[i] = (priority, f"{a_before}~({a_after})|{b}")
                else:
                    self.beliefs[i] = (priority, f"~{a}|{b}")
                belief = self.beliefs[i][1]
        self.print_as_conjunction()

    def resolve_negation(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            if "~" in belief:
                # iterate from right to left
                for j in range(len(belief)-1, -1, -1):
                    if belief[j] == "~" and belief[j+1] == "(":
                        bracket = -1
                        bracket_break = -1
                        for k in range(j+2, len(belief)):
                            if bracket == 0:
                                bracket_break = k  #denotes the index where the inital "(" is closed ")"
                                break
                            if belief[k] == "(":
                                bracket -= 1
                            if belief[k] == ")":
                                bracket += 1
                        bracket_break -= 1
                        # save into to_negate string between j+2 and bracket_break
                        # this string should not include the beginning and ending brackets
                        # just j to skip the "~"
                        before_negate = belief[:j]
                        to_negate = belief[j+1:bracket_break+1]
                        # +1 to skip the ")"
                        after_negate = belief[bracket_break+1:]

                        # in to_negate, replace "&" with "|", and vice versa
                        to_negate = to_negate.replace("&", "temp")
                        to_negate = to_negate.replace("|", "&")
                        to_negate = to_negate.replace("temp", "|")
                        # check if character is a letter
                        # if it is, add "~" before it
                        negated = ""
                        for char in to_negate:
                            if char.isalpha():
                                negated += "~" + char
                            else:
                                negated += char

                        to_negate = negated

                        self.beliefs[i] = (priority, f"{before_negate}{to_negate}{after_negate}")
        self.print_as_conjunction()


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
