

from Project import *

cwd = os.path.dirname(os.path.abspath(__file__))

experiment_name = "exp1"

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

system = System(experiment_name="exp1",
                width_height=50,
                num_starting_agents=10,
                num_starting_plants=100,
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





