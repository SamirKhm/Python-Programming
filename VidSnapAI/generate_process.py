# This file looks for new folder insdie user uploads and converts them to reel if they are not already converted
import os
import time
from text_to_audio import text_to_speech_file
def text_to_audio(folder):
    with open(f"user_uploads/{folder}/description.txt") as f:
        text=f.read()
    print(text,folder)
    # text_to_speech_file(text,done_folder)

def create_reel(folder):
    pass

if __name__=="__main__":
    while(True):
        with open("done.txt","r") as f:
            done_folders=f.readlines()
        done_folders=[f.strip() for f in done_folders]
        
        folders=os.listdir("user_uploads")    
        
        for folder in folders:
            if (folder not in done_folders):
                text_to_audio(folder) # Generate audio from description.txt
                create_reel(folder)# This will convert the images and audio.mp3 inside folder to reel
                with open("Done.txt","a") as f:
                    f.write(folder+"\n")

        time.sleep(4)