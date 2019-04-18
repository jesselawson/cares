#  Cellular Agent Research Experiment System (CARES)
#  Copyright (c) 2019 Jesse Lawson
#
#  Web: https://jesselawson.org
#  Email: jesselawson@protonmail.com
#  Telegram: t.me/jesselawson
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
