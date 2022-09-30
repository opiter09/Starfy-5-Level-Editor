import os
new = open("output_roominfo.bin", "ab")
old = open("roominfo.bin", "rb").read()
new.write(old[0:7168])
for root, dirs, files in os.walk("./roomFiles"):
    sortList = files
    sortList.sort()
    for file in sortList:
        if (file.endswith(".bin") == True):
            new.write(open("./roomFiles/" + file, "rb").read())
new.write(old[1267328:])