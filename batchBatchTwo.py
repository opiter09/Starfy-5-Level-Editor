import os
import subprocess

text = open("roomList.txt", "rt").read()
count = -1

for root, dirs, files in os.walk("./mapooFiles"):
    for file in files:
        if (int(file[0:4]) >= 571) and (int(file[0:4]) <= 2076):
            count = count + 1
            subprocess.run([ "lzss.exe", "-d", os.path.join(root, file) ])
            
            if (int(file[0:4]) <= 1147):
                os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[0:4] + " [" + text.split("\n")[count] + "].bin")
            else:
                obj = open("objectsList.txt", "rt")
                splits = obj.read().split("\n")
                for line in splits:
                    if (int(line.split(" ")[1]) == int(file[0:4])):
                        os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[0:4] + "_O_[" + line.split(" ")[0] + "].bin")
                        break
                obj.close()