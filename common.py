import os
import numpy

from numpy import *
from PIL import Image



def get_pic_list(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]

def image_resize(image, new_size):
    pil_im = Image.fromarray(uint8(image))
    return array(pil_im.resize(new_size))

def histeq(image, nbr_bins=256):


if __name__ == '__main__':
    pass

