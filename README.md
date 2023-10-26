# IQ_Metrics

<!-- ## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://wmg-gitlab.wmgds.wmg.warwick.ac.uk/iv-sensors/grads/ima/iqa_metrics_toolbox.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://wmg-gitlab.wmgds.wmg.warwick.ac.uk/iv-sensors/grads/ima/iqa_metrics_toolbox/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers. -->

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
    git clone -b main git@wmg-gitlab.wmgds.wmg.warwick.ac.uk:iv-sensors/grads/ima/iqa_metrics_toolbox.git
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






