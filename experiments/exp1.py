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

# Project Files
from cares.System import *

# Entities

# Libraries
import os
from pathlib import Path

cwd = os.path.dirname(os.path.abspath(__file__))

experiment_name = "exp1a"

directories = [
    Path(cwd+'/%s' % experiment_name),
    Path(cwd+'/%s/images' % experiment_name),
    Path(cwd+'/%s/states' % experiment_name)
]

log("Making directories for %s... " % experiment_name, False)
for dir in directories:
    try:
        os.makedirs(dir)
    except FileExistsError:
        # directory already exists
        pass

log("[OK]")

system = System(
                experiment_name=experiment_name,
                width_height=50,
                num_starting_agents=10,
                num_starting_plants=250,
                max_system_steps=50)

system.step_time()

system.generate_animation()

# Results
"""
All agents die out fairly quickly.




"""

# Considerations for Future Experiments
"""
* Increase number of starting plants to see if agents can survive to at least day 50


"""


"""
exp1a:
width_height=50,
                num_starting_agents=10,
                num_starting_plants=250,
                max_system_steps=50)

exp1b:
system = System(experiment_name=experiment_name,
                width_height=50,
                num_starting_agents=35,
                num_starting_plants=250,
                max_system_steps=50)
                
Here they're all going north because I don't randomly pick one of the n-number of 
cells that surround it that contain plants. I only go for the first one--which
just so happens to be the top one.

"""




