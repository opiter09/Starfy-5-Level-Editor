file = open("mapoo.bin", "rb").read()
import os
try:
    os.mkdir("mapooFiles")
except OSError as error:
    pass

import math
for i in range(3286):
    oldOffset = int.from_bytes(file[(16 + (i * 8)):(20 + (i * 8))], "little")
    newOffset = int.from_bytes(file[(24 + (i * 8)):(28 + (i * 8))], "little")

    extension = ".bin"
    if (int.from_bytes(file[(oldOffset + 5):(oldOffset + 8)], "big") == 5129036):
        extension = ".NCL"
    elif (int.from_bytes(file[(oldOffset + 5):(oldOffset + 8)], "big") == 5133123):
        extension = ".NSC"
    elif (int.from_bytes(file[(oldOffset + 5):(oldOffset + 8)], "big") == 5129031):
        extension = ".NCG"
        
    if (oldOffset != newOffset):
        new = open("mapooFiles/" + str(i).zfill(4) + extension, "wb")
        new.write(file[oldOffset:newOffset])
    