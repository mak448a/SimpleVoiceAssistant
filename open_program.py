from os import system
from speaker import speaker
from threading import Thread


def open_documents():
    x = Thread(target=system, args=("nautilus ~/Documents",))
    x.start()
    speaker.say("Here are your documents.")
    speaker.runAndWait()


def open_downloads():
    x = Thread(target=system, args=("nautilus ~/Downloads",))
    x.start()
    speaker.say("Here are your downloads.")
    speaker.runAndWait()


def open_pictures():
    x = Thread(target=system, args=("nautilus ~/Pictures",))
    x.start()
    speaker.say("Here are your pictures.")
    speaker.runAndWait()


def open_discord():
    x = Thread(target=system, args=("/home/aram/.downloaded programs/discord-0.0.17/Discord/Discord",))
    x.start()
    speaker.say("Opening Discord.")
    speaker.runAndWait()


def open_pycharm():
    x = Thread(target=system, args=("sh \"/home/aram/.downloaded programs/pycharm-community-2021.3.2/bin/pycharm.sh\"",))
    x.start()
    speaker.say("Opening Pie Charm.")
    speaker.runAndWait()


def open_firefox():
    x = Thread(target=system, args=("firefox",))
    x.start()
    speaker.say("Opening Fire Fox.")
    speaker.runAndWait()
