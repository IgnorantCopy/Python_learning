"""
Created by Ignorant on 2024/1/28
Description: File Operation
"""
import os

# copy file
with open("data/img1.png", 'rb') as ibs:
    container = ibs.read()
    with open("data/img1_copy.png", 'wb') as obs:
        obs.write(container)
print("Copy Successfully!")

# directory name
path = os.path.dirname(__file__)
print(path)
# absolute path
path = os.path.abspath(__file__)
print(path)
print(os.path.isfile(path))
print(os.path.isdir(path))
print()
# current working directory
path = os.getcwd()
print(path)
print(os.path.isfile(path))
print(os.path.isdir(path))
print()
# size of file
os.path.join(path, "02-operation.py")
size = os.path.getsize(path)
print(size)
# file name
result = os.path.split(path)
print(result)
print()

# copy directory
path = "data"
files = os.listdir(path)
print(files)
for i in files:
    file_path = os.path.join(path, i)
    if os.path.isfile(file_path):
        with open(os.path.join(path, i), "rb") as ibs:
            container = ibs.read()
            with open(os.path.join(path, "copy", i), "wb") as obs:
                obs.write(container)
print("Copy Successfully!")

# remove file
os.remove("data/copy/img1_copy.png")
# create a directory
new_path = "data/new"
if not os.path.exists(new_path):
    os.mkdir(new_path)
# remove a directory
os.rmdir(new_path)
