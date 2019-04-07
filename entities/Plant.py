from Project import *

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