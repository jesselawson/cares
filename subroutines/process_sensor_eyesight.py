# "Process Sensor Eyesight"
# A Subroutine for the CARES Project
# Written by: Jesse Lawson
# Version: 2019.1
from Functions import *

def process_sensor_eyesight(agent):
    """Identifies neighborhood cells and stores them in an array."""
    log("- Processing eyesight sensors... ", False)
    # Look around us. What cells are there?
    x_pos = agent.cell.x
    y_pos = agent.cell.y

    # Cells around agent. Using immediate cells north, east, south, and west
    agent.neighborhood = [
        agent.system.cells[x_pos][y_pos-1] if y_pos > 0 else False,
        agent.system.cells[x_pos+1][y_pos] if x_pos < agent.system.width-1 else False,
        agent.system.cells[x_pos][y_pos+1] if y_pos < agent.system.height-1 else False,
        agent.system.cells[x_pos-1][y_pos] if x_pos > 0 else False
    ]

    log("[ OK ]")