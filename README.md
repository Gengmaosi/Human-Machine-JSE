                                                                                                                                                                                                                   
# Leveraging artificial intelligence to natural intelligence
This is the official implementation of the paper “Leveraging artificial intelligence to natural intelligence.”
We design an adaptive-learning nonverbal Turing test to imitate the certainty and variability of human behaviors simultaneously in a stepwise machine-learning manner, and monitor inter-brain neural synchrony changes with functional near-infrared spectroscopy (fNIRS).

The code for the experiment was in the folder “Adaptive-learning nonverbal Turing test.” The processed and the human-machine interaction raw data used in the experiments to support the findings was in the folder “Data analysis.” Note that different from that in the raw data and open-source code, the names of P1 and P2 were swapped in the manuscript and report summary for better readability purposes. Besides, the prompts and other information are displayed in Chinese during the experiments.

# Preparations
We recommend that the readers test the program in the newly built environment based on Python 3.8. You can run the following command in the terminal to install the needed libraries:
```
pip install -r requirements.txt
```

# Run the program
'experiments_with_Marking.py' is the complete program with marking process code, which needs the port address of the experimental equipment, e.g., fNIRS. If you want to test and change the program first without experimental equipment, you can try 'experiments.py', which annotates the marking-related codes. The running commands are as follows:
```
python experiments_with_Marking.py
```
or
```
python experiments.py
```

# Acknowledgements
Sincerely thanks for PA_exam repository (https://github.com/AddiH/PA_exam) of the stimuli and dialog window reference.  
