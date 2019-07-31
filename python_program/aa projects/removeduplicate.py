# program for remove duplicate song
import os
print("path 1 for folder name where original file is available  \n \
path 2 for folder name where Duplicate file is available  \n")
a = input(r"Enter  the path 1 ")
folder1 = (a)
folder1song = os.listdir(folder1)

b = input(r"Enter the path 2 ")
folder2 = (b)
folder2song = os.listdir(folder2)

for song in folder1song:
    if song in folder2song:
        commonsong = os.path.join(folder2 , song)
        os.remove(commonsong)
