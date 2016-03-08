import soundfile as sf
import matplotlib.pyplot as plt
import random
import os
import pyglet


data, samplerate = sf.read("in.wav")

print data.shape
print samplerate
samplerate = int(samplerate * 1.5)

# plt.plot(data)
# plt.show()




#for i, one in enumerate(data):
	#one[0] = 0
	#one[1] = 0





sf.write("out.wav", data, samplerate)
os.system("afplay out.wav")
