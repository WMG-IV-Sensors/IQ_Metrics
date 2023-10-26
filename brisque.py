from IQA_Metrics_Toolbox import brisque

def brisque_score(img):
    '''
    Reference paper: https://ieeexplore.ieee.org/document/6272356
    '''
    # Converting grayscale to RGB representation
    if len(img.shape) == 2:
        from skimage.color import gray2rgb
        img = gray2rgb(img)

    return brisque.BRISQUE().score(img)
    