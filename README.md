# voicher
python voice changer


[Audio File Structure]
https://www.zhihu.com/question/29261034
http://www.cs.bu.edu/courses/cs101b1/slides/CS101.Lect28.Python.Audio.ppt.pdf


[Format Conversion]
Convert audio file to .wav, process it, and then convert it to your output format.
	sox nuo.mp3 nuo.wav
	ffmpeg
	mpg123


[Libraries]
http://nbviewer.jupyter.org/github/mgeier/python-audio/blob/master/audio-files/index.ipynb

#PySoundFile: 
http://pysoundfile.readthedocs.org/en/0.8.1/
Additional Notes:
	1. download miniconda(python3.5) from http://conda.pydata.org/miniconda.html
	2. manually configure .zshrc to modify PATH, if you use zsh
	3. sublime python configuration: http://blog.shank.in/post/26276497763/sublime-text-how-to-change-the-version-of-python
	4. may change the file "python" in miniconda's bin to another name, then "python3" refers to python3.5 while "python" refers to your previous version
		sometimes, when using pip to install things, may need to rename it back;
	5. matplotlib issue: http://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python



Steps:
1. learn PySoundFile API
2. python play read-in sound file
3. non-real-time voice changer
4. python record voice
5. real-time voice changer



