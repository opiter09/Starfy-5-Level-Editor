import sys

data = open(sys.argv[1], "rb").read()

for i in range(16, 16 + 40 * data[0], 40):
    new = open(str((i - 16) // 40 + 1) + ".bin", "wb")
    new.write(data[i:(i + 40)])