import os
from speaker import speaker
from voice_recognition import listen


def computer_off():
    speaker.say("Are you sure?")
    speaker.runAndWait()
    res = listen()
    print(res)
    if res == "yes" or res == "yeah" or res == "yup":
        os.system("shutdown -P now")
    else:
        return
