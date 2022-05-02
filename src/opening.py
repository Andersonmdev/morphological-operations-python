import numpy as np
from .dilation import dilation
from .erode import erode

def opening(img, kernel_heigth, kernel_width):
    eroded_img = erode(img, kernel_heigth, kernel_width)
    out_img = dilation(eroded_img, kernel_heigth, kernel_width)
    return np.uint8(out_img)