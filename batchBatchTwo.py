import os
import subprocess

for root, dirs, files in os.walk("./mapooFiles"):
    for file in files:
        subprocess.run([ "lzss.bat", os.path.join(root, file)])