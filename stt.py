import speech_recognition as sr 
import os
import shutil

def stt():
    r = sr.Recognizer()
    file_path = 'text/text.txt'

    #how many files to process
    os.chdir('chunks')
    file_no = len([name for name in os.listdir('.') if os.path.isfile(name)])
    os.chdir('..')

    try:
        print("[stt started]")
        for i in range(file_no):
            file = 'chunks/chunk' + str(i+1) + '.wav'
            print('processing ', file)
            
            audio = sr.AudioFile(file)  
            with audio as source:
                audio = r.record(source)

            try:
                with open(file_path, 'a') as f:
                        f.write(r.recognize_google(audio)+'\n\n')
            except:
                print("[probably no voice found in audio. it's normal.]")
        print("[stt ended successfully]")
    except:
        print("[erro occured in stt]")

    shutil.rmtree('chunks')
    shutil.rmtree('file_wav')