# Functions common to all research experiments

import random

class Plant:
    def __init__(self, id, color, size, has_berries, is_leafy, is_edible):
        self.id = id
        self.color = color
        self.size = size
        self.has_berries = has_berries
        self.is_leafy = is_leafy
        self.is_edible = is_edible

    def consume(self):
        """Consume the plant. If this returns a positive number,
        this plant is edible. If negative, this plant is poison.
        """
        if self.is_edible:
            return random.randint(1,20)
        else:
            return -1*random.randint(1,20)


plants = [
    Plant("plant001", "red", "large", True, False, False),
    Plant("plant002", "green", "medium", False, False, True),
    Plant("plant003", "red", "large", True, True, True),
    Plant("plant004", "yellow", "medium", False, False, False),
    Plant("plant005", "yellow", "small", True, False, True),
    Plant("plant006", "green", "small", False, True, False)
]


class Cell:
    def __init__(self, x, y, has_plant = False):
        self.occupant = None
        self.has_plant = has_plant
        self.plant = None
        self.x = x
        self.y = y
        if has_plant:
            self.grow_plant()

    def consume_plant(self):
        if self.has_plant:
            energy = self.plant.consume()
            self.plant = None
            self.has_plant = False
            return energy

    def grow_plant(self):
        if not self.has_plant:
            self.has_plant = True
        self.plant = plants[random.randint(0, len(plants)-1)]


class Agent:
    """An autonomous agent of the system.

    The lifecycle of the agent is as follows:
    While energy > 0 and age < 100:
        1. Evaluate our goal, based on our current conditions (energy, age)
        2. Given our goal, check our current tile. If it has a plant, decide whether to eat it or not.
        2.b. If we decide to eat it, remember whether it was edible or poison. check all tiles around us for a tile that contains
           something that will bring us closer to that goal.
        3.
    """
    def __init__(self):
        self.energy = 10
        self.age = 1
        self.goal = "find_food"
        self.cell = None

    def evaluate_goals(self):
        # Future Experiments: change goals based on energy. If energy > 50, goal == find_mate
        # self.goal = "find_mate" if self.energy >= 50 else "find_food"
        # Also: self.goal = "share_knowledge" (based on proximity to other organisms && self.energy)
        self.goal = "find_food"

    def update(self, the_cell):
        """Given the_cell, update this agent."""
        self.cell = the_cell
        self.evaluate_goals()





class System:
    def __init__(self, width_height, num_starting_agents, num_starting_plants):
        self.width = width_height
        self.height = width_height
        self.cells = [[None for x in range(width_height)] for y in range(width_height)]

        # Populate cells
        for x in range(0, width_height):
            for y in range(0, width_height):
                self.cells[x][y] = Cell(x, y)


        self.elapsed_time = 0

        # Populate system with starting agents
        self.agents = [Agent() for x in range(num_starting_agents)]

        # Grow random plants
        for x in range(num_starting_plants):
            self.cells[random.randint(0, width_height-1)][random.randint(0, width_height-1)].grow_plant()

    def step_time(self):
        """Run through all agents and have them create an action and commit to an action."""
        self.elapsed_time += 1

    def print_step(self):

        for x in range(0, self.width):
            for y in range(0, self.height):
                has_plant = "does not have a plant"
                if self.cells[x][y].has_plant:
                    plant_type = self.cells[x][y].plant.id
                    has_plant = "has a %s plant" % plant_type
                    print("Cell at %s %s %s" % (self.cells[x][y].x, self.cells[x][y].y, has_plant))

