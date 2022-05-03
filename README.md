# VoiceAssistant
A voice assistant made with Python.

## How to use?

### Initial Setup

First install dependencies.
---
    pip install -r requirements.txt
---
Go to main.py and edit the lines that say 
---
    # assistant.train_model()
    # assistant.save_model()
---
To
---
    assistant.train_model()
    assistant.save_model()
---
Then run the program. After it's done training, close the program and change the lines of code back.

### Triggering Assistant
To trigger the assistant, say "Hey sam!"

### Setting up weather
To setup the weather, create a new file called secret_weather_data.txt.
Then grab the url for your city from weather.com and put it into the file.
Example: https://weather.com/weather/today/l/96f2f84af9a5f5d452eb0574d4e4d8a840c71b05e22264ebdc0056433a642c84
(This weather link is for New York)

## Credits
- [mak448a](https://mak448a.github.io)
- [NeuralNine](https://www.neuralnine.com)
