# TODO: Main program loop 
# 
# load and process input audio file, 
# perform diarization to split into multiple files based on speakers,
# perform transcription on wav files
# combine transcriptions with speaker tags and write to final text file
import os
import shutil
import time
import glob
from processing import Processing
from diarization import Diarizer
from transcription import Transcription

def main():

    folders = ["inputs_processed", "inputs_split", "plots", "outputs_temp"]

    for folder in folders:
        if os.path.exists(folder) != True:
            os.mkdir(folder)

    location = os.getcwd()
    files = []

    for name in glob.glob(location + "/inputs/*.wav"):
        files.append(name)
        print

    start = time.time()

    for input_file in files:
        file_split = input_file.split("/")
        file_split[2] = "inputs_processed"
        output_file = " ".join(file_split).replace(" ", "/")
        Processing()._process(input_file=input_file, output_file=output_file)
        Diarizer()._segmentFiles(input_file=input_file)
    Transcription()._files2listen()

    end = time.time()
    print("")
    print("Total Time: ", end - start)
    print("")

    for folder in folders:
        if os.path.exists(folder) == True:
            shutil.rmtree(folder)

if __name__ == "__main__":
    main()