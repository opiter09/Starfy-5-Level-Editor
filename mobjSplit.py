file = open("mobj.bin", "rb").read()
import os
try:
    os.mkdir("mobjFiles")
except OSError as error:
    pass

import math
for i in range(((11968 - 16) // 8) - 10):
    oldOffset = int.from_bytes(file[(16 + (i * 8)):(20 + (i * 8))], "little")
    newOffset = int.from_bytes(file[(24 + (i * 8)):(28 + (i * 8))], "little")
    
    if (i == ((11968 - 16) // 8) - 11):
        newOffset = os.stat("mobj.bin").st_size

    extension = ".bin"
    try:
        extension = "." + file[(oldOffset + 5):(oldOffset + 9)].decode("UTF-8")[::-1]
    except ValueError as error:
        pass
    
    
    if (oldOffset != newOffset):
        try:
            new = open("mobjFiles/" + str(i).zfill(4) + "_" + str(math.floor(i / 4)) + extension, "wb")
        except ValueError as error:
            new = open("mobjFiles/" + str(i).zfill(4) + "_" + str(math.floor(i / 4)) + ".NCL", "wb")
        new.write(file[oldOffset:newOffset])
    