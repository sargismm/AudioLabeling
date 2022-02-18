Imagine you have a folder with audio files and you want to label them as noisy / clean.

You need to write a script that will play the audio files one by one, after playing each file wait for user input - ‘n’ (for noisy) or ‘c’ (for clean). Once the appropriate key is pressed proceed to the next file. Once all the files are processed export a json file where you have the file names and corresponding labels.

To run audio_labeling.py file:

**pip install playsound**

if

       Error 263 for command:

       open Typing.wav
        
       The specified device is not open or is not recognized by MCI.

appears do the following: 

**pip uninstall playsound**

**pip install playsound==1.2.2**
