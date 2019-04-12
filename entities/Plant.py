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

class Plant:
    def __init__(self, img_id, id, color, size, has_berries, is_leafy, is_edible):
        self.img_id = img_id
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
            return random.randint(1, 20)
        else:
            return -1*random.randint(1, 20)


plants = [
    Plant(1, "Tuna Bush", "red", "large", True, False, False),
    Plant(2, "Salmon Bush", "green", "medium", False, False, True),
    Plant(3, "Oreo Bush", "red", "large", True, True, True),
    Plant(4, "Leafy Fish Plant", "yellow", "medium", False, False, False),
    Plant(5, "Coffee Vine", "yellow", "small", True, False, True)
]