import os
import sys
import wave
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pyannote.audio import Pipeline

class Diarizer:
    def __init__(self):
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
        self.location = os.getcwd() + "/inputs_split/"

    def _diarize(self, input_file):
        diarization = self.pipeline(input_file)
        speakers = []

        i = 0
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            t1 = turn.start*1000
            t2 = turn.end*1000
            speakers.append([i, t1, t2, speaker]) # start time, end time, speaker
            i = i + 1

        return speakers

    def _segment(self, input_file, speakers):
        audio = AudioSegment.from_wav(input_file)
        for speaker in speakers:
            name = self.location + str(speaker[0]) + "_" + str(speaker[3]) + ".wav"
            print(speaker)
            audio[speaker[1]:speaker[2]].export(name, format="wav")

    def _segmentFiles(self, input_file):
        speakers = self._diarize(input_file=input_file)
        self._segment(input_file=input_file, speakers=speakers)

    def _plotDiarizarion(self, input_file):

        speakers = self._diarize(input_file=input_file)
        points_to_plot = []
        for speaker in speakers:
            points_to_plot.append(speaker[1])
            points_to_plot.append(speaker[2])
        points_to_plot = np.array(points_to_plot)

        spf = wave.open(input_file, "r")
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, dtype = "int16")
        y_min = np.min(signal)
        y_max = np.max(signal)

        x = points_to_plot*8
        plt.figure(1)
        plt.title("Diarized Signal Wave")
        plt.plot(signal)
        plt.vlines(x = x, ymin=y_min, ymax=y_max, colors="r")
        plt.savefig("plots/Diarization_plot.png")


        
if __name__ == "__main__":
    Diarizer()._segmentFiles("inputs_processed/test.wav")
