import os
import glob
import subprocess

whole = open("mapoo.bin", "rb").read()
new = open("output_mapoo.bin", "ab")
new.write(whole[0:16])

previousOffset = int.from_bytes(whole[8:12], "little")
for i in range(3286):
    file = glob.glob("./mapooFiles/" + str(i).zfill(4) + "*")
    if (len(file) > 0):
        size = os.stat(file[0]).st_size
        newOffset = size + previousOffset
        previousOffset = newOffset
        new.write(newOffset.to_bytes(4, "little"))
    else:
        new.write(previousOffset.to_bytes(4, "little"))
    new.write(whole[(20 + (i * 8)):(24 + (i * 8))])
        
for root, dirs, files in os.walk("./mapooFiles"):
    sortList = files
    sortList.sort()
    for file in sortList:
        if (file.endswith("].bin") == True):
            subprocess.run([ "lzss.exe", "-evo", "./mapooFiles/" + file ])
        new.write(open("./mapooFiles/" + file, "rb").read())