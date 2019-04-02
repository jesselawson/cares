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
    Plant("Tuna Bush", "red", "large", True, False, False),
    Plant("Salmon Bush", "green", "medium", False, False, True),
    Plant("Oreo Bush", "red", "large", True, True, True),
    Plant("Leafy Fish Plant", "yellow", "medium", False, False, False),
    Plant("Coffee Vine", "yellow", "small", True, False, True),
    Plant("Burrito Bush", "green", "small", False, True, False)
]


class Cell:
    def __init__(self, x, y, has_plant = False):
        self.occupying_agent = None
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
    def __init__(self, starting_cell):
        self.energy = 10
        self.age = 1
        self.goal = "find_food" # find_food, Future: find_shelter, find_mate, etc
        """Agent.intent is a string that tells the System (during update) what it should do about this agent?"""
        self.intent = "start"
        self.cell = starting_cell #if starting_cell is not None else False
        self.system = None

    def evaluate_goals(self):
        # Future Experiments: change goals based on energy. If energy > 50, goal == find_mate
        # self.goal = "find_mate" if self.energy >= 50 else "find_food"
        # Also: self.goal = "share_knowledge" (based on proximity to other organisms && self.energy)
        self.goal = "find_food"

    def update(self, system):
        """Update this agent, given a pointer to the system in which it exists."""

        # System is a reference to the System where this Agent exists

        # Look around us. What cells are there?
        x_pos = self.cell.x
        y_pos = self.cell.y

        # Cells around agent
        cell_north = system.cells[x_pos][y_pos-1] if y_pos > 0 else False
        cell_east = system.cells[x_pos+1][y_pos] if x_pos < system.width else False
        cell_south = system.cells[x_pos][y_pos+1] if x_pos < system.height else False
        cell_west = system.cells[x_pos-1][y_pos] if x_pos > 0 else False

        self.evaluate_goals()

        if self.goal == "find_food":
            # Check if we are on a plant cell. If yes, determine if we should eat it.
            if self.cell.has_plant:
                print("There's food here!")
                # There's a plant here. Should we eat it?
                # Step 1. "Observe" plant (take in characteristics & add to plants_encountered (the training data)
                # Step 2. "Ponder" (train model based on all plants ever encountered / re-train model)
                # Step 3. "Decide" (make a prediction)
                # Step 4. "Act" (If prediction = edible, eat plant. Otherwise, move to a new cell.

            # Check if any cell around us has a plant.
            # If none have plants, choose a random direction and move there.







class System:
    def __init__(self, width_height, num_starting_agents, num_starting_plants, max_system_steps=False, quiet=False):
        self.width = width_height
        self.height = width_height
        self.cells = [[None for x in range(width_height)] for y in range(width_height)]
        self.agents = []
        self.num_starting_agents = num_starting_agents
        self.quiet = quiet
        self.max_system_steps = max_system_steps
        # TODO: num_starting_agents should be customizable
        self.max_active_plants = num_starting_agents*2
        # Populate cells
        for x in range(0, width_height):
            for y in range(0, width_height):
                self.cells[x][y] = Cell(x, y)


        self.elapsed_time = 0

        # Grow random plants
        for x in range(num_starting_plants):
            planted = False
            while not planted:
                random_x = random.randint(0, width_height - 1)
                random_y = random.randint(0, width_height - 1)

                if not self.cells[random_x][random_y].has_plant:
                    planted = True
                    self.cells[random_x][random_y].grow_plant()

        # Populate system with starting agents
        for i in range(0, self.num_starting_agents):
            if not quiet:
                print("> Building agent %d..." % i)
            cell_is_open = False
            while not cell_is_open:

                random_x = random.randint(0, width_height-1)
                random_y = random.randint(0, width_height-1)

                if not quiet:
                    print("-> Trying to put agent at {%s, %s}..." % (random_x, random_y))
                if not self.cells[random_x][random_y].occupying_agent:
                    this_agent = Agent(self.cells[random_x][random_y])
                    self.agents.append(this_agent)
                    self.cells[random_x][random_y].occupying_agent = self.agents[-1] # Get most recently appended agent
                    cell_is_open = True
                    if not quiet:
                        print("- -> Looks good!")
                else:
                    if not quiet:
                        print("- -> Already occupied!")

    def num_active_plants(self):
        num_plants = 0
        for x in range(0, self.width):
            for y in range(0, self.height):
                num_plants += 1 if self.cells[x][y].has_plant else 0
        return num_plants

    def step_time(self):
        """Run through all agents and have them create an action and commit to an action."""

        self.elapsed_time += 1
        if not self.quiet:
            print("A new day has begun! It's been %s days since this universe began." % (self.elapsed_time))

        self.update_system()
        if self.elapsed_time < self.max_system_steps:
            self.step_time()

    def update_system(self):
        # Update any occupying agents
        for x in range(0, self.width):
            for y in range(0, self.height):
                """TODO: Cell.update() (which includes check for occupying agent, and then updates that agent accordingly)"""
                print("[Day #%s] Updating cell %s %s..." % (self.elapsed_time, x, y))

                # Is this cell occupied?
                if self.cells[x][y].occupying_agent:
                    # Call any agent updating that needs to happen
                    agent = self.cells[x][y].occupying_agent
                    agent.update(self)

        # Update any plants, if necessary
        for x in range(1, self.max_active_plants - self.num_active_plants()):
            self.cells[x][y].grow_plant()

        # TODO: MOdify the below to merge with the above block so the plants
        # are populating at random places
        for x in range(num_starting_plants):
            planted = False
            while not planted:
                random_x = random.randint(0, width_height - 1)
                random_y = random.randint(0, width_height - 1)

                if not self.cells[random_x][random_y].has_plant:
                    planted = True
                    self.cells[random_x][random_y].grow_plant()






    def print_step(self):

        # Print the plants
        for x in range(0, self.width):
            for y in range(0, self.height):
                has_plant = "does not have a plant"
                if self.cells[x][y].has_plant:
                    plant_type = self.cells[x][y].plant.id
                    has_plant = "has a %s plant" % plant_type
                    if not self.quiet:
                        print("Cell at %s %s %s" % (self.cells[x][y].x, self.cells[x][y].y, has_plant))

        # Print the agents
        for i in self.agents:
            pos_x = i.cell.x
            pos_y = i.cell.y
            if not self.quiet:
                print("Agent @ %s %s" % (pos_x, pos_y))
