import os
from bz2 import BZ2File


path = "standard/"
for root, dirs, files in os.walk(path, topdown=False):
    for filename in files:
        filepath = path + filename
        newfilepath = filepath + ".decompressed"
        print("decompressing: " + filepath)
        cf = BZ2File(filepath)
        data = cf.read()
        open(newfilepath, 'wb').write(data)