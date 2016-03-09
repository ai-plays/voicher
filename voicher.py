import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
import os


def changeWavSamplerate():
	data, samplerate = sf.read("in.wav")

	print data.shape
	print samplerate
	samplerate = int(samplerate * 1.5)


	sf.write("out.wav", data, samplerate)
	os.system("afplay out.wav")

	plt.plot(data)
	plt.show()


def recordEditPlay():
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


def recordAndEdit():
	fs = 44100
	sd.default.samplerate = fs
	sd.default.channels = 2

	print "start recording..."
	duration = 5  # seconds
	myRec = sd.rec(duration * fs)
	sd.wait()

	print "start playing..."
	sd.play(myRec, fs * 2)
	sd.wait()


# for i, one in enumerate(data):
# 	one[0] *= 2
# 	one[1] *= 2




if __name__ == "__main__":
	# recordEditPlay()
	recordAndEdit()








