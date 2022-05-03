# import pyttsx3 as tts
#
# speaker = tts.init()
# speaker.setProperty("rate", 150)
# Uncomment if you want a female voice
# speaker.setProperty("voice", "en-us+f4")
# f1, f2, f3, f4, f5 for different pitches.
import os


def say(text: str):
    """
    Uses pyttsx3 to speak. If pyttsx3 failed, then it defaults to espeak.
    """
    if failed_import:
        os.system("espeak \"" + text + "\"")
    else:
        speaker.say(text)
        speaker.runAndWait()


class DummyEngine:
    def __init__(self):
        pass

    @staticmethod
    def say(text):
        say(text)

    def runAndWait(self):
        pass


try:
    import pyttsx3
    speaker = pyttsx3.init()
except OSError:
    failed_import = True
    speaker = DummyEngine()
