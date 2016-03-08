import soundfile as sf
import matplotlib.pyplot as plt
import random

data, samplerate = sf.read('test.wav')

print(data.shape)

plt.plot(data);

print(data[:2])

for i, one in enumerate(data):
	one[0] = 0
	#one[1] = 0

sf.write('1.wav', data, samplerate)

a = input("1111")
print(a)
