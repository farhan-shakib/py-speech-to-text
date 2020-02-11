from pydub import AudioSegment
import os, math

def chunker():
    #file path
    path = './file_wav/1.wav'
    #make directory for chunks
    try:
        os.mkdir('chunks')
    except:
        pass

    #load audio
    audio = AudioSegment.from_wav(path)

    #calculate duration
    duration = len(audio)
    chunk_duration = 25000
    no_of_chunks = math.ceil(duration/chunk_duration);

    #create chunks of 10 seconds
    init = 0
    last = chunk_duration
    silent_chunk = AudioSegment.silent(duration = 2500)
    try:
        print("[segmentation started]")
        for i in range(no_of_chunks):
            chunk = silent_chunk + audio[init:last] + silent_chunk
            path = 'chunks/chunk' + str(i+1) + '.wav'
            chunk.export(path, format='wav')
            
            duration -= chunk_duration
            init = last + 1
            if duration > chunk_duration:
                last += chunk_duration
            else:
                last = duration
        print("[segmentation ended successfully]")
    except:
        print("[error occured in segmentation]")