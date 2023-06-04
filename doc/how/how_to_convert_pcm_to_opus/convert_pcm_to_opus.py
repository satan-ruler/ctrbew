# 这段代码可以将pcm转成opus，而且播放很正常

import opuslib
import os

# Set up the Opus encoder with CBR mode
encoder = opuslib.Encoder(48000, 2, opuslib.APPLICATION_AUDIO)
#encoder.set_bitrate(64000) # Set the bitrate to 64 kbps
#encoder.set_bitrate_range(64000, 64000)
#encoder.set_vbr(False) # Disable VBR mode

# Open the PCM file for reading
with open('testspeak_cut.pcm', 'rb') as pcm_file:

# Set up the Opus output file numbering counter
    opus_num = 1 

    # Loop through the PCM file, encoding each frame to Opus and saving to file
    while True:
        pcm_frame = pcm_file.read(3840) # Read 3840 bytes (960 samples) for each frame
        if not pcm_frame: # End of file
            break
        opus_frame = encoder.encode(pcm_frame, 960) # 960 samples per frame
        opus_filename = 'opus/sample-{:03d}.opus'.format(opus_num) # Format filename with 3-digit zero-padded index
        with open(opus_filename, 'wb') as opus_file:
            opus_file.write(opus_frame)
        opus_num += 1

