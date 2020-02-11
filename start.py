import towav, chunker, stt
import time

print("[process started]")
time.sleep(2)
towav.toWav()
time.sleep(2)
chunker.chunker()
time.sleep(2)
stt.stt()
time.sleep(2)
print("[process finished]")