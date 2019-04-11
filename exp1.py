# Project Files
from Functions import *
from Agent import *
from Cell import *
from System import *

# Entities
from entities.Plant import *

# Libraries
import PIL.Image as Image
import random
import os, sys
import imageio
import glob
from natsort import natsorted, ns
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




