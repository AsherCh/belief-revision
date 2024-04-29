import heapq
from sympy.logic.boolalg import to_cnf

class BeliefBasePriority:
    def __init__(self):
        self.beliefs = []
        #self.neo_beliefs = [] #used to store beliefs after Contraction 

    def add_belief(self, belief, priority):
        heapq.heappush(self.beliefs, (priority, belief))

    def add_neo_belief(self, belief, priority):      #to add the remainaing beliefs after Contraction version 1
        heapq.heappush(self.neo_beliefs, (priority, belief))

    def find_Contracting_belief(self, belief, contract_belief):     # Version 1 of Contraction, which creates a new belief base after contraction
        for priority,  belief in self.beliefs:
            if belief.is_in_belief_base(contract_belief):
                print(f"The belief {contract_belief} is contracted from the belief base")
            else:
                belief.add_neo_belief(self, belief, priority)
                pass
        return belief

    def V2_find_Contracting_belief(self, belief, new_belief):   # Version 2 of COntraction, which removes the contracting belief and returns the modified belief base
        if self.is_in_belief_base(new_belief):
            new_belief = self.string_to_cnf_friendly(new_belief)   #to make the new string cnf frinedly
            self.remove_belief(new_belief)
            print(f"The belief {new_belief} is contracted from the belief base")
        else:
            pass
        return belief      

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

    def print_Neo_beliefs(self,contract_belief):
        print("Belief Base after Contraction of ",contract_belief)
        for priority,  belief in self.neo_beliefs:
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
        expression_cnf = to_cnf(self.string_to_cnf_friendly(expression), True)
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
            if exp not in belief_base_cnf_split and "(" + exp + ")" not in belief_base_cnf_split:
                return False
        return True

    def get_last_priority(self):
        return self.beliefs[-1][0]

    def belief_base_to_cnf_friendly(self, belief_base):
        to_convert = belief_base

        # replace bi-implication with conjunction of implications
        to_convert = self.replace_bi_implication(to_convert)

        # replace implication
        to_convert = self.replace_implication(to_convert)

        return self.belief_base_as_conjunction(to_convert)

    def string_to_cnf_friendly(self, belief):
        belief = self.string_replace_bi_implication(belief)
        belief = belief.replace("->", ">>")
        return belief

    def is_subset_of(self, another_belief_base):
        # for each belief in self.beliefs, check if it is in another_belief_base
        for _, belief in self.beliefs:
            if not another_belief_base.is_in_belief_base(belief):
                return False
        return True

    def replace_bi_implication(self, belief_base):
        for i, (priority, belief) in enumerate(belief_base):
            belief_base[i] = (priority, self.string_replace_bi_implication(belief))
        return belief_base

    def string_replace_bi_implication(self, belief):
        if "<->" in belief:
            # replace first occurrence of "<->" with "->"
            belief1 = belief.replace("<->", ">>", 1)
            belief2 = belief.replace("<->", "<<", 1)
            return "(" + self.string_replace_bi_implication(belief1) + ")&(" + self.string_replace_bi_implication(belief2) + ")"
        else:
            return belief

    def replace_implication(self, belief_base):
        for i, (priority, belief) in enumerate(belief_base):
            # replace "->" with ">>"
            belief_base[i] = (priority, belief.replace("->", ">>"))

        return belief_base

