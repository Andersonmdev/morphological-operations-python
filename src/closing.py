import numpy as np
from .dilation import dilation
from .erode import erode

def closing(img, kernel_heigth, kernel_width):
    dilated_img = dilation(img, kernel_heigth, kernel_width)
    out_img = erode(dilated_img, kernel_heigth, kernel_width)
    return np.uint8(out_img)