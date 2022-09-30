file = open("player.bin", "rb").read()
import os
try:
    os.mkdir("playerFiles")
except OSError as error:
    pass

import math
count = -1
for i in range(352):
    count = count + 1
    oldOffset = int.from_bytes(file[(i * 8):(4 + (i * 8))], "little")
    newOffset = int.from_bytes(file[(8 + (i * 8)):(12 + (i * 8))], "little")

    extension = ".bin"
    try:
        extension = "." + file[(oldOffset + 5):(oldOffset + 9)].decode("UTF-8")[::-1]
    except ValueError as error:
        pass
    
    
    if (oldOffset != newOffset) and (oldOffset != 0) and (newOffset != 0):
        try:
            new = open("playerFiles/" + str(i).zfill(4) + "_" + str(math.floor(count / 4)) + extension, "wb")
        except ValueError as error:
            count = count - 1
            new = open("playerFiles/" + str(i).zfill(4) + ".NCL", "wb")
        new.write(file[oldOffset:newOffset])