class BeliefBase:
    def __init__(self):
        self.beliefs = []

    def add_belief(self, belief):
        self.beliefs.append(belief)

    def remove_belief(self, belief):
        if belief in self.beliefs:
            self.beliefs.remove(belief)
        else:
            print("Belief not found in the belief base.")

    def query_belief(self, belief):
        return belief in self.beliefs

    def print_beliefs(self):
        print("Belief Base:")
        for belief in self.beliefs:
            print("-", belief)

