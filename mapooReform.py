import os
import glob
import subprocess
import shutil

for root, dirs, files in os.walk("./mapooFiles"):
    sortList = files
    sortList.sort()
    for file in sortList:
        if (file.endswith("].bin") == True) or ((int(file[0:4]) >= 1148) and (int(file[0:4]) <= 2076)):
            shutil.copy2("./mapooFiles/" + file, "./mapooFiles/temp_" + file)
            subprocess.run([ "lzss.exe", "-evn", "./mapooFiles/" + file ])

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
    sortList2 = files
    sortList2.sort()
    for file in sortList2:
        if (file.startswith("temp_") == False):
            data = open("./mapooFiles/" + file, "rb")
            new.write(data.read())
            data.close()

for root, dirs, files in os.walk("./mapooFiles"):
    sortList3 = files
    sortList3.sort()
    for file in sortList3:
        if (file.startswith("temp_") == False):
            if (file.endswith("].bin") == True) or ((int(file[0:4]) >= 1148) and (int(file[0:4]) <= 2076)):
                shutil.copy2("./mapooFiles/temp_" + file, "./mapooFiles/" + file)
                os.remove("./mapooFiles/temp_" + file)