# IQ_Metrics

## Setup Instructions

### Installing Python 3 and VScode:
1) Checking if Python and VScode are installed on your device:

    a) In command prompt, type the following commands to check python version:
        ```
        cd C:\users\your_username
        python --version
        ```
    if the output python version > 3.9.13, skip step 2)a), else execute step 2)a).

    b) In command prompt, type the following commands to check is VScode is installed:
        ```
        cd C:\users\your_username
        code --version
        ```
    if the output is a VScode version number in the format 1.xx.x, skip step 2)b), else execute step 2)b).


2) Installing Python and setting up Jupyter Notebook in vscode:

    a) Install Python 3.9.13:
    - Go to the following URL: https://www.python.org/downloads/windows/
    - Scroll down till you find the Python 3.9.13 section and then click on: 'Download Windows installer (64-bit)'

    b) Install VScode:
    - Use the following link to install VScode: https://code.visualstudio.com/Download
    - The extension to open jupyter notebooks in vscode should be automatically installed and active, if it is not consult the following documentation: https://code.visualstudio.com/docs/datascience/jupyter-notebooks

### Installing Anaconda:
1) Checking is Anaconda is installed:
    - Follow the instructions in the following url: https://docs.anaconda.com/free/anaconda/install/verify-install/
    - If you cannot see Anaconda Navigator, Anaconda prompt or if the 'conda' command is not running, install anaconda using the instructions in step 2).

2) Installing Anaconda:
    - Go to the follwing URL: https://www.anaconda.com/download/
    - click on the 'Download' button
    - The installer will start downloading. Once downloaded, open the installer and follow the installation instructions (The installer should be called 'Anaconda3-2023.03-1-Windows-x86_64')

### Cloning the IQA_Metrics_Toolbox Repository
1) Check that Python, VScode and Anaconda are installed
2) Create a new folder to store the cloned repository
3) Open the new folder in VSCode
4) Type ctrl+shift+' to open a new terminal window in VScode
5) Type the following command in the new terminal window:

    ```
    git clone -b main git@github.com:WMG-IV-Sensors/IQ_Metrics.git
    ```

    or
   
    ```
    git clone -b main https://github.com/WMG-IV-Sensors/IQ_Metrics.git
    ```
   

### Installing required libraries in base Anaconda environment:
1) Open 'Anaconda Prompt' (you can search for it in the windows search bar at the bottom left of your screen)
2) Once opened you will be presented with a command line interface
3) You should see the current active Anaconda enviromnent - it will be called: (base)
4) Change directories so that you are within the directory that holds the 'requirements.txt' file

    a) In 'Anaconda Prompt' type:
        ```cd path\to\folder\containing\cloned\iqa_metrics_gitlab_repo```
        
    b) If the folder containing the cloned repository is not in the same drive as the one seen in 'Anaconda Prompt', you can change the drive using the following command:
        ```cd /d DRIVE_NAME:\```

5) Once in the correct directory type the following command: 

    ```
    pip install -r requirements.txt
    ```


## Using the IQA Metrics:
The script ```IQA_metric_example.py``` contains examples of how to use each metric when providing it with RGB and grayscale images as inputs.


## List of IQA Metrics:
Full-Reference (FR)
===================

| Acronym | Year | Metric |
| ------- | ---- | ------ |
| PSNR    | -    | [Peak Signal-to-Noise Ratio](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio) |
| SSIM    | 2003 | [Structural Similarity](https://en.wikipedia.org/wiki/Structural_similarity) |
| MS-SSIM | 2004 | [Multi-Scale Structural Similarity](https://ieeexplore.ieee.org/abstract/document/1292216) |
| IW-SSIM | 2011 | [Information Content Weighted Structural Similarity Index](https://ece.uwaterloo.ca/~z70wang/publications/IWSSIM.pdf) |
| CW-SSIM | 2009 | [Complex Wavelet Structural Similarity Index](https://ieeexplore.ieee.org/document/5109651) |
| VIF     | 2004 | [Visual Information Fidelity](https://ieeexplore.ieee.org/document/1576816) |
| FSIM    | 2011 | [Feature Similarity Index Measure](https://ieeexplore.ieee.org/document/5705575) |
| SR-SIM  | 2012 | [Spectral Residual Based Similarity](https://sse.tongji.edu.cn/linzhang/ICIP12/ICIP-SR-SIM.pdf) |
| GMSD    | 2013 | [Gradient Magnitude Similarity Deviation](https://arxiv.org/abs/1308.3052) |
| MS-GMSD | 2017 | [Multi-Scale Gradient Magnitude Similarity Deviation](https://ieeexplore.ieee.org/document/7952357) |
| VSI     | 2014 | [Visual Saliency-induced Index](https://ieeexplore.ieee.org/document/6873260) |
| DSS     | 2015 | [DCT Subband Similarity Index](https://ieeexplore.ieee.org/document/7351172) |
| HaarPSI | 2016 | [Haar Perceptual Similarity Index](https://arxiv.org/abs/1607.06140) |
| MDSI    | 2016 | [Mean Deviation Similarity Index](https://arxiv.org/abs/1608.07433) |

No-Reference (NR)
==================

| Acronym | Year | Metric |
| ------- | ---- | ------ |
| BRISQUE | 2012 | [Blind/Referenceless Image Spatial Quality Evaluator](https://ieeexplore.ieee.org/document/6272356) |
| NIQE    | 2013 | [Natural Image Quality Evaluator](https://ieeexplore.ieee.org/document/6353522) |
| PIQUE   | 2015 | [Perception-based Image Quality Evaluator](https://ieeexplore.ieee.org/document/7084843) |






