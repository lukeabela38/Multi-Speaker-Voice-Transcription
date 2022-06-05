import os
import re
import speech_recognition as sr
import glob
from pydub import AudioSegment
from pydub.silence import split_on_silence
from punctuation import punctuate


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def write2text(text, filename = "outputs/test.txt"):
    with open(filename, "a") as f:
        f.write(text)

class Transcription():
    def __init__(self):
        self.r = sr.Recognizer()
        self.location = os.getcwd()
    
    def _listen(self, input_file):
        with sr.AudioFile(input_file) as source:
            try:
                text = self.r.record(source)
                text = self.r.recognize_google(text).capitalize()
            except:
                text = "..."  
        return text

    def _large_listen(self, input_file):

        listoftexts = []
        sound = AudioSegment.from_wav(input_file)
        chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500)

        for i, audio_chunk in enumerate(chunks, start = 1):
            chunk_filename = os.path.join("outputs_temp/", f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            text = self._listen(chunk_filename)
            listoftexts.append([i, punctuate(text)])

        return listoftexts

    def _files2listen(self):

        files = []
        for name in glob.glob(self.location + "/inputs_split/*.wav"):
            files.append(name)
        
        files.sort(key=natural_keys)
        for file in files:
            listoftexts = self._large_listen(file)
            speaker = file.split("/")[3].split("_")[2][:2]

            text = "Speaker " + str(speaker) + ":" + "\t" + listoftexts[0][1] +"\n"
            write2text(text=text)

if __name__ == "__main__":

    Transcription()._files2listen()

"""
    text = Transcription()._listen("inputs_processed/test.wav")
    print("")
    print("TEXT: ")
    print(text)
    print("")
    
    text = Transcription()._large_listen("inputs_processed/test.wav")
    print("")
    print("TEXT: ")
    print(text)
    print("")
"""
