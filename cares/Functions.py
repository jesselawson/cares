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
