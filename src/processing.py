import librosa
import soundfile as sf

class Processing:
    def __init__(self):
        self.sr = 16000

    def _load(self, input_file):
        y, sr = librosa.load(input_file)
        return y, sr
    
    def _mono(self, y, sr):
        return librosa.to_mono(y), sr
    
    def _resample(self, y, sr, target_sr = 16000):
        return librosa.resample(y, orig_sr = sr, target_sr = target_sr), target_sr

    def _save(self, y, sr, output_file):
        sf.write(output_file, y, sr)

    def _process(self, input_file = "inputs/test.wav", output_file = "inputs_processed/test.wav"):
        y, sr = self._load(input_file=input_file)
        y, sr = self._mono(y, sr)
        y, sr = self._resample(y, sr)
        self._save(y, sr, output_file=output_file)

if __name__ == "__main__":
    Processing()._process()
