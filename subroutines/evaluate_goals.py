# "Evaluate Goals"
# A Subroutine for the CARES Project
# Written by: Jesse Lawson
# Version: 2019.1


def evaluate_goals(agent):
    # Future Experiments: change goals based on energy. If energy > 50, goal == find_mate
    # self.goal = "find_mate" if self.energy >= 50 else "find_food"
    # Also: self.goal = "share_knowledge" (based on proximity to other organisms && self.energy)
    agent.goal = "find_food"