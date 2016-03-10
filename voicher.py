import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
import os
import numpy as np


def readEditWritePlayWav():
	data, samplerate = sf.read("in.wav")
	print data.shape
	print samplerate

	plt.plot(data)
	plt.show()

	samplerate = int(samplerate * 1.5)

	sf.write("out.wav", data, samplerate)
	os.system("afplay out.wav")



def recordEditPlay1():
	fs = 44100
	sd.default.samplerate = fs
	sd.default.channels = 2

	print "start recording..."
	duration = 5  # seconds
	myRec = sd.rec(duration * fs)
	sd.wait()	# wait until finish recording

	print "start playing..."
	sd.play(myRec)
	sd.wait()	# wait until finish playing

	print "start recording while playing..."
	myRec2 = sd.playrec(myRec)
	sd.wait()
	print "start playing mix..."
	sd.play(myRec2)
	sd.wait()


def recordEditPlay2():
	fs = 44100
	sd.default.samplerate = fs
	sd.default.channels = 2

	print "start recording..."
	duration = 10  # seconds
	myRec = sd.rec(duration * fs)
	sd.wait()

	print "start playing..."
	sd.play(myRec, int(fs * 1.5))
	sd.wait()


# for i, one in enumerate(data):
# 	one[0] *= 2
# 	one[1] *= 2


def PSOLA():
	data, samplerate = sf.read("in.wav")
	print data.shape
	print samplerate

	newData = np.zeros((data.shape[0] * 2, data.shape[1]))

	j = 0
	for i in range(data.shape[0]):
		newData[j] = data[i]
		newData[j+1] = data[i]
		j += 2

	# sd.play(data, samplerate)
	# sd.wait()

	sd.play(newData, samplerate * 2)
	sd.wait()




if __name__ == "__main__":
	# readEditWritePlayWav()
	# recordEditPlay1()
	# recordEditPlay2()

	PSOLA()







