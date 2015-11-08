from PIL import Image
from pylab import *
from numpy import *

im = array(Image.open(r'C:\Users\Public\Pictures\Sample Pictures\desert.jpg').convert('L'))
gray()
im2 = 255 - im

im3 = (100.0/255) * im + 100

im4 = 255.0*(im/255.0)**2

imshow(im)
figure()
imshow(im2)
figure()
imshow(im3)
figure()
imshow(im4)

show()
