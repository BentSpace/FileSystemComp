import os
import shutil
import ast

homeDirectory = os.path.expanduser('~')
directoryPathSingle = homeDirectory + "/singleRoot"
directoryPathHy = homeDirectory + "/hierarchicalRoot"
# def create_directory(directory_name, path)

def singleRootFileSysCreate():
    directoryExistsAlready = os.path.isdir(directoryPathSingle)
    if directoryExistsAlready:
        shutil.rmtree(directoryPathSingle)
    os.mkdir(directoryPathSingle)
    i = 1
    while i <= 100:
        f = open(directoryPathSingle + "/file" + str(i) + ".txt", "w")
        f.close()
        i += 1

def hyFileSysCreate():
    directoryExistsAlready = os.path.isdir(directoryPathHy)
    if directoryExistsAlready:
        shutil.rmtree(directoryPathHy)
    os.mkdir(directoryPathHy)
    i = 1
    while i <= 100:
        if i % 10 == 1:
            newDir = directoryPathHy + "/files" + str(i) + "-" + str(i + 9) 
            os.mkdir(newDir)
        f = open(newDir + "/file" + str(i) + ".txt", "w")
        f.close()
        i += 1

def traverseDirectory(startDir):
    fileDict = {}
    dirDict = {}
    for dirName, subdirList, fileList in os.walk(startDir):
        for fileName in fileList:
            fileSize = os.path.getsize(dirName + "/" + fileName)
            fileDict.update({fileName: fileSize})
        for subdir in subdirList:
            dirSize = os.path.getsize(startDir + "/" + subdir)
            dirDict.update({subdir: dirSize})
    return fileDict, dirDict

def writeToFile(startDir, fileDict, dirDict = None):
    if startDir == directoryPathSingle:
        fileName = startDir + "/" + "singleLevelFiles.txt"
    else:
        fileName = startDir + "/" + "hierarchicalFiles.txt"
    f = open(fileName, "w")
    f.write(str(fileDict))
    f.write("*")
    f.write(str(dirDict))
    f.close()

def printToScreen(file):
    with open(file) as f:
        data = f.read()
    splitData = data.split("*")
    fileDict = ast.literal_eval(splitData[0])
    dirDict = ast.literal_eval(splitData[1])
    print(fileDict)
    print(dirDict)

singleRootFileSysCreate()
hyFileSysCreate()
fileDict, dirDict = traverseDirectory(directoryPathSingle)
writeToFile(directoryPathSingle, fileDict)
printToScreen(directoryPathSingle + "/" + "singleLevelFiles.txt")
fileDict, dirDict = traverseDirectory(directoryPathHy)
writeToFile(directoryPathHy, fileDict, dirDict)
printToScreen(directoryPathHy  + "/" + "hierarchicalFiles.txt")

