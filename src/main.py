# TODO: Main program loop 
# 
# load and process input audio file, 
# perform diarization to split into multiple files based on speakers,
# perform transcription on wav files
# combine transcriptions with speaker tags and write to final text file
import os
import glob
from processing import Processing
    
def main():

    location = os.getcwd()
    files = []

    for name in glob.glob(location + "/inputs/*.wav"):
        files.append(name)
    print(files)

    for input_file in files:
        file_split = input_file.split("/")
        file_split[2] = "inputs_processed"
        output_file = " ".join(file_split).replace(" ", "/")
        Processing()._process(input_file=input_file, output_file=output_file)

if __name__ == "__main__":
    main()