from skimage.metrics import structural_similarity
from skimage.color import rgb2gray
import numpy as np

def ssim(reference, target, data_range=255, multichannel=True):
    """
    Compute the Structural Similarity Index (SSIM) between two images.

    Parameters:
        reference: numpy.ndarray
            The reference image (RGB of size (H, W, C) if multichannel=True, grayscale of size (H, W) if multichannel=False).
        target: numpy.ndarray
            The target image (RGB of size (H, W, C) if multichannel=True, grayscale of size (H, W) if multichannel=False).
        data_range: int, optional (default: 255)
            The value range of the input images (usually 255 for uint8 images).
        multichannel: bool, optional (default: True)
            True if input images are RGB, False if they are grayscale.

    Returns:
        ssim_score: float
            The SSIM score between the reference and target images.

    Required Libraries/Modules to Install: 
        python -m pip install scikit-image==0.20.0

    Reference:
        https://ieeexplore.ieee.org/document/1284395
    """

    if not isinstance(multichannel, bool):
        raise ValueError("Expected multichannel to be a boolean value.")

    if multichannel and (reference.shape[-1] != 3 or target.shape[-1] != 3):
        raise ValueError("Expected reference and target images to be RGB with 3 channels. \nIf you want to input single channel images, set the parameter 'multichannel' to False.")

    if not multichannel and (reference.ndim != 2 or target.ndim != 2):
        raise ValueError("Expected reference and target images to be grayscale. \nIf you want to input three channel images, set the parameter 'multichannel' to True.")

    return structural_similarity(reference, target, win_size=None, gradient=None,
                                 data_range=data_range, multichannel=multichannel,
                                 gaussian_weights=None, full=None)




# from skimage.metrics import structural_similarity
# from skimage.color import rgb2gray
# import numpy as np

# # def __init__(self):
# #     self.win_size = None
# #     self.gradient = False
# #     self.data_range = 255
# #     self.multichannel = 2
# #     self.gaussian_weights = False
# #     self.full = False

# def ssim(reference, target, range = 255, multiple_channel = True):
#     """
#     input:
#         multiple_channel: True, False or None
#             if True - input images need to be 3 channel images
#             if False or None - input images need to be single channel images
            
#         reference: 
#             if multiple_channel = True:
#                 RGB image of size (H, W, C) and type: uint8 ndarray
#             if multiple_channel = False:
#                 Grayscale image of size: (H, W) and type: uint8 ndarray
#         target:
#             if multiple_channel = True:
#                 RGB image of size (H, W, C) and type: uint8 ndarray
#             if multiple_channel = False:
#                 Grayscale image of size: (H, W) and type: uint8 ndarray

#     return:
#         ssim score, float.
#     import package requirements: 
#         python -m pip install scikit-image==0.20.0

#     """

#     if (multiple_channel != True) and (multiple_channel != False) and (multiple_channel != None):
#         raise ValueError(f"Expected multiple_channel to be True, False or None, instead multiple_channel = {multiple_channel}")

#     if multiple_channel == True:
#         if len(reference.shape) != 3:
#             raise ValueError(f"Expected reference image to be RGB of size (M, N, 3), received image of size: {reference.shape}")
        
#         if len(target.shape) != 3:
#             raise ValueError(f"Expected target image to be RGB of size (M, N, 3), received image of size: {target.shape}")
        
#         if len(reference.shape) == 3 and len(target.shape) == 3:
#             if reference.shape[2] != 3:
#                 raise ValueError(f"Expected reference image to be an RGB image with 3 channels, number of channels in reference image is: {reference.shape[2]}")
#             if target.shape[2] != 3:
#                 raise ValueError(f"Expected target image to be an RGB image with 3 channels, number of channels in target image is: {target.shape[2]}")
#             if (reference.shape[2] == 3) and (target.shape[2] == 3):
#                 multichannel_axis = 2

#     if (multiple_channel == False) or (multiple_channel == None):
#         if len(reference.shape) != 2:
#             raise ValueError(f"Expected reference image to be RGB of size (M, N), received image of size: {reference.shape}")
        
#         if len(target.shape) != 2:
#             raise ValueError(f"Expected target image to be RGB of size (M, N), received image of size: {target.shape}")
        
#         if len(reference.shape) == 2 and len(target.shape) == 2:
#                 multichannel_axis = None
    
    
#     return structural_similarity(reference, target, win_size=None, gradient=None,
#                                     data_range=range, channel_axis=multichannel_axis,
#                                     gaussian_weights=None, full=None)



