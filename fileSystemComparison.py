import os
import shutil

homeDirectory = os.path.expanduser('~')
# def create_directory(directory_name, path)

def singleRootFileSysCreate():
    directoryPath = homeDirectory + "/singleRoot"
    directoryExistsAlready = os.path.isdir(directoryPath)
    if directoryExistsAlready:
        shutil.rmtree(directoryPath)
    os.mkdir(directoryPath)
    i = 1
    while i <= 100:
        f = open(directoryPath + "/file" + str(i) + ".txt", "w")
        f.close()
        i += 1

def hyFileSysCreate():
    directoryPath = homeDirectory + "/hierarchicalRoot"
    directoryExistsAlready = os.path.isdir(directoryPath)
    if directoryExistsAlready:
        shutil.rmtree(directoryPath)
    os.mkdir(directoryPath)
    i = 1
    while i <= 100:
        f = open(directoryPath + "/file" + str(i) + ".txt", "w")
        f.close()
        i += 1

singleRootFileSysCreate()