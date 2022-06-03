from pyannote.audio import Pipeline

class Diarizer:
    def __init__(self):
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    def _diarize(self, input_file):
        diarization = self.pipeline(input_file)
        speakers = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            speakers.append([turn.start, turn.end, speaker]) # start time, end time, speaker
        return speakers

if __name__ == "__main__":
    speakers = Diarizer()._diarize("inputs/test.wav")
    print(speakers)