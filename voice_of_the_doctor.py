# Step 1a: setup text to speech--tts-model with (gtts )

import os 
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text,output_filepath):
    
    language ="en"
    
    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    
    audioobj.save(output_filepath)

input_text= "hey hello, how are you , we are going to create a ai bot which will asssist patient as a virtual doctor "
# text_to_speech_with_gtts_old(input_text=input_text,output_filepath="gtts_testing.mp3")

# Step 1b: setup text to speech--tts-model  with (elevenlabs)

import os
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
set_api_key(ELEVENLABS_API_KEY)

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    # client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text=input_text, output_filepath="elevenlabs_testing.mp3") 

#Step 2 : use model  for test output of the voice

import subprocess
import platform
def text_to_speech_with_gtts(input_text,output_filepath):
    
    language ="en"
    
    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Use ffplay with -loglevel quiet to suppress output
            subprocess.run(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', output_filepath], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text= "hey hello, how are you , we are going to create a ai bot which will asssist patient as a virtual doctor with new version and we are testing it now"
# text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    # client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Use ffplay with -loglevel quiet to suppress output
            subprocess.run(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', output_filepath], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3") 