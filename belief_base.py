import heapq
from sympy.logic.boolalg import to_cnf

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

    def belief_base_as_conjunction(self, belief_base):
        cnf = ""
        for i, (priority, belief) in enumerate(belief_base):
            if i == len(belief_base) - 1:
                # concatenate to cnf
                cnf += "(" + belief + ")"
            else:
                cnf += "(" + belief + ")&"
        return cnf

    def is_in_belief_base(self, expression):
        expression_cnf = to_cnf(expression, True)
        belief_base_cnf = to_cnf(self.belief_base_to_cnf_friendly(self.beliefs), True)
        # cast expression_cnf and belief_base_cnf to string
        expression_cnf = str(expression_cnf)
        belief_base_cnf = str(belief_base_cnf)
        # remove the character ' ' from the strings
        expression_cnf = expression_cnf.replace(" ", "")
        belief_base_cnf = belief_base_cnf.replace(" ", "")
        # split expression_cnf and belief_base_cnf to an array, separated by "&"
        expression_cnf_split = expression_cnf.split("&")
        belief_base_cnf_split = belief_base_cnf.split("&")
        # loop through the expression_cnf_split
        for exp in expression_cnf_split:
            # check if the expression is in belief_base_cnf_split
            if exp not in belief_base_cnf_split:
                return False
        return True

    def get_last_priority(self):
        return self.beliefs[-1][0]

    def belief_base_to_cnf_friendly(self, belief_base):
        to_convert = belief_base

        # replace bi-implication with conjunction of implications
        to_convert = self.replace_bi_implication(to_convert)

        # replace implication with disjunction
        to_convert = self.replace_implication(to_convert)

        return self.belief_base_as_conjunction(to_convert)

        # # resolve negation before ()
        # self.resolve_negation()
        #
        # # remove redundant brackets in the beginning and end
        # self.remove_brackets()
        #
        # # split beliefs with conjunctions into two beliefs
        # self.split_conjunctions()
        #
        # # apply associative law (a | (b | c)) -> ((a | b) | c) -> (a | b | c)
        # self.apply_associative_law()
        #
        # # apply distributive law (a | (b & c)) -> ((a | b) & (a | c))
        # self.apply_distributive_law()

    def replace_bi_implication(self, belief_base):
        for i, (priority, belief) in enumerate(belief_base):
            if "<->" in belief:
                # split bi-implication into two implications
                a, b = belief.split("<->")
                belief_base[i] = (priority, f"({a}->{b})&({b}->{a})")
        return belief_base

    def replace_implication(self, belief_base):
        for i, (priority, belief) in enumerate(belief_base):
            # replace "->" with ">>"
            belief_base[i] = (priority, belief.replace("->", ">>"))

        return belief_base

    # def replace_implication(self, belief_base):
    #     for i, (priority, belief) in enumerate(belief_base):
    #         # while there is "->" in belief, replace by disjunction
    #
    #         while "->" in belief:
    #             # split implication into two parts, finding the first occurrence of "->"
    #             a, b = belief.split("->", 1)
    #
    #             # if b has more than one character, it should go into ()
    #             # example: "a -> b & c" -> "a -> (b & c)" -> "~a | (b & c)"
    #             # & has priority over ->, priority should be kept when changing -> to |
    #             # if b is more than one character and has no brackets, add brackets
    #             # if first character of b is not "("
    #             # if b has any character from the set {"&", "|"}
    #
    #             if len(b) > 1:
    #                 # iterate over a from right to left
    #                 bracket = 0
    #                 bracket_break = len(b)
    #
    #                 for j, char in enumerate(b):
    #                     if bracket < 0:
    #                         bracket_break = j
    #                         break
    #                     if b[j] == "(":
    #                         bracket += 1
    #                     if b[j] == ")":
    #                         bracket -= 1
    #                 bracket_break -= 1
    #                 # save a before bracket_break and after bracket_break index into separate variables
    #                 b_before = b[:bracket_break]
    #                 b_after = b[bracket_break:]
    #
    #             if ("&" in b_before or "|" in b_before) and (b_before[0] != "(" and b_before[-1] != ")"):
    #                 b_before = f"({b_before})"
    #                 b = f"{b_before}{b_after}"
    #
    #
    #             # if a has more than one character
    #             if len(a) > 1:
    #                 # iterate over a from right to left
    #                 bracket = 0
    #                 bracket_break = -1
    #                 for j in range(len(a)-1, -1, -1):
    #                     if bracket < 0:
    #                         bracket_break = j
    #                         break
    #                     if a[j] == "(":
    #                         bracket -= 1
    #                     if a[j] == ")":
    #                         bracket += 1
    #                 bracket_break += 2
    #                 # save a before bracket_break and after bracket_break index into separate variables
    #                 a_before = a[:bracket_break]
    #                 a_after = a[bracket_break:]
    #
    #                 if (a_after[0] == "(" and a_after[-1] == ")") or len(a_after) == 1:
    #                     belief_base[i] = (priority, f"{a_before}~{a_after}|{b}")
    #
    #                 # adding brakcets before and after a if there are any
    #                 # example: a = "p&q" -> "(p&q)"
    #                 # check if there are any ")" in a
    #                 else:
    #                     belief_base[i] = (priority, f"{a_before}~({a_after})|{b}")
    #             else:
    #                 belief_base[i] = (priority, f"~{a}|{b}")
    #             belief = belief_base[i][1]
    #     return belief_base

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

    def remove_brackets(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            valid = True
            while belief[0] == "(" and belief[-1] == ")" and valid:
                # remove brackets from the beginning and end
                belief = belief[1:-1]
                # check for validity
                # iterate over belief, if at any point there are more ) than (, set valid to False
                bracket = 0
                for char in belief:
                    if bracket < 0:
                        valid = False
                        # put the brackets back
                        belief = f"({belief})"
                        break
                    if char == "(":
                        bracket += 1
                    if char == ")":
                        bracket -= 1
            self.beliefs[i] = (priority, belief)
        self.print_as_conjunction()

    def remove_brackets_from_string(self, belief):
        valid = True
        while belief[0] == "(" and belief[-1] == ")" and valid:
            # remove brackets from the beginning and end
            belief = belief[1:-1]
            # check for validity
            # iterate over belief, if at any point there are more ) than (, set valid to False
            bracket = 0
            for char in belief:
                if bracket < 0:
                    valid = False
                    # put the brackets back
                    belief = f"({belief})"
                    break
                if char == "(":
                    bracket += 1
                if char == ")":
                    bracket -= 1
        return belief

    def split_conjunctions(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            if "&" in belief:
                # iterate over belief
                should_iterate = True
                # if any & gets replaced by *, iterate again from the beginning after running through the whole belief
                # ex. ((p|q)&r)&(p|q) -> ((p|q)&r)*(p|q)
                while(should_iterate):
                    should_iterate = False
                    for (index, char) in enumerate(belief):
                        if char == "&":
                            # split belief into two beliefs
                            a, b = belief.split("&", 1)
                            # if "a" includes character "*" then cut a only to the last "*"
                            if "*" in a:
                                a = a.rsplit("*", 1)[-1]
                            if "*" in b:
                                b = b.split("*", 1)[0]
                            # count the number of brackets before and after the "&" (until the potential *)
                            a = self.remove_brackets_from_string(a)
                            b = self.remove_brackets_from_string(b)
                            if a.count("(") - a.count(")") == 0 and b.count("(") - b.count(")") == 0:
                                belief = self.replace_char_at_index(belief, index, "*")  # replace & at index by *
                                should_iterate = True
            # in every cell, if there is a "*"
            # split the cell there and add the two new beliefs to the list and remove the old one
            while "*" in belief:
                a, b = belief.split("*", -1)
                self.beliefs[i] = (priority, a)
                self.beliefs.append((priority, b))
                belief = a

    def replace_char_at_index(self, org_str, index, replacement):
        new_str = org_str[:index] + replacement + org_str[index + 1:]
        return new_str

    def apply_associative_law(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            if "|" in belief and "&" not in belief:
                # remove all brackets from belief
                belief = belief.replace("(", "")
                belief = belief.replace(")", "")
                self.beliefs[i] = (priority, belief)
        self.print_as_conjunction()

    def apply_distributive_law(self):
        for i, (priority, belief) in enumerate(self.beliefs):
            if "|" in belief and "&" in belief:
                # iterate over belief
                should_iterate = True
                # if any & gets replaced by *, iterate again from the beginning after running through the whole belief
                # ex. ((p|q)&r)&(p|q) -> ((p|q)&r)*(p|q)
                while(should_iterate):
                    should_iterate = False
                    for (index, char) in enumerate(belief):
                        if char == "|":
                            # split belief into two beliefs
                            a, b = belief.split("|", 1)
                            # if "a" includes character "*" then cut a only to the last "*"
                            if "*" in a:
                                a = a.rsplit("*", 1)[-1]
                            if "*" in b:
                                b = b.split("*", 1)[0]
                            # count the number of brackets before and after the "&" (until the potential *)
                            a = self.remove_brackets_from_string(a)
                            b = self.remove_brackets_from_string(b)
                            if a.count("(") - a.count(")") == 0 and b.count("(") - b.count(")") == 0:
                                belief = self.replace_char_at_index(belief, index, "*")

# Example usage:
# bbp = BeliefBasePriority()
# # bbp.add_belief("p", priority=2)
# # bbp.add_belief("q", priority=1)
# bbp.add_belief("p->q", priority=3)
# bbp.add_belief("p<->q", priority=2)
# bbp.add_belief("p&r<->q", priority=2)
# bbp.add_belief("(p&r)<->q", priority=2)
#
# bbp.to_cnf()
#
# #print("Querying belief 'p':", bbp.query_belief("p"))
# #print("Querying belief 'p->q':", bbp.query_belief("p->q"))
# #bbp.remove_belief("q")
# #bbp.to_cnf()
