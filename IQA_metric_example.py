# Importing Full Reference IQA Metrics
from psnr import psnr
from ssim import ssim
from cw_ssim import cw_ssim
from dss import dss
from fsim import fsim
from gmsd import gmsd
from haar_psi import haar_psi
from iw_ssim import iw_ssim
from mdsi import mdsi
from ms_gmsd import ms_gmsd
from ms_ssim import ms_ssim
from sr_sim import sr_sim
from vif import vif
from vsi import vsi

# Importing No Reference IQA Metrics
from brisque import brisque_score
from niqe import niqe_score
from pique import pique

# Importing other libraries
import os
import cv2
import numpy as np
from skimage.color import rgb2gray

## Creating function to extract images from a folder into a python list
def extract_images(path_to_images, reverse=False, image_limit=None):
    '''
    Parameters:
        path_to_images: string
            The filepath of the folder containing the images you wish to extract.
        reverse: boolean
            Set reverse to True, if you wish to extract images from path_to_images in reverse order (i.e. from the last image to the first).
        image_limit: interger
            Specifies the total number of images you wish to extract from path_to_images

    Returns:
        images: list
            A list containing all extracted images, each element in this list will be a single image.
    ''' 

    # Create an empty list to store the images
    images = []
    num_images_extracted = 0

    # Validating 'reverse' value
    if not isinstance(reverse,bool):
        raise ValueError('Invalid input for parameter reverse, please set reverse to True or False')
    # Validating 'image_limit' value
    if ((image_limit != None) and (not isinstance(image_limit, int))):
        raise ValueError('Invalid input for parameter image_limit, please set image_limit to None or interger greater than 0')
    # Validating 'image_limit' value
    if isinstance(image_limit, int):
        if image_limit <= 0:
            raise ValueError('Invalid input for parameter image_limit, please set image_limit to None or interger greater than 0')

    # If reverse is True, extract images from last to first
    if reverse == True:
        # Get the list of files in the directory
        files = os.listdir(path_to_images)
        files.reverse() # reverse file order

    # If reverse is False, extract images from first to last
    if reverse == False:
        # Get the list of files in the directory
        files = os.listdir(path_to_images)

    # Loop through all the files in the directory
    for filename in files:
        # Check if the file is an image
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') :
            # Load the image using OpenCV
            image = cv2.imread(os.path.join(path_to_images, filename))
            # Add the image to the list
            images.append(image)
            # Update image count
            num_images_extracted += 1
        
        # End extraction if images extracted == image_limit (when image_limit >= 1)
        if image_limit == None:
            continue
        elif image_limit == num_images_extracted:
            break
            
    # Print the number of images found
    print(f'Found {len(images)} images in {path_to_images}')

    # Return the list of images
    return images

###############################################
###### Using IQA Metrics with RGB Images ######

# Extracting the images from the  test_images folder (NOTE: change the image_path after cloning repository)
image_path = 'M:/Project 2 - Camera Sensor/Python Files/IQA Metric Scripts/iqa_metrics_toolbox/test_images'
images = extract_images(image_path)

# Reference Image (RGB):
ref = images[0]
# Target Image (RGB) (blurry version of 'ref'):
tar = cv2.GaussianBlur(ref,(5,5),cv2.BORDER_DEFAULT)

print(f'PSNR Value (RGB): {psnr(ref,tar)}')
print(f'SSIM Value (RGB): {ssim(ref,tar,multichannel=True)}') # NOTE: You need to set multichannel to True is you are using RGB images for SSIM
print(f'CW-SSIM Value (RGB): {cw_ssim(ref,tar)}')
print(f'DSS Value (RGB): {dss(ref,tar)}')
print(f'FSIM Value (RGB): {fsim(ref,tar)}')
print(f'GMSD Value (RGB): {gmsd(ref,tar)}')
print(f'HAAR-PSI Value (RGB): {haar_psi(ref,tar)}')
print(f'IW-SSIM Value (RGB): {iw_ssim(ref,tar)}')
print(f'MDSI Value (RGB): {mdsi(ref,tar)}')
print(f'MS_GMSD Value (RGB): {ms_gmsd(ref,tar)}')
print(f'MS-SSIM Value (RGB): {ms_ssim(ref,tar)}')
print(f'SR-SIM Value (RGB): {sr_sim(ref,tar)}')
print(f'VIF Value (RGB): {vif(ref,tar)}')
print(f'VSI Value (RGB): {vsi(ref,tar)}')
print("")
print(f'BRISQUE Value (RGB) Reference: {brisque_score(ref)}')
print(f'BRISQUE Value (RGB) Target: {brisque_score(tar)}')
print("")
print(f'NIQE Value (RGB) Reference: {niqe_score(ref)}')
print(f'NIQE Value (RGB) Target: {niqe_score(tar)}')
print("")
print(f'PIQUE Value (RGB) Reference: {pique(ref)}')
print(f'PIQUE Value (RGB) Target: {pique(tar)}')

print("")
print("--------------------------------------------------------------------------------------")
print("")

#####################################################
###### Using IQA Metrics with Grayscale Images ######

# Extracting the images from the  test_images folder (NOTE: change the image_path after cloning repository)
image_path = 'M:/Project 2 - Camera Sensor/Python Files/IQA Metric Scripts/iqa_metrics_toolbox/test_images'
images = extract_images(image_path)

# Reference Image (Grayscale):
ref = rgb2gray(images[0])

# Target Image (Grayscale) (blurry version of 'ref'):
tar = cv2.GaussianBlur(ref,(5,5),cv2.BORDER_DEFAULT)

print(f'PSNR Value (Grayscale): {psnr(ref,tar)}') 
print(f'SSIM Value (Grayscale): {ssim(ref,tar,multichannel=False)}') # NOTE: You need to set multichannel to False is you are using grayscale images for SSIM
print(f'CW-SSIM Value (Grayscale): {cw_ssim(ref,tar)}') 
print(f'DSS Value (Grayscale): {dss(ref,tar)}')
print(f'FSIM Value (Grayscale): {fsim(ref,tar)}')
print(f'GMSD Value (Grayscale): {gmsd(ref,tar)}')
print(f'HAAR-PSI Value (Grayscale): {haar_psi(ref,tar)}')
print(f'IW-SSIM Value (Grayscale): {iw_ssim(ref,tar)}')
print(f'MDSI Value (Grayscale): {mdsi(ref,tar)}')
print(f'MS_GMSD Value (Grayscale): {ms_gmsd(ref,tar)}')
print(f'MS-SSIM Value (Grayscale): {ms_ssim(ref,tar)}')
print(f'SR-SIM Value (Grayscale): {sr_sim(ref,tar)}')
print(f'VIF Value (Grayscale): {vif(ref,tar)}')
print(f'VSI Value (Grayscale): {vsi(ref,tar)}')
print("")
print(f'BRISQUE Value (Grayscale) Reference: {brisque_score(ref)}')
print(f'BRISQUE Value (Grayscale) Target: {brisque_score(tar)}')
print("")
print(f'NIQE Value (Grayscale) Reference: {niqe_score(ref)}')
print(f'NIQE Value (Grayscale) Target: {niqe_score(tar)}')
print("")
print(f'PIQUE Value (Grayscale) Reference: {pique(ref)}') 
print(f'PIQUE Value (Grayscale) Target: {pique(tar)}') 



