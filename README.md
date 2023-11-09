                                                                                                                                                                                                                   
# Human-Machine-JSE
This is the official implementation of ''. The abstract is ''.

# Preparations
We recommend the readers test the program in the newly-built environment based on Python 3.8, which we tested in Nov. 2023. You can run the following command in the terminal to install the needed libraries:
###pip install -r requirements.txt 

# Run the program
'experiments_with_Marking.py' is the complete program with marking process code, which needs the port address of the experimental equipment, e.g., fNIRS. If you want to test and change the program first without experimental equipment, you can try 'experiments.py', which annotates the marking-related codes. The running commands are as follows:
    #python experiments_with_Marking.py
    or
    #python experiments.py

# Note for the reliable libraries
In the initial version, our experiment was built and tested on Python=3.7, psychopy==2022.1.4, fitter==1.5.2, pandas==1.1.3, and numpy==1.19.5. However, during recent testing, we found that there were errors when installing Python=2022.1.4 library in Python 3.7 environment, possibly due to version update iterations. Thus, we have provided the library version that can run smoothly in the Python 3.8 environment in requirements.txt for your reference (until 2023/11). In summary, please ensure that the libraries in right versions such as psycopy, filter, pandas, and numpy are installed correctly before running the program.

