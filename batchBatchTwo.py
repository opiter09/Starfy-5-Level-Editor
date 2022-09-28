import os
import subprocess

text = open("roomList.txt", "rt").read()
for root, dirs, files in os.walk("./mapooFiles"):
    for file in files:
        if (int(file[0:4]) >= 569) and (int(file[0:4]) <= 1125):
            subprocess.run([ "lzss.exe", "-d", os.path.join(root, file)])
            os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[0:4] + " [" + text.split("\n")[int(file[0:4]) - 569] + "].bin")