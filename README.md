# voicher
python voice changer


## Audio File Structure:
https://www.zhihu.com/question/29261034   
http://www.cs.bu.edu/courses/cs101b1/slides/CS101.Lect28.Python.Audio.ppt.pdf  


##Format Conversion:
Convert audio file to .wav, process it, and then convert it to your output format.  
* `sox nuo.mp3 nuo.wav` 
* `ffmpeg ...`
* `mpg123 ...`


## Libraries:
http://nbviewer.jupyter.org/github/mgeier/python-audio/blob/master/audio-files/index.ipynb  

### PySoundFile:  
http://pysoundfile.readthedocs.org/en/0.8.1/  

### Additional Notes:
**use python2.7**:
	* use `pip2.7 install *`  
	* if sublime can not run successfully, just use terminal instead;  
**use python3.5**: 
	* download miniconda(python3.5) from http://conda.pydata.org/miniconda.html  
	* manually configure `.zshrc` to modify PATH, if you use zsh  
	* sublime python configuration: http://blog.shank.in/post/26276497763/sublime-text-how-to-change-the-version-of-python
	* may change the file "python" in miniconda's bin to another name, then "python3" refers to python3.5 while "python" refers to your previous version  
		sometimes, when using pip to install things, may need to rename it back;  
	* matplotlib issue: http://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python  
  
  
  

# Steps:  
* learn PySoundFile API  
* python play read-in sound file  
* non-real-time voice changer  
* python record voice  
* real-time voice changer  



