
from exp1_functions import *
import PIL.Image as Image
import os, sys
import imageio
import glob
from natsort import natsorted, ns
from pathlib import Path

cwd = os.path.dirname(os.path.abspath(__file__))

system = System(width_height=50,
                num_starting_agents=10,
                num_starting_plants=100,
                max_system_steps=50)

system.step_time()

# Now that it's done, convert the images in /images/exp1-t*.jpg to a gif

def create_animated_gif(files, animated_gif_name, duration=.05):
    """Creates an animated gif from the list of files in var files."""
    images = []
    for file in files:
        print("Grabbing snapshot '%s'... " % file)
        images.append(imageio.imread(file))
    print("Compiling GIF...")
    imageio.mimsave(animated_gif_name, images, duration=duration)

images_path = r'%s/states/exp1-t*.jpg' % cwd
state_snapshots = glob.glob(images_path)
state_snapshots = natsorted(state_snapshots, alg=ns.IGNORECASE)
print("Creating animation for these states...")
create_animated_gif(state_snapshots, Path(cwd+"/states/exp1_animated.gif"))



