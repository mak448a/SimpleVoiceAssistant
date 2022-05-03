import sys

import vosk
import sounddevice as sd
import queue
import os

q = queue.Queue()
if not os.path.exists("model"):
	print("Please download a model for your language from https://alphacephei.com/vosk/models")
	print("and unpack as 'model' in the current folder.")
	sys.exit()
model = vosk.Model("model")
samplerate = 44100
device = None


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def listen():
    try:
        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                               channels=1, callback=callback):
            # print("Listening")
            # print('#' * 80)
            # print('Press Ctrl+C to stop the recording')
            # print('#' * 80)

            rec = vosk.KaldiRecognizer(model, samplerate)

            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    return result.split("\"")[3]
                # data = q.get()
                # if rec.AcceptWaveform(data):
                #     print("Result")
                #     print(rec.Result())
                # else:
                #     print("Partial")
                #     print(rec.PartialResult())

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    print("Listening")
    print(listen())
