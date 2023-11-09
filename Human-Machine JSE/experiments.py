### Import ###
from psychopy import visual, core, event, gui, data, clock
import random
import pandas as pd
import numpy as np
import time

### Introduce the parallel module and set the port address for the marking purpose ###
from psychopy import parallel
# port = parallel.setPortAddress(address=0x3FF0)

### Collecting basic data ###
# define white box window
win_box = visual.Window(color = "white", size=(1440, 847), pos=(0,0))

# HUMANLIKE_RT_STD = 0.0264
# HUMANLIKE_RT_MEAN = 0.3374
#human_rt = np.random.uniform(HUMANLIKE_RT_MEAN - HUMANLIKE_RT_STD, HUMANLIKE_RT_MEAN + HUMANLIKE_RT_STD)

# Get experiment parameters ##
# define dialogue box
dialog_1 = gui.Dlg(title = "Experiment Parameters")
dialog_1.addText('Welcome to the experiment! First please set the experimental parameters.\nFill in the blanks without the participants:')

# dialog_1 = gui.Dlg(title = "设置实验ID")
# dialog_1.addText('欢迎开始实验! 请填写实验ID: \n')

dialog_1.addField("Experimental ID: ")

# dialog_1.addField("实验ID: ")


# show dialog 1
dialog_1.show()

if dialog_1.OK:
    # save variables
    exp_ID = dialog_1.data[0]

elif dialog_1.Cancel:
    core.quit()

# Get participant parameters ##
# define dialogue box
dialog_2 = gui.Dlg(title = "Participant Information")
dialog_2.addText('Welcome to the experiment! First we need some data from you.\nFill in the blanks below for each participant.\nPlease use the alphabetic of your name (For example, Geng Maosi, Xia Yingji, etc.)')
dialog_2.addField("Number ID of the participant 1: ")
dialog_2.addField("Name of the participant 1: ")
dialog_2.addField("Number ID of the participant 2: ")
dialog_2.addField("Name of the participant 2: ")

# dialog_2 = gui.Dlg(title = "参与者信息")
# dialog_2.addText('欢迎开始实验! 首先我们需要采集您们的基本信息。\n请受试者1按要求填写两位受试者信息。')
# dialog_2.addField("受试者1的ID: ")
# dialog_2.addField("受试者1的姓名: ")
# dialog_2.addField("受试者2的ID: ")
# dialog_2.addField("受试者2的姓名: ")

# show dialog 2
dialog_2.show()
if dialog_2.OK:
    # save variables
    P1_ID = dialog_2.data[0]
    P1_name = dialog_2.data[1]
    P2_ID = dialog_2.data[2]
    P2_name = dialog_2.data[3]
    #block_ID = dialog_2.data[4]
elif dialog_2.Cancel:
    core.quit()

### Welcome text ###
# define window
win1 = visual.Window(color = "black",screen=1, fullscr = True)
win2 = visual.Window(color = "black",screen=2, fullscr = True)

# prepare welcome text
text1 = visual.TextStim(win1, text = "Welcome to the experiment! \n {} place your index finger on the W button. \n {} place your index finger on the P button. \n {} Press spacebar to continue.".format('Participant 1','Participant 2','Participant 1'))
text2 = visual.TextStim(win2, text = "Welcome to the experiment! \n {} place your index finger on the W button. \n {} place your index finger on the P button. \n {} Press spacebar to continue.".format('Participant 1','Participant 2','Participant 1'))
# text1 = visual.TextStim(win1, text = "欢迎开始实验!\n受试者1请将手指放在W键上。\n受试者2请将手指放在P键上。\n完成后请受试者1按空格键继续实验。")
# text2 = visual.TextStim(win2, text = "欢迎开始实验!\n受试者1请将手指放在W键上。\n受试者2请将手指放在P键上。\n完成后请受试者1按空格键继续实验。")

text1.draw()
text2.draw()
win1.flip()
win2.flip()
event.waitKeys(keyList = ["space"])

text1 = visual.TextStim(win1, text = "A circle will be shown on the screen.\n {} should press W when the circle is yellow. \n {} should press P when the circle is blue. \n Please response as fast as possible, while still responsing correctly.\n {} Press spacebar to start the practise trials.".format('Participant 1','Participant 2','Participant 1'))
text2 = visual.TextStim(win2, text = "A circle will be shown on the screen.\n {} should press W when the circle is yellow. \n {} should press P when the circle is blue. \n Please response as fast as possible, while still responsing correctly.\n {} Press spacebar to start the practise trials.".format('Participant 1','Participant 2','Participant 1'))
# text1 = visual.TextStim(win1, text = "屏幕上将出现一个圆圈。\n当圆圈是黄色时，请受试者1按下W键。\n当圆圈是蓝色时，请受试者2按下P键。\n 请快速准确地完成按键。\n准备好后，请受试者1按空格键继续实验。")
# text2 = visual.TextStim(win2, text = "屏幕上将出现一个圆圈。\n当圆圈是黄色时，请受试者1按下W键。\n当圆圈是蓝色时，请受试者2按下P键。\n 请快速准确地完成按键。\n准备好后，请受试者1按空格键继续实验。")

text1.draw()
text2.draw()
win1.flip()
win2.flip()
event.waitKeys(keyList = ["space"])

win1.flip()
win2.flip()
core.wait(1)

### Practise trials ###
# Load in all stimuli

BR1 = visual.ImageStim(win1, image = "stimuli/BR_F.png")
BL1 = visual.ImageStim(win1, image = "stimuli/BL_F.png")
YR1 = visual.ImageStim(win1, image = "stimuli/YR_F.png")
YL1 = visual.ImageStim(win1, image = "stimuli/YL_F.png")
# BM1 = visual.ImageStim(win1, image = "stimuli/BM.png")
# YM1 = visual.ImageStim(win1, image = "stimuli/YM.png")
f_cross1 = visual.ImageStim(win1, image = "stimuli/fix_cross.png")
# question1 = visual.ImageStim(win2, image = "stimuli/question1.png")
question1 = visual.ImageStim(win2, image = "stimuli/English_question1.png")

BR2 = visual.ImageStim(win2, image = "stimuli/BR_F.png")
BL2 = visual.ImageStim(win2, image = "stimuli/BL_F.png")
YR2 = visual.ImageStim(win2, image = "stimuli/YR_F.png")
YL2 = visual.ImageStim(win2, image = "stimuli/YL_F.png")
# BM2 = visual.ImageStim(win2, image = "stimuli/BM.png")
# YM2 = visual.ImageStim(win2, image = "stimuli/YM.png")
f_cross2 = visual.ImageStim(win2, image = "stimuli/fix_cross.png")
# question2 = visual.ImageStim(win1, image = "stimuli/question2.png")
question2 = visual.ImageStim(win1, image = "stimuli/English_question2.png")

# Include 2 of each stimuli in pactise trials
prac_order1 = [BR1, BL1, YR1, YL1] * 1
prac_order2 = [BR2, BL2, YR2, YL2] * 1
# randomise order
random_index = list(range(len(prac_order1)))
random.shuffle(random_index)

new_order1 = []
new_order2 = []
for i in range(len(random_index)):
    new_order1.append(prac_order1[random_index[i]])
    new_order2.append(prac_order2[random_index[i]])
prac_order1 = new_order1
prac_order2 = new_order2

for idx in range(len(prac_order1)):
    stim1 = prac_order1[idx]
    stim2 = prac_order2[idx]
    f_cross1.draw()
    f_cross2.draw()
    win1.flip()
    win2.flip()
    core.wait(1)
    stim1.draw(win1)
    stim2.draw(win2)
    win1.flip()
    win2.flip()
    # wait for the participant to press W or P or esc
    key = event.waitKeys(keyList = ["w", "p", "escape"], maxWait=(2.0))

# if escape if pressed - end the experiment
    # if no key is pressed, show "too slow"
    if key == None:
        text1 = visual.TextStim(win1, text = "Too slow")
        text2 = visual.TextStim(win2, text="Too slow")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(1)
    # if esc is pressed quit the experiment
    elif key[0] == "escape":
        core.quit()
    # if w is pressed when a  yellow circle is shown, show "correct"
    elif (key [0] == "w" and (stim1 == YR1 or stim1 == YL1)):
        text1 = visual.TextStim(win1, text = "Correct", color = "green")
        text2 = visual.TextStim(win2, text="Correct", color="green")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(1)
    # if p is pressed when a  blue circle is shown, show "correct"
    elif (key [0] == "p" and (stim1 == BR1 or stim1 == BL1)):
        text1 = visual.TextStim(win1, text = "Correct", color = "green")
        text2 = visual.TextStim(win2, text="Correct", color="green")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(1)
    # if the wrong key is pressed, show "error"
    else:
        text1 = visual.TextStim(win1, text = "Error", color = "red")
        text2 = visual.TextStim(win2, text="Error", color="red")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(1)

### Experiment ###
## Welcome text ##
text1 = visual.TextStim(win1, text = "Good job! {} Press spacebar to continue to the experiment.\n Note that during the first part of the experiment, you will be working with your partner on the task.".format('Participant 1'))
text2 = visual.TextStim(win2, text = "Good job! {} Press spacebar to continue to the experiment.\n Note that during the first part of the experiment, you will be working with your partner on the task.".format('Participant 1'))
# text1 = visual.TextStim(win1, text = "恭喜完成练习! 请受试者1按 空格 键继续实验。\n请注意，在实验的第一部分，\n"
#                                      "您将与您的合作伙伴共同完成任务。")
# text2 = visual.TextStim(win2, text = "恭喜完成练习! 请受试者1按 空格 键继续实验。\n请注意，在实验的第一部分，\n"
#                                      "您将与您的合作伙伴共同完成任务。")
text1.draw()
text2.draw()
win1.flip()
win2.flip()
key = event.waitKeys(keyList = ["space",'escape'])

if key[0] == "escape":
    core.quit()

text1 = visual.TextStim(win1, text="The first part will start soon.")
text2 = visual.TextStim(win2, text="The first part will start soon.")
# text1 = visual.TextStim(win1, text="第一部分正式实验将马上开始")
# text2 = visual.TextStim(win2, text="第一部分正式实验将马上开始")

text1.draw()
text2.draw()
win1.flip()
win2.flip()
core.wait(2)
#since = time.time()
win1.flip()
win2.flip()
core.wait(1)

# Include 2 of each stimuli in pactise trials

prac_orders1 = []
prac_orders2 = []

# Formal experimental setting
prac_order1 = [BR1, BL1, YR1, YL1] * 25
prac_order2 = [BR2, BL2, YR2, YL2] * 25

# Test experimental setting
# prac_order1 = [BR1, BL1, YR1, YL1] * 1
# prac_order2 = [BR2, BL2, YR2, YL2] * 1
# randomise order
random_index = list(range(len(prac_order1)))
random.shuffle(random_index)

new_order1 = []
new_order2 = []
for i in range(len(random_index)):
    new_order1.append(prac_order1[random_index[i]])
    new_order2.append(prac_order2[random_index[i]])

prac_orders1.append(new_order1)
prac_orders2.append(new_order2)

random_index = list(range(len(prac_order1)))
random.shuffle(random_index)

new_order1 = []
new_order2 = []
for i in range(len(random_index)):
    new_order1.append(prac_order1[random_index[i]])
    new_order2.append(prac_order2[random_index[i]])

prac_orders1.append(new_order1)
prac_orders2.append(new_order2)
# prac_order1 = new_order1
# prac_order2 = new_order2

# define stopwatch
stopwatch = core.Clock()

#record the reaction times of Participant 2
ada_rts = []
p2_rts = []

rest_time = 300
since = time.time()

for i in range(len(prac_orders1)):
    prac_order1 = prac_orders1[i]
    prac_order2 = prac_orders2[i]

    for idx in range(len(prac_order1)):
        stim1 = prac_order1[idx]
        stim2 = prac_order2[idx]
        f_cross1.draw()
        f_cross2.draw()
        win1.flip()
        win2.flip()
        core.wait(1)
        stim1.draw(win1)
        stim2.draw(win2)
        win1.flip()
        win2.flip()

        # wait for the participant to press W or P or esc
        stopwatch.reset()
        key = event.waitKeys(keyList=["w", "p", "escape"], maxWait=(2.0))
        rt = stopwatch.getTime()
        if key == None:
            print('too slow')
        elif key[0] == "escape":
            core.quit()
        elif (key[0] == "w" and (stim1 == YR1 or stim1 == YL1)):
            ada_rts.append(rt)
        elif (key[0] == "p" and (stim2 == BR2 or stim1 == BL2)):
            p2_rts.append(rt)

        # text1.draw()
        # text2.draw()
        win1.flip()
        win2.flip()
        core.wait(1)

    if i == 0:
        text1 = visual.TextStim(win1,
                                text="Please rest for a moment. \n When you and your partner are ready, press spacebar once to continue the experiment.")
        text2 = visual.TextStim(win2,
                                text="Please rest for a moment. \n When you and your partner are ready, press spacebar once to continue the experiment.")
        # text1 = visual.TextStim(win1,
        #                         text="请休息片刻。\n当你跟同伴休息好后，请按空格键继续试验。")
        # text2 = visual.TextStim(win2,
        #                         text="请休息片刻。\n当你跟同伴休息好后，请按空格键继续试验。")

        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        event.waitKeys(keyList=["space"])
        event.waitKeys(keyList=["space"])
        text1 = visual.TextStim(win1, text="The next block will begin soon.")
        text2 = visual.TextStim(win2, text="The next block will begin soon.")
        # text1 = visual.TextStim(win1, text="实验马上继续")
        # text2 = visual.TextStim(win2, text="实验马上继续")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(2)
        since = time.time()
        win1.flip()
        win2.flip()
        core.wait(1)


# Part 2 Experiment: human with machine, 20 block, 2+6(1)+6(1)+6(1)

text1 = visual.TextStim(win1, text="Good job! Please rest for a moment.\nThe second part of the experiment will start soon. When you are ready, please press spacebar twice to continue.\n "
                                   "Note that in the second part of the experiment, you will be either working with your partner or with a machine. \n"
                                   "After we asked, “Do you think human partner did the task, or the machine did the task?” Please answer quickly and accurately!")
text2 = visual.TextStim(win2, text="Good job! Please rest for a moment.\nThe second part of the experiment will start soon. When you are ready, please press spacebar twice to continue.\n "
                                   "Note that in the second part of the experiment, you will be either working with your partner or with a machine. \n"
                                   "After we asked, “Do you think human partner did the task, or the machine did the task?” Please answer quickly and accurately!")

# text1 = visual.TextStim(win1, text="恭喜完成第一部分实验，请休息片刻。\n当您准备好后，请按两次 空格 键以继续第二部分实验。\n"
#                                    "请注意在第二阶段实验过程中，\n"
#                                    "与你合作的对象可能是你的同伴，也可能是机器，\n"
#                                    "在我们询问“你觉得刚刚的任务是你的同伴完成的，\n还是机器完成的？”问题后，\n"
#                                    "请快速准确地完成回答！")
# text2 = visual.TextStim(win2, text="恭喜完成第一部分实验，请休息片刻。\n当您准备好后，请按两次 空格 键以继续第二部分实验。\n"
#                                    "请注意在第二阶段实验过程中，\n"
#                                    "与你合作的对象可能是你的同伴，也可能是机器，\n"
#                                    "在我们询问“你觉得刚刚的任务是你的同伴完成的，\n还是机器完成的？”问题后，\n"
#                                    "请快速准确地完成回答！")

text1.draw()
text2.draw()
win1.flip()
win2.flip()
#core.wait(6)
#core.quit()
key = event.waitKeys(keyList=["space","escape"])
if key[0] == "escape":
    core.quit()
key = event.waitKeys(keyList=["space","escape"])
if key[0] == "escape":
    core.quit()
key = event.waitKeys(keyList=["space","escape"])
if key[0] == "escape":
    core.quit()
key = event.waitKeys(keyList=["space","escape"])
if key[0] == "escape":
    core.quit()
text1 = visual.TextStim(win1, text="The second part will start soon.")
text2 = visual.TextStim(win2, text="The second part will start soon.")
# text1 = visual.TextStim(win1, text="第二部分正式实验将马上开始")
# text2 = visual.TextStim(win2, text="第二部分正式实验将马上开始")
text1.draw()
text2.draw()
win1.flip()
win2.flip()
core.wait(2)
#since = time.time()
win1.flip()
win2.flip()
core.wait(1)

# Part 2 Experiment: parameter setting
total_l = 16
factor = int(int(total_l)/16)

# Formal experimental setting
# n_block is supposed to be 20
n_block = 20
# Test experimental setting
# n_block = 8

# Formal experimental setting
real_trials1 = [BR1, BL1, YR1, YL1] * 4 * factor
real_trials2 = [BR2, BL2, YR2, YL2] * 4 * factor

# Test experimental setting
# real_trials1 = [BR1, BL1, YR1, YL1] * 1 * factor
# real_trials2 = [BR2, BL2, YR2, YL2] * 1 * factor

start_fakes = [0]*n_block

# Formal experimental setting
random_end_1 = [total_l,total_l,total_l,total_l,total_l,0]
random_end_2 = [total_l,total_l,total_l,total_l,total_l,0]
random_end_3 = [total_l,total_l,total_l,total_l,total_l,0]

# Test experimental setting
# random_end_1 = [total_l,0]
# random_end_2 = [total_l,0]
# random_end_3 = [total_l,0]
random.shuffle(random_end_1)
random.shuffle(random_end_2)
random.shuffle(random_end_3)

end_fakes = [0,0]+random_end_1+random_end_2+random_end_3
# all_rts = []
if len(ada_rts) == 0:
    print('Wrong adaptive record of the human reaction times!')
    core.quit()

# from fitter import Fitter
# f = Fitter(np.array(ada_rts), distributions=['norm'])
# f.fit()
# HUMANLIKE_RT_MEAN = f.fitted_param['norm'][0]
# HUMANLIKE_RT_STD = f.fitted_param['norm'][1]
# print(HUMANLIKE_RT_MEAN,HUMANLIKE_RT_STD)

HUMANLIKE_RT_MEAN = np.array(ada_rts).mean()
HUMANLIKE_RT_STD = np.array(ada_rts).std()
print(HUMANLIKE_RT_MEAN,HUMANLIKE_RT_STD)

mu_0 = 0.4
#mu_0 = 0.2
adaptive_rt_mean = []
adaptive_rt_std = []
for i in range(n_block-2-3):
    adaptive_rt_mean.append(HUMANLIKE_RT_MEAN+mu_0-i/(n_block-5-1)*mu_0)
    adaptive_rt_std.append(HUMANLIKE_RT_STD-(n_block-5-1-i)/(n_block-5-1)*HUMANLIKE_RT_STD)

start_block = 0
rest_time = 300
#main_experiment(logfile,total_l,n_block,start_block,start_fakes,end_fakes,all_rts,real_trials1,real_trials2, rest_time)

since = time.time()

# Part 2 Experiment: save the logfile templates
columns = ["timestamp",
    "experiment_ID",
    "block_ID",
    "stimulus_ID",
    "subject",
    "key_press",
    "rt",
    "fake_human_rt",
    "trial_stim",
    "fake_or_not",
    "UNIX_time",
    "wrong_type"]

# logfile dataframe
logfile = pd.DataFrame(columns = columns)
# judge_human_or_not dataframe
judge_human_or_not = pd.DataFrame(
    columns=['exp_ID', 'block_ID', 'P1_human_or_not', 'P2_human_or_not', 'label_human_or_not','P1_reaction_time','P2_reaction_time'])

#Part 2 Experiment: main code of the second part of the experiment
human_machine_flag = 0

for loop in range(n_block):
    # parallel.setData(0)
    # time.sleep(0.5)
    # parallel.setData(1)
    # time.sleep(0.5)
    block_ID = loop + start_block + 1
    # 每个loop的reaction time
    rts = []

    # 随机打乱order1和order2
    order1 = real_trials1
    order2 = real_trials2
    random_index = list(range(len(order1)))
    random.shuffle(random_index)
    new_order1 = []
    new_order2 = []
    for i in range(len(random_index)):
        new_order1.append(order1[random_index[i]])
        new_order2.append(order2[random_index[i]])
    order1 = new_order1
    order2 = new_order2

    human_iters = [1] * int(total_l)
    start_fake = int(start_fakes[loop])
    end_fake = int(end_fakes[loop])
    human_iters[start_fake:end_fake] = [0] * (end_fake - start_fake)
    human_flag = 'y'
    if start_fake != end_fake:
        # HUMANLIKE_RT_MEAN = np.array(ada_rts).mean()
        # HUMANLIKE_RT_STD = np.array(ada_rts).std()
        # from fitter import Fitter
        # f = Fitter(np.array(ada_rts), distributions=['norm'])
        # f.fit()
        # HUMANLIKE_RT_MEAN = f.fitted_param['norm'][0]
        # HUMANLIKE_RT_STD = f.fitted_param['norm'][1]
        human_flag = 'n'
        human_machine_flag += 1

    # define stopwatch
    stopwatch = core.Clock()

    # if human_flag=='y':
    #     parallel.setData(0)
    #     time.sleep(0.5)
    #     parallel.setData(2)
    #     time.sleep(0.5)
    # else:
    #     parallel.setData(0)
    #     time.sleep(0.5)
    #     parallel.setData(3)
    #     time.sleep(0.5)

## Experiment block loop
    for idx in range(len(order1)):

        human_or_not = human_iters[idx]
        stim1 = order1[idx]
        stim2 = order2[idx]
        f_cross1.draw(win1)
        f_cross2.draw(win2)
        win1.flip()
        win2.flip()
        core.wait(1)

        if not human_or_not and stim1 in [YR1, YL1]:
            # print(human_machine_flag)
            HUMANLIKE_RT_MEAN = adaptive_rt_mean[human_machine_flag-1]
            HUMANLIKE_RT_STD = adaptive_rt_std[human_machine_flag-1]
            fake_human_rt = np.random.uniform(HUMANLIKE_RT_MEAN - HUMANLIKE_RT_STD,
                                                HUMANLIKE_RT_MEAN + HUMANLIKE_RT_STD)
            stim1.draw(win1)
            stim2.draw(win2)

            win1.flip()
            win2.flip()

            stopwatch.reset()
            key = event.waitKeys(keyList=["w", "p", "escape"], maxWait=(fake_human_rt))
            rt = stopwatch.getTime()

            if key == None:
                win1.flip()
                stopwatch.reset()
                key = event.waitKeys(keyList=["w", 'p', "escape"], maxWait=(2.0 - fake_human_rt))
                rt1 = stopwatch.getTime()
                rt = rt1 + rt
            elif key[0] == 'w':
                win2.flip()
                core.wait(fake_human_rt - rt)

            win1.flip()
            win2.flip()
            core.wait(1)

            if stim1 == YR1:
                trial_stim = "YR"
            elif stim1 == YL1:
                trial_stim = "YL"

            if key == None:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": P2_ID,
                    "key_press": "none",
                    "rt": 'none',
                    "fake_human_rt": round(fake_human_rt, 4),
                    "trial_stim": trial_stim,
                    "fake_or_not": True,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'Not_press'},index=[0])], ignore_index=True)
            elif key[0] == "w":
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": P2_ID,
                    "key_press": "w",
                    "rt": round(rt, 4),
                    "fake_human_rt": round(fake_human_rt, 4),
                    "trial_stim": trial_stim,
                    "fake_or_not": True,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'none'},index=[0])], ignore_index=True)
            elif key[0]=='escape':
                core.quit()
            else:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": P2_ID,
                    "key_press": key[0],
                    "rt": round(rt, 4),
                    "fake_human_rt": round(fake_human_rt, 4),
                    "trial_stim": trial_stim,
                    "fake_or_not": True,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'Wrong_press'},index=[0])], ignore_index=True)

        else:
            stim1.draw(win1)
            stim2.draw(win2)
            win1.flip()
            win2.flip()
            # reset stopwatch and start recording
            stopwatch.reset()
            # wait for the participant to press W or P or esc
            key = event.waitKeys(keyList=["w", "p", "escape"], maxWait=(2.0))
            rt = stopwatch.getTime()
            # black screen for 1 second
            win1.flip()
            win2.flip()
            core.wait(1)

            if stim1 == BR1:
                trial_stim = "BR"
                agent_type = 'B'
                CAT = P1_ID
            if stim1 == BL1:
                trial_stim = "BL"
                agent_type = 'B'
                CAT = P1_ID
            if stim1 == YR1:
                trial_stim = "YR"
                agent_type = 'Y'
                CAT = P2_ID
            if stim1 == YL1:
                trial_stim = "YL"
                agent_type = 'Y'
                CAT = P2_ID

            # if participant did not press anything within 1.5 seconds, recod "none" key press
            if key == None:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": CAT,
                    "key_press": "none",
                    "rt": 'none',
                    "fake_human_rt": "none",
                    "trial_stim": trial_stim,
                    "fake_or_not": False,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'Not_press'
                },index=[0])], ignore_index=True)
            elif key[0] == "escape":
                core.quit()
            elif key[0] == "w" and trial_stim in ['YL', 'YR']:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": CAT,
                    "key_press": key[0],
                    "rt": round(rt, 4),
                    "fake_human_rt": "none",
                    "trial_stim": trial_stim,
                    "fake_or_not": False,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'none'
                },index=[0])], ignore_index=True)
            elif key[0] == "w" and trial_stim in ['BL', 'BR']:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": CAT,
                    "key_press": key[0],
                    "rt": round(rt, 4),
                    "fake_human_rt": "none",
                    "trial_stim": trial_stim,
                    "fake_or_not": False,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'Wrong_press'
                },index=[0])], ignore_index=True)
            elif key[0] == "p" and trial_stim in ['BL', 'BR']:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": CAT,
                    "key_press": key[0],
                    "rt": round(rt, 4),
                    "fake_human_rt": "none",
                    "trial_stim": trial_stim,
                    "fake_or_not": False,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'none'
                },index=[0])], ignore_index=True)
            elif key[0] == "p" and trial_stim in ['YL', 'YR']:
                logfile = pd.concat([logfile,pd.DataFrame({
                    "timestamp": data.getDateStr(),
                    "experiment_ID": exp_ID,
                    "block_ID": block_ID,
                    "stimulus_ID": idx + 1,
                    "subject": CAT,
                    "key_press": key[0],
                    "rt": round(rt, 4),
                    "fake_human_rt": "none",
                    "trial_stim": trial_stim,
                    "fake_or_not": False,
                    "UNIX_time": round(time.time(), 4),
                    "wrong_type": 'Wrong_press'
                },index=[0])], ignore_index=True)

    # parallel.setData(0)
    # time.sleep(0.5)
    # parallel.setData(4)
    # time.sleep(0.5)

    # random_time = random.uniform(15, 20)
    # core.wait(random_time / 2)

    # prepare P1 question text
    # text2 = visual.TextStim(win2,
    #                         text="Good job! \n Do you think the test just completed is completed by your partner or machine? \n "
    #                                 "Please press y buttion if you think the test is completed by your partner \n Please press n buttion if you think the test is completed by machine.")
    # text1 = visual.TextStim(win1, text="Good job! \n Please wait for a second.")

    # text1 = visual.TextStim(win2,text="Good job! \n Do you think the test just completed is completed by your partner or machine? \n\n "
    #                              "Participant 1 please press y buttion if you think the test is completed by your partner \n Please press n buttion if you think the test is completed by machine.")
    # text2 = visual.TextStim(win1,text="Good job! \n Do you think the test just completed is completed by your partner or machine? \n\n "
    #                              "Participant 2 please press a buttion if you think the test is completed by your partner \n Please press b buttion if you think the test is completed by machine.")

    #导语换成图片
    # text1 = visual.TextStim(win2,
    #                         text="你认为刚刚的任务是由你的同伴完成，\n"
    #                              "还是机器完成?\n"
    #                              "如果你认为是由你的同伴完成，请按y键\n如果你认为是由机器完成，请按n键。")
    # text2 = visual.TextStim(win1,
    #                         text="你认为刚刚的任务是由你的同伴完成，\n"
    #                              "还是机器完成?\n"
    #                              "如果你认为是由你的同伴完成，请按a键\n如果你认为是由机器完成，请按b键。")
    #
    # # text1 = visual.TextStim(win1, text = "Welcome to the experiment! \n {} please sit to the right of the computer, and place your right index finger on the P button. \n {} please sit on the left and place your left index finger on the W button. \n {} Press spacebar to continue.".format(P1_nn, P2_nn,P2_nn))
    # # text2 = visual.TextStim(win2, text = "Welcome to the experiment! \n {} please sit to the right of the computer, and place your right index finger on the P button. \n {} please sit on the left and place your left index finger on the W button. \n {} Press spacebar to continue.".format(P1_nn, P2_nn,P2_nn))
    #
    # text1.draw()
    # text2.draw()

    question1.draw()
    question2.draw()
    win1.flip()
    win2.flip()

    rt1_press, rt2_press = None,None
    stopwatch.reset()
    temp_key_1 = 0
    temp_key_2 = 0
    key = event.waitKeys(keyList=["a","s","k","l",'escape'],maxWait=(6.0))
    if key==None:
        print('too slow')
    elif key[0] == "escape":
        core.quit()
    elif key[0] in ['a','s']:
        temp_key_1 = 1
        p1_answer = key[0]
        rt1_press = stopwatch.getTime()
        question1.draw()
        win2.flip()
    elif key[0] in ['k','l']:
        temp_key_1 = 2
        p2_answer = key[0]
        rt2_press = stopwatch.getTime()
        question2.draw()
        win1.flip()

    if rt1_press==None and rt2_press == None:
        press_rt = 6
    elif rt1_press==None and rt2_press != None:
        press_rt = rt2_press
    elif rt1_press!=None and rt2_press == None:
        press_rt = rt1_press
    else:
        press_rt = max([rt1_press,rt2_press])

    key = event.waitKeys(keyList=["a","s","k","l",'escape'],maxWait=(6-press_rt))
    if key == None:
        print('too slow')
    elif key[0] == "escape":
        core.quit()
    elif key[0] in ['a', 's']:
        temp_key_2 = 1
        p1_answer = key[0]
        rt1_press = stopwatch.getTime()
        question1.draw()
        win2.flip()

    elif key[0] in ['k', 'l']:
        temp_key_2 = 2
        p2_answer = key[0]
        rt2_press = stopwatch.getTime()
        question2.draw()
        win1.flip()

    print(rt1_press,rt2_press)
    if temp_key_1 == temp_key_2:
        p1_answer = None
        p2_answer = None
        if temp_key_2==1:
            core.wait(6 - rt1_press)
        elif temp_key_2==2:
            core.wait(6 - rt2_press)
    elif rt1_press == None and rt2_press == None:
        press_rt = 6
        p1_answer = None
        p2_answer = None
    elif rt1_press == None and rt2_press != None:
        press_rt = 6
        p1_answer = None
    elif rt1_press != None and rt2_press == None:
        press_rt = 6
        p2_answer = None
    else:
        press_rt = max([rt1_press, rt2_press])
        core.wait(6 - press_rt)

    win1.flip()
    win2.flip()
    # parallel.setData(0)
    # time.sleep(0.5)
    # parallel.setData(5)
    # time.sleep(0.5)

    judge_human_or_not = pd.concat([judge_human_or_not,pd.DataFrame({
                            'exp_ID': exp_ID, 'block_ID': block_ID,
                            'P1_human_or_not': p1_answer, 'P2_human_or_not': p2_answer,
                            'label_human_or_not': human_flag,
                            'P1_reaction_time': rt1_press, 'P2_reaction_time': rt2_press}
                            ,index=[0])], ignore_index=True)
    # filename = r"logfiles\{}_{}_{}.csv".format('Human_or_not', exp_ID, block_ID)
    # judge_human_or_not.to_csv(filename)

    filename = r"logfiles\{}_{}_{}.csv".format(data.getDateStr(), 'human_or_not', exp_ID)
    judge_human_or_not.to_csv(filename)

    ### Saving logfile ###
    # logfilename
    # logfilename = r"logfiles\{}_{}_with_{}_trials.csv".format(data.getDateStr(), exp_ID, block_ID)
    logfilename = r"logfiles\{}_{}_with_{}_blocks.csv".format(data.getDateStr(), exp_ID, block_ID)
    logfile.to_csv(logfilename)

    if loop == n_block - 1:
        ### Saving judge_human_or_not file ###
        filename = r"logfiles\final_{}_{}_{}.csv".format(data.getDateStr(), 'human_or_not', exp_ID)
        judge_human_or_not.to_csv(filename)

        ### Saving logfile ###
        # logfilename
        # logfilename = r"logfiles\final_{}_{}_with_{}_trials.csv".format(data.getDateStr(), exp_ID, block_ID)
        logfilename = r"logfiles\final_{}_{}_with_{}_blocks.csv".format(data.getDateStr(), exp_ID, block_ID)
        logfile.to_csv(logfilename)

        adafilename = r"logfiles\adaptive_rt_mean_{}_{}.npy".format(data.getDateStr(), exp_ID)
        np.save(adafilename,np.array(adaptive_rt_mean))
        adafilename = r"logfiles\adaptive_rt_std_{}_{}.npy".format(data.getDateStr(), exp_ID)
        np.save(adafilename, np.array(adaptive_rt_std))

        p2filename = r"logfiles\p2_rt_{}_{}.npy".format(data.getDateStr(), exp_ID)
        np.save(p2filename, np.array(p2_rts))

        text1 = visual.TextStim(win1, text="All the experiments are over! \nSincerely thank you for your participation!")
        text2 = visual.TextStim(win2, text="All the experiments are over! \nSincerely thank you for your participation!")
        # text1 = visual.TextStim(win1, text="全部实验已经结束! \n由衷感谢您的参与!")
        # text2 = visual.TextStim(win2, text="全部实验已经结束! \n由衷感谢您的参与!")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(6)
        core.quit()

    random_time = random.uniform(15, 20)
    core.wait(random_time-press_rt)
    # text1.draw()
    # text2.draw()
    win1.flip()
    win2.flip()
    core.wait(2)

    # prepare P2 question text
    # text1 = visual.TextStim(win1,
    #                         text="Good job! \n Do you think the test just completed is completed by your partner or machine? \n "
    #                                 "Please press y buttion if you think the test is completed by your partner \n Please press n buttion if you think the test is completed by machine.")
    # text2 = visual.TextStim(win2, text="Good job! \n Please wait for a second.")
    # # text1 = visual.TextStim(win1, text = "Welcome to the experiment! \n {} please sit to the right of the computer, and place your right index finger on the P button. \n {} please sit on the left and place your left index finger on the W button. \n {} Press spacebar to continue.".format(P1_nn, P2_nn,P2_nn))
    # # text2 = visual.TextStim(win2, text = "Welcome to the experiment! \n {} please sit to the right of the computer, and place your right index finger on the P button. \n {} please sit on the left and place your left index finger on the W button. \n {} Press spacebar to continue.".format(P1_nn, P2_nn,P2_nn))
    #
    # text1.draw()
    # text2.draw()
    # win1.flip()
    # win2.flip()
    # key = event.waitKeys(keyList=["y", "n", 'escape'])
    # if key[0] == "escape":
    #     core.quit()
    # p2_answer = key[0]

    if time.time() - since >= rest_time:
        text1 = visual.TextStim(win1,
                                text="Please rest for a moment. \n When you and your partner are ready, press spacebar once to continue the experiment.")
        text2 = visual.TextStim(win2,
                                text="Please rest for a moment. \n When you and your partner are ready, press spacebar once to continue the experiment.")
        # text1 = visual.TextStim(win1,
        #                         text="请休息片刻。\n当您和同伴准备好后，请按一次空格键继续实验。")
        # text2 = visual.TextStim(win2,
        #                         text="请休息片刻。\n当您和同伴准备好后，请按一次空格键继续实验。")

        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        key = event.waitKeys(keyList=["space",'escape'])
        if key[0]=='escape':
            core.quit()
        key = event.waitKeys(keyList=["space", 'escape'])
        if key[0] == 'escape':
            core.quit()
        text1 = visual.TextStim(win1, text="The experiment continues soon.")
        text2 = visual.TextStim(win2, text="The experiment continues soon.")
        # text1 = visual.TextStim(win1, text="实验马上继续")
        # text2 = visual.TextStim(win2, text="实验马上继续")
        text1.draw()
        text2.draw()
        win1.flip()
        win2.flip()
        core.wait(2)
        since = time.time()
        win1.flip()
        win2.flip()
        core.wait(1)
        continue

    # random_time = random.uniform(15, 20)
    win1.flip()
    win2.flip()
    # core.wait(random_time / 2)
    core.wait(2)
    text1 = visual.TextStim(win1, text="The next block will begin soon.")
    text2 = visual.TextStim(win2, text="The next block will begin soon.")
    # text1 = visual.TextStim(win1, text="下一个试次马上开始")
    # text2 = visual.TextStim(win2, text="下一个试次马上开始")
    text1.draw()
    text2.draw()
    win1.flip()
    win2.flip()
    core.wait(2)
    win1.flip()
    win2.flip()
    core.wait(1)
    # print(all_rts)
