
1、原始音频文件testspeak.mp3
	- 该文件是从windows电脑中找到的
	- 内容为：如果能听到这段声音，证明您的扬声器工作正常，If you hear ...

2、查看mp文件格式
	- ffmpeg -i testspeak.mp3 -f null -
	- 得到信息如下:
		Input #0, mp3, from 'testspeak.mp3':
		  Metadata:
			  encoder         : Lavf58.20.100
				Duration: 00:00:13.35, start: 0.050113, bitrate: 70 kb/s
					Stream #0:0: Audio: mp3, 22050 Hz, stereo, fltp, 70 kb/s
					Stream mapping:
					  Stream #0:0 -> #0:0 (mp3 (mp3float) -> pcm_s16le (native))

3、将mp3转成pcm
	- ffmpeg -i testspeak.mp3 -f s16le -ar 48000 -ac 2 -acodec pcm_s16le testspeak.pcm

4、使用python截断pcm文件（为了得到整数帧, 3840的整数）
	- python3 cut_pcm.py

5、将cut以后的pcm转成opus
	- python3 convert_pcm_to_opus.py

6、opus目录下得到的sample-xxx.opus文件就是最终的opus文件，该文件可以给到客户端sample来播放

7、通过ffmpeg -i opus/sample-664.opus -f null - 来测试opus帧会提示opus/sample-664.opus: Invalid data found when processing input，这是正常现象

