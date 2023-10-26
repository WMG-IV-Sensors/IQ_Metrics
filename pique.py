import numpy as np
import scipy.signal as signal
from skimage.color import rgb2gray

def pique(img):
    '''
    Reference Paper of PIQUE Metric: https://ieeexplore.ieee.org/document/7084843
    
    '''

    # # import cv2
    # # import collections
    # # from itertools import chain
    # import numpy as np
    # import scipy.signal as signal
    # from skimage.color import rgb2gray
    # # import scipy.ndimage.filters as filters
    # # import scipy.special as special
    # # import scipy.optimize as optimize
    # # import skimage.io
    # # import os


    ### MSCN/NSS Image:

    def grayscale(original_image):
        image = np.array(original_image)
        if len(image.shape) == 3 and image.shape[2] == 4:
            image = image[:, :, :3]
        return rgb2gray(image)

    def normalize_kernel(kernel):
        return kernel / np.sum(kernel)

    def gaussian_kernel2d(n, sigma):
        Y, X = np.indices((n, n)) - int(n / 2)
        gaussian_kernel = 1 / (2 * np.pi * sigma ** 2) * np.exp(-(X ** 2 + Y ** 2) / (2 * sigma ** 2))
        return normalize_kernel(gaussian_kernel)

    def local_mean(image, kernel):
        return signal.convolve2d(image, kernel, 'same')

    def local_deviation(image, img_mean, kernel):
        "Vectorized approximation of local deviation"
        sigma = image ** 2
        sigma = signal.convolve2d(sigma, kernel, 'same')
        return np.sqrt(np.abs(img_mean ** 2 - sigma))

    def calculate_mscn_coefficients(image, kernel_size=6, sigma=7 / 6):
        if len(image.shape) == 3:
            image = grayscale(image)
        C = 1 / 255
        kernel = gaussian_kernel2d(kernel_size, sigma=sigma)
        mean = local_mean(image, kernel)
        var = local_deviation(image, mean, kernel)
        return (image - mean) / (var + C)
    
    mscn_img = calculate_mscn_coefficients(img)

    ### Determining if a block in the MSCN image is spatially active:

    def block_extract(mscn):
        # obtaining number of rows and columns in the input mscn image
        mscn_shape = np.shape(mscn)
        mscn_rows = mscn_shape[0]
        mscn_cols = mscn_shape[1]

        # setting block size to be 16 by 16 pixels
        block_size = 16

        # obtaining number of blocks extracted along each row of the mscn image
        num_blocks_row = np.round(mscn_rows/block_size,0)
        if  num_blocks_row > mscn_rows/block_size:
            num_blocks_row = num_blocks_row - 1

        # obtaining number of blocks extracted along each column of the mscn image
        num_blocks_col = np.round(mscn_cols/block_size,0)
        if  num_blocks_col > mscn_cols/block_size:
            num_blocks_col = num_blocks_col - 1

        # cropping mscn image to make sure the shape allows for an interger number of blocks to be extracted 
        end_row = int(num_blocks_row*block_size)
        end_col = int(num_blocks_col*block_size)
        mscn_new = mscn[0:end_row,0:end_col]
        mscn_new = np.array(mscn_new)

        # extracting the blocks from the mscn image
        M = block_size
        N = block_size
        blocks = [mscn_new[x:x+M,y:y+N] for x in range(0,mscn_new.shape[0],M) for y in range(0,mscn_new.shape[1],N)]
        return blocks
    
    def extract_spatially_active_blocks(blocks):
        # spatially_active_index = []
        spatially_active_blocks = []
        for i in range(len(blocks)):
            if np.var((blocks[i]).flatten()) >= 0.1:
                spatially_active_blocks.append(blocks[i])

        return spatially_active_blocks
    
    ### Noticable Distortion Criterion:

    def noticable_distortion_criterion(spatially_active_blocks,block_size=16):
        ndc_true = []
        distortion_appended = False
        segment_length = 6
        segment_range = (block_size - segment_length) + 1

        # Assess each spatially active block for a given image
        for i in range(len(spatially_active_blocks)):
            block = spatially_active_blocks[i]
            # extract edges of each block
            L1 = block[0,:] # first row
            L2 = block[:,-1] # last column
            L3 = block[-1,:] # last row
            L4 = block[:,0] # first column

            # evaluate segemnts of each edge for each block to detect noticable distortion
            for j in range(segment_range):
                sd_L1 = np.sqrt(np.var(L1[(0+j):(6+j)]))
                sd_L2 = np.sqrt(np.var(L2[(0+j):(6+j)]))
                sd_L3 = np.sqrt(np.var(L3[(0+j):(6+j)]))
                sd_L4 = np.sqrt(np.var(L4[(0+j):(6+j)]))

                # if distortion is detected append 1 to the list: ndc_true
                if (sd_L1 < 0.1) or (sd_L2 < 0.1) or (sd_L3 < 0.1) or (sd_L4 < 0.1):
                    ndc_true.append(1)
                    distortion_appended = True
                    break
                else:
                    continue
            # If no distortion is found for a block - append 0 to the list: ndc_true
            if distortion_appended == False:
                ndc_true.append(0)
            distortion_appended = False

        return ndc_true
        
    ### Noise Criterion:

    def noise_criterion(spatially_active_blocks):
        nc_true = []
        # distortion_appended = False
        # segment_length = 6
        # segment_range = (block_size - segment_length) + 1

        # Assess each spatially active block for a given image
        for i in range(len(spatially_active_blocks)):
            block = spatially_active_blocks[i]
            centre = (block[:,7:9]).flatten()
            surrounding = (np.concatenate((block[:,0:7],block[:,9:16]),axis=1)).flatten()
            block_flat = block.flatten()

            sd_block = np.sqrt(np.var(block_flat))
            sd_centre = np.sqrt(np.var(centre))
            sd_surrounding = np.sqrt(np.var(surrounding))

            beta = np.absolute((sd_centre/sd_surrounding)-sd_block)/np.maximum((sd_centre/sd_surrounding),sd_block)

            if sd_block > beta:
                nc_true.append(1)
            elif sd_block <= beta:
                nc_true.append(0)

        return nc_true
    

    ### PIQUE Score function:
    def pique_score():
        blocks = block_extract(mscn_img)
        sa_blocks = extract_spatially_active_blocks(blocks)
        num_sa_blocks = len(sa_blocks)
        const = 1

        ndc_true = noticable_distortion_criterion(sa_blocks)
        nc_true = noise_criterion(sa_blocks)

        # pooling:
        Dsk = []
        for i in range(num_sa_blocks):
            var_block = np.var(sa_blocks[i])
            if ndc_true[i] == 1 and nc_true[i] == 1:
                Dsk.append(1)
            if ndc_true[i] == 1 and nc_true[i] == 0:
                Dsk.append(var_block)
            if nc_true[i] == 1 and ndc_true[i] == 0:
                Dsk.append((1-var_block))
            if nc_true[i] == 0 and ndc_true[i] == 0:
                Dsk.append(0)
        
        pique_value = (np.sum(Dsk) + const)/(num_sa_blocks + const)
        return pique_value
    

    return pique_score()