from skimage.metrics import peak_signal_noise_ratio
from skimage.color import rgb2gray
import numpy as np

def validate_and_convert_to_gray(image):
    size = 2
    if len(image.shape) == size:
        return image
    elif len(image.shape) == 3 and image.shape[2] == 3:
        return rgb2gray(image)
    elif len(image.shape) == 3 and image.shape[2] != 3:
        raise ValueError(f"Expected image to be RGB image of size (M, N, 3), received image of size: {image.shape}")
    else:
        raise ValueError(f"Expected image to be grayscale of size (M, N), received image of size: {image.shape}")

def psnr(reference, target, range=255):
    """
    Inputs:
        reference: 
            - Grayscale image of size: (H, W), type: uint8 ndarray.
            - RGB image of size: (H, W, 3), type: uint8 ndarray.
        target: 
            - Grayscale image of size: (H, W) and type: uint8 ndarray.
            - RGB image of size: (H, W, 3) and type: uint8 ndarray.
        range: Image pixel value range (default: 0 to 255), type: interger

    Return:
        PSNR score: type = float

    Import package requirements: 
        python -m pip install scikit-image==0.20.0 
        python -m pip install numpy
    """
    reference = validate_and_convert_to_gray(reference)
    target = validate_and_convert_to_gray(target)
    return peak_signal_noise_ratio(reference, target, data_range=range)





        
    

    
    
