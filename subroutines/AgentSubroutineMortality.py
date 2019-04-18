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

# TODO: Version 2: Regenerate one energy at the start of the turn (up to a maximum).

from cares.Functions import *
from cares.Subroutine import AgentSubroutine


class AgentSubroutineMortality(AgentSubroutine):
    """This subroutine will hard-stop the agent if energy <= 0."""
    def process(self, agent):
        if agent.energy <= 0:
            # This agent will be cleaned up by the System update function
            if not agent.system.quiet:
                log("- as died (energy = %d) and will be removed from the system." % agent.energy)
            agent.alive = False
            return False
