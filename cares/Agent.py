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
from cares.Functions import *


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
    def __init__(self, model, agent_id, system, starting_cell):
        self.agent_id = agent_id
        # TODO: Dynamically set set starting energy
        self.energy = 20
        self.age = 1
        self.goal = "find_food" # find_food, Future: find_shelter, find_mate, etc
        """Agent.intent is a string that tells the System (during update) what it should do about this agent?"""
        self.intent = "start"
        self.cell = starting_cell #if starting_cell is not None else False
        self.system = system
        self.model = model
        # Keep track of whether this agent has been marked as "end of turn".
        # This is a hard stop we can employ mid-subroutine, if necessary.
        self.alive = True

        self.neighborhood = []  # process_sensor_eyesight

    def update(self):
        """Update this agent, given a pointer to the system in which it exists."""
        log("+ Agent #%02d Starting Energy: %03d" % (self.agent_id, self.energy))

        # Execute all subroutines
        for subroutine in self.model.get_subroutines():
            subroutine.__call__(self)

        # System is a reference to the System where this Agent exists



        # TODO: How to intergrate subroutines into the below "decision complete?"
        # In other words, how do we convert this into a subroutine?
        if self.goal == "find_food":
            decision_complete = False
            # Check if we are on a plant cell. If yes, determine if we should eat it.
            if self.cell.has_plant:
                log("- has found a plant ", False)
                # TODO: exp2 below:
                # There's a plant here. Should we eat it?
                # Step 1. "Observe" plant (take in characteristics & add to plants_encountered (the training data)
                # Step 2. "Ponder" (train model based on all plants ever encountered / re-train model)
                # Step 3. "Decide" (make a prediction)
                # Step 4. "Act" (If prediction = edible, eat plant. Otherwise, move to a new cell.

                # For exp1, just eat anything
                log("and decides to eat it. ", False)
                diff = self.cell.consume_plant()
                self.energy += diff
                if diff > 0:
                    log("The plant is edible (+%d energy) " % diff, False)
                else:
                    log("The plant is poisonous (%d energy) " % diff, False)

                if self.energy > 0:
                    log("and not fatal. %d energy left. " % self.energy, False)
                else:
                    log("and fatal. :< This agent has died.", False)
            else:
                # This cell doesn't have a plant. Does any of the surrounding cells have a plant?
                # Check all self.neighborhood cells for a plant that is unoccupied
                for x in range(0, len(self.neighborhood)):
                    # Is there a free cell with a plant?
                    if self.neighborhood[x]:
                        if not self.neighborhood[x].occupying_agent and self.neighborhood[x].has_plant:
                            self.cell = self.neighborhood[x]
                            decision_complete = True
                            log("- sees food nearby [%s,%s] and moves there. " % (self.cell.x, self.cell.y), False)
                            break

                # No surrounding cell has a plant. Pick a random direction to go
                while not decision_complete:
                    random_neighborhood_cell = random.randint(0, len(self.neighborhood) - 1)
                    if self.neighborhood[random_neighborhood_cell]:
                        if not self.neighborhood[random_neighborhood_cell].occupying_agent:
                            self.cell = self.neighborhood[random_neighborhood_cell]
                            decision_complete = True
                            log("- sees no food nearby and moves to a new random cell [%02d,%02d]. " %
                                (self.cell.x, self.cell.y), False)

        self.energy -= 1
        log("") # to print \n
