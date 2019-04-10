
import os
import imageio

cwd = os.path.dirname(os.path.abspath(__file__))


def log(msg, newline=True):
    if newline:
        print(msg)
    else:
        print(msg, end="")


the_duration = 1/12


def create_animated_gif(files, animated_gif_name, duration=the_duration):
    """Creates an animated gif from the list of files in var files."""

    # Default Duration is 1/<fps>
    the_duration = duration

    images = []
    for file in files:
        print("Grabbing snapshot '%s'... " % file)
        images.append(imageio.imread(file))
    print("Compiling GIF...")
    imageio.mimsave(animated_gif_name, images, duration=duration)
