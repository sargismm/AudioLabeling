import json
from datetime import datetime
import playsound as ps
import os as os

directory = './audio_samples/'
resultDict = {}


def labeling_func(filename):
    print("Playing audio: " + filename)
    ps.playsound(directory + filename)
    label = input("Type 'n' if " + filename + " was noisy. Type 'c' if " + filename + " was clean.\n")
    while label != 'c' and label != 'n':
        print("Please select one of the options given")
        label = input()
    if label == 'c':
        resultDict[filename] = "Clean"
    elif label == 'n':
        resultDict[filename] = "Noisy"


for audio_file in os.listdir(directory):
    labeling_func(audio_file)

if not os.path.exists('./results'):
    os.mkdir('./results')
filename = 'result_' + datetime.now().strftime("%Y%m%d%H%M%S") + '.json'
with open('./results/' + filename, 'w') as jsonfile:
    jsonfile.write(json.dumps(resultDict, indent=4))

