import soundfile as sf
import matplotlib.pyplot as plt
import random

data, samplerate = sf.read('test.wav')

print data.shape

plt.plot(data)
plt.show()

#print(data[:2])

#for i, one in enumerate(data):
	#one[0] = 0
	#one[1] = 0

#sf.write('2.wav', data, samplerate)

# plt.plot([1,2,3,1])
# plt.show()
