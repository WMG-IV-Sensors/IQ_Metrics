import torch
import piq

def fsim(reference, target):

    '''
    Reference paper: https://ieeexplore.ieee.org/document/5705575
    '''

    # Converting grayscale to RGB representation
    if len(reference.shape) == 2 and len(target.shape) == 2:
        from skimage.color import gray2rgb
        reference = gray2rgb(reference)
        target = gray2rgb(target)

    # Read RGB image and it's noisy version
    x = torch.tensor(reference).permute(2, 0, 1)[None, ...] / 255.
    y = torch.tensor(target).permute(2, 0, 1)[None, ...] / 255.


    if torch.cuda.is_available():
        # Move to GPU to make computaions faster
        x = reference.cuda()
        y = target.cuda()

    # To compute FSIM index as a measure, use lower case function from the library:
    fsim_index: torch.Tensor = piq.fsim(x, y, data_range=1.)

    return fsim_index.item()