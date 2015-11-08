from PIL import Image
from pylab import *

__author__ = 'william'


def show_hist(img_path):
    im = array(Image.open(img_path).convert('L'))
    figure()
    gray()
    contour(im, origin='image')
    axis('equal')
    axis('off')
    figure()
    hist(im.flatten(), 128)
    show()


if __name__ == '__main__':
    image_path = raw_input('Please input the path of the image: ')
    show_hist(image_path)

