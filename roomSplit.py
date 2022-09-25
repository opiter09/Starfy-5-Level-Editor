file = open("roominfo.bin", "rb").read()
import os
try:
    os.mkdir("roomFiles")
except OSError as error:
    pass

import math
for i in range(894):
    beginning = 8576 + (i * 1408)
    end = 8576 + ((i + 1) * 1408)
    goal = ""
    if (file[(end - 68):(end - 64)].decode("UTF-8") == "Goal"):
        goal = "_Goal"
    if (file[(end - 68):(end - 57)].decode("UTF-8") == "Goal+SEVENT"):
        goal = "_Goal_ST"
    world = str(file[beginning + 2]).zfill(2)
    level = str(file[beginning + 1]).zfill(2)
    room = str(file[beginning]).zfill(2)
    if (world == "02") and (level == "02") and (str(file[beginning - 1408]).zfill(2) == "07"):
        room = "08"
    new = open("roomFiles/" + world + "_" + level + "_" + room + goal + ".bin", "wb")
    new.write(file[beginning:end])

goal = ""
if (file[(8576 - 68):(8576 - 64)].decode("UTF-8") == "Goal"):
    goal = "_Goal"
if (file[(8576 - 68):(8576 - 57)].decode("UTF-8") == "Goal+SEVENT"):
     goal = "_Goal_ST"
minus = open("roomFiles/00_01_01" + goal + ".bin", "wb")
minus.write(file[7168:8576])
    