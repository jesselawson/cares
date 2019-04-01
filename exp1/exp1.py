
from exp1_functions import *
import PIL.Image as Image
import os, sys

cwd = os.path.dirname(os.path.abspath(__file__))

#system = System(100, 3, 25, 5)
#system.print_step()
#system.step_time()

#opens an image:
im = Image.open(cwd+"\\images\\plant1.png")
#creates a new empty image, RGB mode, and size 400 by 400.
new_im = Image.new('RGB', (400,400))

#Here I resize my opened image, so it is no bigger than 100,100
im.thumbnail((100,100))
#Iterate through a 4 by 4 grid with 100 spacing, to place my image
for i in range(0,500,100):
    for j in range(0,500,100):
        #I change brightness of the images, just to emphasise they are unique copies.
        #im=Image.eval(im,lambda x: x+(i+j)/30)
        #paste the image at location i,j:
        new_im.paste(im, (i,j))

new_im.show()



