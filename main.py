from neuralintents import GenericAssistant
import sys
from voice_recognition import listen
import playsound
import open_program
from speaker import speaker
import random
# import os
import weather
import misc

# os.system('notify-send "Voice assistant has started."')


def main():
    def quit_program():
        bye = ["Bye! See you next time.", "Talk to you later!"]
        speaker.say(random.choice(bye))
        speaker.runAndWait()
        sys.exit()

    mappings = {
        "documents": open_program.open_documents,
        "downloads": open_program.open_downloads,
        "pictures": open_program.open_pictures,
        "discord": open_program.open_discord,
        "weather": weather.weather,
        "pycharm": open_program.open_pycharm,
        "computeroff": misc.computer_off,
        "firefox": open_program.open_firefox,
        "quit": quit_program
    }

    assistant = GenericAssistant('intents.json', intent_methods=mappings)

    # assistant.train_model()
    # assistant.save_model()
    assistant.load_model()

    while 1:
        wake_word = "hey sam"
        print("Listening for wake word...")
        user_input = listen()
        print("You said:", user_input)
        if not user_input.count(wake_word) > 0:
            continue
        else:
            playsound.playsound("wake.wav")

        print("Say something...")
        message = listen()
        print(message)
        if not message:
            speaker.say("What?")
            speaker.runAndWait()
            continue

        bot_response = assistant.request(message)

        if bot_response is not None:
            print("Sam: " + bot_response)
            speaker.say(bot_response)
            speaker.runAndWait()


if __name__ == "__main__":
    main()
