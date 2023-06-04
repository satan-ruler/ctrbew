input_file = "testspeak.pcm"
output_file = "testspeak_cut.pcm"

with open(input_file, "rb") as infile:
    data = infile.read(2549760)

with open(output_file, "wb") as outfile:
    outfile.write(data)

print("截取完成，已保存为", output_file)

