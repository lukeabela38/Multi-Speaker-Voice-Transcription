import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

class Transcription():
    def __init__(self):
        self.r = sr.Recognizer()
    
    def _listen(self, input_file):
        with sr.AudioFile(input_file) as source:
            text = self.r.record(source)  
        return self.r.recognize_google(text).capitalize()

    def _large_listen(self, input_file):

        listoftexts = []
        sound = AudioSegment.from_wav(input_file)
        chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500)

        for i, audio_chunk in enumerate(chunks, start = 1):
            chunk_filename = os.path.join("inputs_split/", f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            text = self._listen(chunk_filename)
            listoftexts.append([i, text])

        return listoftexts

if __name__ == "__main__":

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