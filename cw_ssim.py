from skimage.color import rgb2gray
import numpy as np
from scipy import signal 

def validate_and_convert_to_gray(image):
    size = 2
    if len(image.shape) == size:
        return image
    elif len(image.shape) == 3 and image.shape[-1] == 3:
        return rgb2gray(image)
    elif len(image.shape) == 3 and image.shape[-1] != 3:
        raise ValueError(f"Expected image to be RGB image of size (M, N, 3), received image of size: {image.shape}")
    else:
        raise ValueError(f"Expected image to be grayscale of size (M, N), received image of size: {image.shape}")

def cw_ssim(reference, target, width=8):
    """Compute the complex wavelet SSIM (CW-SSIM) value from the reference
    image to the target image.

    Parameters:
        reference: numpy.ndarray or equivilant
            The reference image (RGB of size (H, W, C) or grayscale of size (H, W)).
            - H = Height of the image (number of rows)
            - W = Width of the image (number of columns)
            - C = Number of channels in the image
        target: numpy.ndarray or equivilant
            The target image (RGB of size (H, W, C) or grayscale of size (H, W)).
            - H = Height of the image (number of rows)
            - W = Width of the image (number of columns)
            - C = Number of channels in the image
    Returns:
        Computed CW-SSIM float value.

    Reference:
        https://ieeexplore.ieee.org/document/5109651 
        
    """

    # Define a width for the wavelet convolution
    widths = np.arange(1, width+1)
    k = 0.01

    # Use the image data as arrays
    sig1 = np.array(reference)
    sig2 = np.array(target)

    # Validate shape of input images
    sig1 = validate_and_convert_to_gray(sig1)
    sig1 = sig1.flatten()
    sig2 = validate_and_convert_to_gray(sig2)
    sig2 = sig2.flatten()

    # # Converting to grayscale if necessary
    # if len(sig1.shape) == 3 and sig1.shape[-1] == 3:
    #     sig1 = rgb2gray(sig1)
    #     sig1 = sig1.flatten()
    
    # if len(sig2.shape) == 3 and sig2.shape[-1] == 3:
    #     sig2 = rgb2gray(sig2)
    #     sig2 = sig2.flatten()
        

    # Wavelet Transform convolution
    cwtmatr1 = signal.cwt(sig1, signal.ricker, widths)
    cwtmatr2 = signal.cwt(sig2, signal.ricker, widths)

    # Compute the first term
    c1c2 = np.multiply(abs(cwtmatr1), abs(cwtmatr2))
    c1_2 = np.square(abs(cwtmatr1))
    c2_2 = np.square(abs(cwtmatr2))
    num_ssim_1 = 2 * np.sum(c1c2, axis=0) + k
    den_ssim_1 = np.sum(c1_2, axis=0) + np.sum(c2_2, axis=0) + k

    # Compute the second term
    c1c2_conj = np.multiply(cwtmatr1, np.conjugate(cwtmatr2))
    num_ssim_2 = 2 * np.abs(np.sum(c1c2_conj, axis=0)) + k
    den_ssim_2 = 2 * np.sum(np.abs(c1c2_conj), axis=0) + k

    # Compute the CW-SSIM score
    cw_ssim_score = np.average((num_ssim_1 / den_ssim_1) * (num_ssim_2 / den_ssim_2))
    
    return cw_ssim_score