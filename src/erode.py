import numpy as np

def erode(img, kernel_heigth, kernel_width):
    img_width = len(img[0])
    img_heigth = len(img)

    out_img_heigth = img_heigth - (kernel_heigth-1)
    out_img_width = img_width - (kernel_width-1)

    out_img = np.ndarray([out_img_heigth, out_img_width], dtype=np.uint8)

    for i in range(out_img_heigth):
        for j in range(out_img_width):
            aux = 255
            for k in range(kernel_heigth):
                for l in range(kernel_width):
                    if (img[i+k][j+l] < aux):
                        aux = img[i+k][j+l]
            out_img[i][j] = aux

    return np.uint8(out_img)