import os
import numpy

from numpy import *
from pylab import *
from PIL import Image



def get_pic_list(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]

def image_resize(image, new_size):
    pil_im = Image.fromarray(uint8(image))
    return array(pil_im.resize(new_size))

def histeq(image, nbr_bins=256):
    imhist, bins = histogram(image.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = interp(image.flatten(), bins[:-1], cdf)
    return im2.reshape(image.shape), cdf


if __name__ == '__main__':
    im = array(Image.open(r'p:\picture\bridge_city_1-wallpaper-1920x1080.jpg').convert('L'))
    im2, cdf = histeq(im)
    imshow(im)
    show()


