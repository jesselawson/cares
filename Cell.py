import random
from entities.Plant import *

class Cell:
    def __init__(self, x, y, has_plant = False):
        self.occupying_agent = None
        self.has_plant = has_plant
        self.plant = None
        self.x = x
        self.y = y
        if has_plant:
            self.grow_plant()

    def get_map_coords(self):
        """Returns the [x,y] of where this cell is represented on the snapshot map."""
        map_x = self.x * 8
        map_y = self.y * 8
        return [map_x, map_y]

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
