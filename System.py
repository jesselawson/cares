import PIL.Image as Image
import random
import os, sys
import imageio
import glob
from natsort import natsorted, ns
from pathlib import Path

# Project Files

from Agent import *
from Cell import *
from entities.Plant import *
from Functions import *

class System:
    def __init__(self, experiment_name, width_height, num_starting_agents, num_starting_plants, max_system_steps=False, quiet=False):
        self.experiment_name = experiment_name
        self.width = width_height
        self.height = width_height
        self.cells = [[None for x in range(width_height)] for y in range(width_height)]
        self.agents = []
        self.num_starting_agents = num_starting_agents
        self.num_starting_plants = num_starting_plants
        self.quiet = quiet
        self.max_system_steps = max_system_steps
        # TODO: num_starting_agents should be customizable
        self.max_active_plants = num_starting_agents*2
        # Populate cells
        for x in range(0, width_height):
            for y in range(0, width_height):
                self.cells[x][y] = Cell(x, y)


        self.elapsed_time = 0

        # Grow random plants
        for x in range(num_starting_plants):
            planted = False
            while not planted:
                random_x = random.randint(0, width_height - 1)
                random_y = random.randint(0, width_height - 1)

                if not self.cells[random_x][random_y].has_plant:
                    planted = True
                    self.cells[random_x][random_y].grow_plant()

        # Populate system with starting agents
        for i in range(0, self.num_starting_agents):
            if not quiet:
                log("> Building agent %d..." % i)
            cell_is_open = False
            while not cell_is_open:

                random_x = random.randint(0, width_height-1)
                random_y = random.randint(0, width_height-1)

                if not quiet:
                    log("-> Trying to put agent at {%s, %s}..." % (random_x, random_y))
                if not self.cells[random_x][random_y].occupying_agent:
                    this_agent = Agent(i, self.cells[random_x][random_y])
                    self.agents.append(this_agent)
                    self.cells[random_x][random_y].occupying_agent = self.agents[-1] # Get most recently appended agent
                    cell_is_open = True
                    if not quiet:
                        log("- -> Looks good!")
                else:
                    if not quiet:
                        log("- -> Already occupied!")

        # Generate snapshot configurations
        self.agent_image = Image.open(Path(cwd + "/images/agent.jpg"))
        self.agent_image.thumbnail([16, 16], Image.FASTOCTREE)

        self.plant_images = []

        self.blank_image = Image.open(Path(cwd + "/images/empty.jpg"))
        self.blank_image.thumbnail([16, 16], Image.FASTOCTREE)

        for x in range(1, 6):
            log("Reading plant%d.jpg..." % x)
            the_image = Image.open(Path(cwd + "/images/plant%d.jpg" % x))
            the_image.thumbnail([16, 16], Image.FASTOCTREE)
            self.plant_images.append(the_image)

        # The snapshot_base is a big white layer on which we'll build each step configuration.
        # Doing it this way means we save processing power by not having to recreate the background
        # every time.
        self.snapshot_base = Image.new('RGB', (8*self.width, 8*self.height))

        for i in range(0, 8*self.width, 8):
            for j in range(0, 8*self.height, 8):
                # Paste empty cells
                self.snapshot_base.paste(self.blank_image, (i, j))

    def num_active_plants(self):
        num_plants = 0
        for x in range(0, self.width):
            for y in range(0, self.height):
                num_plants += 1 if self.cells[x][y].has_plant else 0
        return num_plants

    def step_time(self):
        """Run through all agents and have them create an action and commit to an action."""

        self.print_step()

        while self.elapsed_time < self.max_system_steps:
            self.elapsed_time += 1
            self.update_system()
            self.print_step()


    def update_system(self):
        # Update any occupying agents
        log("Day #%02d has begun!" % (self.elapsed_time))
        i = 0
        for x in range(0, self.width):
            for y in range(0, self.height):
                """TODO: Cell.update() (which includes check for occupying agent, and then updates that agent accordingly)"""

                # Is this cell occupied?
                if self.cells[x][y].occupying_agent:
                    agent = self.cells[x][y].occupying_agent
                    i+=1

                    # Call any agent updating that needs to happen

                    if agent.energy <= 0:
                        try:
                            log("* Agent #%02d (Starting Energy: %03d) has died and is being removed from the system." % (agent.agent_id, agent.energy))
                            self.agents.remove(agent)
                            self.cells[x][y].occupying_agent = None
                        except ValueError:
                            pass
                    else:
                        agent.update(self)

        # Grow any new plants that need to be grown
        num_new_plants = self.max_active_plants - self.num_active_plants()
        if not num_new_plants <= 0:
            if not self.quiet:
                log("* Planting %d new plants." % num_new_plants)

        for x in range(1, ):

            planted = False
            while not planted:
                random_x = random.randint(0, self.width - 1)
                random_y = random.randint(0, self.height - 1)

                if not self.cells[random_x][random_y].has_plant:
                    planted = True
                    self.cells[random_x][random_y].grow_plant()

        log("Day #%02d has ended!" % (self.elapsed_time))

    def print_step(self):
        """Create a graphical representation of the step at t=self.elapsed_time."""
        snapshot = self.snapshot_base.copy() # Create a copy so we don't have artifacts from step_{t-1}

        # Print the plants
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.cells[x][y].has_plant:
                    plant_img_id = self.cells[x][y].plant.img_id
                    #log("Trying to get plant id %s..." % plant_img_id)
                    the_image = self.plant_images[plant_img_id-1]
                    snapshot.paste(the_image, self.cells[x][y].get_map_coords())

                    #if not self.quiet:
                    #    log("Printing %s at [%s, %s] " % (self.cells[x][y].plant.id, self.cells[x][y].x, self.cells[x][y].y))

        # Print the agents
        for i in self.agents:
            the_image = self.agent_image
            snapshot.paste(the_image, i.cell.get_map_coords())

            if not self.quiet:
                x, y = i.cell.get_map_coords()
                #log("Printing Agent A%s at [%s, %s]" % (i, x, y))

        # Finally, save the file
        snapshot.save(Path(cwd + "/%s/states/%s-t%02d.jpg" %
                           (self.experiment_name, self.experiment_name, self.elapsed_time)))

        # In this next part, we'll create some mathplot

    def generate_animation(self):
        cwd = os.path.dirname(os.path.abspath(__file__))
        images_path = r'%s/%s/states/%s-t*.jpg' % (cwd, self.experiment_name, self.experiment_name)
        state_snapshots = glob.glob(images_path)
        state_snapshots = natsorted(state_snapshots, alg=ns.IGNORECASE)
        print("Creating animation for these states...")
        create_animated_gif(state_snapshots, Path(cwd + "/%s/states/%s_animated.gif" %
                                                  (self.experiment_name, self.experiment_name)))