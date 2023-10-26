import torch
import piq

def vif(reference, target):

    '''
    Reference paper: https://ieeexplore.ieee.org/document/1576816
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

    # To compute VIF index as a measure, use lower case function from the library:
    vif_index: torch.Tensor = piq.vif_p(x, y, data_range=1.)

    return vif_index.item()