import os

countNull = 0
countNumber = 0
numberList = []
for root, dirs, files in os.walk("./mapooFiles"):
    for file in files:
        opening = open("./mapooFiles/" + file, "rb")
        reading = opening.read()
        
        if (file.endswith(".bin") == True) and (len(reading) >= 5) and (int(file.split("_")[0]) < 2075):
            if (reading[4] == 0):
                countNull = countNull + 1
            else:
                countNumber = countNumber + 1
                numberList.append(file)
            
        opening.close()

text = open("roomList.txt", "rb").read()
for i in range(len(numberList)):
    file = numberList[i]
    os.rename("./mapooFiles/" + file, "./mapooFiles/" + file[:-4] + " [" + text.split("\n")[i] + "].bin")

print("Nulls: " + str(countNull))
print("Numbers: " + str(countNumber))
        