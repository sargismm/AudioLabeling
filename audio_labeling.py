import json
from datetime import datetime
import playsound as ps
import os as os

# Audio samples directory
directory = './audio_samples/'
resultDict = {}

# Function to play the audio, wait for user input, and add values to directory
def labeling_func(filename):
    print("Playing audio: " + filename)
    ps.playsound(directory + filename)
    label = input("Type 'n' if " + filename + " was noisy. Type 'c' if " + filename + " was clean.\n").lower()
    while label != 'c' and label != 'n':
        print("Please select one of the options given")
        label = input().lower()
    if label == 'c':
        resultDict[filename] = "Clean"
    elif label == 'n':
        resultDict[filename] = "Noisy"


# Looping over the audio_samples
for audio_file in os.listdir(directory):
    labeling_func(audio_file)

# Creating results directory if needed
if not os.path.exists('./results'):
    os.mkdir('./results')

# Creating json file and writing results directory to it
filename = 'result_' + datetime.now().strftime("%Y%m%d%H%M%S") + '.json'
with open('./results/' + filename, 'w') as jsonfile:
    jsonfile.write(json.dumps(resultDict, indent=4))

