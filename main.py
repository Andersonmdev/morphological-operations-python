
from PIL import Image
from numpy import array
from src.closing import closing
from src.dilation import dilation
from src.erode import erode
from src.opening import opening

def run_operation_by_type(operation_type, img):
    if operation_type == 1:
        return erode(img, 5, 5)
    elif operation_type == 2:
        return dilation(img, 5, 5)
    elif operation_type == 3:
        return opening(img, 5, 5)
    elif operation_type == 4:
        return closing(img, 5, 5)
    else:
        print('[ERROR] Invalid operation type')

if __name__ == '__main__':
    print('Choose the morphological operation:')
    operation = input('1. Erosion\n2. Dilation\n3. Opening\n4. Closing\n')

    my_img = Image.open('./images/fingerprint.png')
    np_img = array(my_img.getdata())

    try:
        operation = int(operation)
    except:
        print('[ERROR] Invalid operation input')

    try:
        out_img = run_operation_by_type(operation, np_img)
        out_img = Image.fromarray(out_img)
        out_img.show('Morphological Operation')
    except:
        print('[ERROR] Operation process error')