# Functions common to all research experiments

class Cell:
    def __init__(self):
        self.occupant = None # Who is on the cell



class Grid:
    def __init__(self, width_height):
        self.width = width_height
        self.height = width_height
        self.cells = {}
        a = 0
        while a < width_height*width_height:
            row = 0

            self.cells[row][a] = Cell()

