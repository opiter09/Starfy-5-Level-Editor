import os

countNull = 0
countNumber = 0
nullList = []
numberList = []
for root, dirs, files in os.walk("./mapooFiles"):
    for file in files:
        opening = open("./mapooFiles/" + file, "rb")
        reading = opening.read()
        
        if (file.endswith(".bin") == True) and (len(reading) >= 5) and (int(file.split("_")[0]) < 2075):
            if (reading[4] == 0):
                countNull = countNull + 1
                nullList.append(file)
            else:
                countNumber = countNumber + 1
                numberList.append(file)
            
        opening.close()

for file in nullList:
    os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[:-4] + "_Null.bin")
for file in numberList:
    os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[:-4] + "_Number.bin")

print("Nulls: " + str(countNull))
print("Numbers: " + str(countNumber))
        