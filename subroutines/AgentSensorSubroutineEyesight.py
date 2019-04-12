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

from cares.Functions import *
from subroutines.Subroutine import AgentSubroutine


class AgentSensorSubroutineEyesight(AgentSubroutine):

    def process(self, agent):
        """Identifies neighborhood cells and stores them in an array."""
        log("- Processing eyesight sensors... ", False)
        # Look around us. What cells are there?
        x_pos = agent.cell.x
        y_pos = agent.cell.y

        # Cells around agent. Using immediate cells
        # north, east, south, and west
        # TODO: Update tinyDB for this agent with what it sees in its environment.
        agent.neighborhood = [
            agent.system.cells[x_pos][y_pos-1]
            if y_pos > 0 else False,

            agent.system.cells[x_pos+1][y_pos]
            if x_pos < agent.system.width-1 else False,

            agent.system.cells[x_pos][y_pos+1]
            if y_pos < agent.system.height-1 else False,

            agent.system.cells[x_pos-1][y_pos]
            if x_pos > 0 else False
        ]

        log("[ OK ]")