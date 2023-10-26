from skimage.color import rgb2gray
from IQA_Metrics_Toolbox import niqe

def niqe_score(img):
    '''
    Reference paper: https://ieeexplore.ieee.org/document/6353522
    '''
    if len(img.shape) == 2:
        return niqe.score(img)
    elif len(img.shape) == 3 and img.shape[-1] == 3:
        return niqe.score(rgb2gray(img))