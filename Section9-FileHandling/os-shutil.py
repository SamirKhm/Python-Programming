import os

a=os.listdir("Section9-FileHandling")  # list of files in current directory

print(a)

a1=os.getcwd()  # current working directory
print(a1)

print(os.path.isfile("Section9-FileHandling/sam.txt"))  # check if file exists

import shutil

shutil.copy("Section9-FileHandling/sam.txt","Section9-FileHandling/sam_copy.txt")  # copy file