import os
import subprocess

text = open("roomList.txt", "rt").read()
count = -1
for root, dirs, files in os.walk("./mapooFiles"):
    for file in files:
        if (int(file[0:4]) >= 570) and (int(file[0:4]) <= 2075):
            count = count + 1
            subprocess.run([ "lzss.exe", "-d", os.path.join(root, file) ])
            if (int(file[0:4]) <= 1146):
                os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[0:4] + " [" + text.split("\n")[count] + "].bin")