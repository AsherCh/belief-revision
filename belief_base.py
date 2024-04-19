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


# Example usage:
bbp = BeliefBasePriority()
bbp.add_belief("p", priority=2)
bbp.add_belief("q", priority=1)
bbp.add_belief("p->q", priority=3)
bbp.add_belief("p<->q", priority=2)

bbp.print_beliefs()

print("Querying belief 'p':", bbp.query_belief("p"))
print("Querying belief 'p->q':", bbp.query_belief("p->q"))

bbp.remove_belief("q")
bbp.print_beliefs()
