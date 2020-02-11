#from os import path
from pydub import AudioSegment
import os

def toWav():
    # files
    os.mkdir('file_wav')                                                                         
    src = 'file_mp3/1.mp3'
    dst = 'file_wav/1.wav'
    # convert wav to mp3                                                            
    try:
        print("[conversion started]")
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        print("[conversion finished successfully]")
    except:
        print("[error occured in conversion]")