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


from subroutines.move_randomly import *
from subroutines import AgentSubroutineEvaluateGoals
from subroutines import AgentSensorSubroutineEyesight
from subroutines.mortality import *
from subroutines.AgentSensorSubroutineEyesight import *

class Model:
    """A model is a collection of subroutines."""
    def __init__(self, name):
        self.name = name
        self.subroutines = []

    def add_subroutine(self, subroutine):
        """Add an array of subroutines to this model."""
        self.subroutines.append(subroutine)

    def get_subroutines(self):
        return self.subroutines


# The order in which subroutines are added matters. These are FIFO!
MODEL_ALPHA1 = Model('alpha1')
MODEL_ALPHA1.add_subroutine(mortality)
MODEL_ALPHA1.add_subroutine(AgentSensorSubroutineEyesight())
MODEL_ALPHA1.add_subroutine(AgentSubroutineEvaluateGoals())
MODEL_ALPHA1.add_subroutine(move_randomly)


NEWEST_MODEL = MODEL_ALPHA1