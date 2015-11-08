from PIL import Image
from pylab import *

im = array(Image.open(r'p:\picture\modern_architecture-wallpaper-1920x1080.jpg'))

imshow(im)

print 'Please click 3 points'

x = ginput(3)

print 'you clicked: ', x

show()