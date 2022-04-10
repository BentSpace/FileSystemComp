# A comparison of single level vs hierarchical file systems
# by Nathan Bertram
#
# It took anywhere from 2.8 to 5.7 times longer to traverse the hierachical file
# system than the single level one, even thought they had exactly the same number
# of files.  Apparently it takes quite a bit of time to move between directories
# Thus making the single level system potential must faster, but also less 
# organized.  Single level could be a good chose when speed is paramount.
# 
# If you had a system that only support single level architecture you could 
# implement something similar to a hierachical by using a naming convention for
# your files that could something like [directoryName]_[subDirectoryName]_[fileName]
# where directory names are seperately from each other and the file name by the 
# underscore character.  The string after the last underscore is always the file
# name and it can be preceeded by an arbitrary number of directory and sub 
# directory names.  The underscore character can not be used in directory or file 
# names.

import os
import shutil
import ast
import time

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
    startTime = time.time()
    fileDict = {}
    dirDict = {}
    for dirName, subdirList, fileList in os.walk(startDir):
        for fileName in fileList:
            fileSize = os.path.getsize(dirName + "/" + fileName)
            fileDict.update({fileName: fileSize})
        for subdir in subdirList:
            dirSize = os.path.getsize(startDir + "/" + subdir)
            dirDict.update({subdir: dirSize})
    endTime = time.time()
    traversalTime = endTime - startTime
    return fileDict, dirDict, traversalTime

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

def printToScreen(file, traversalTime):
    with open(file) as f:
        data = f.read()
    splitData = data.split("*")
    fileDict = ast.literal_eval(splitData[0])
    dirDict = ast.literal_eval(splitData[1])
    # print(fileDict)
    # print(dirDict)
    aveFileSize, numFiles = findAveSizeAndNum(fileDict)
    if dirDict != None:
        aveDirSize, numDirs = findAveSizeAndNum(dirDict)
    if file == directoryPathSingle + "/" + "singleLevelFiles.txt":
        print("\nSingle Level File System")
        print("Number of files: " + str(numFiles))
        print("Average File Size: " + str(aveFileSize))
        print("Traversal Time: " + str(traversalTime) + " MS\n")
    else:
        print("Hierarchical Level File System")
        print("Number of files: " + str(numFiles))
        print("Number of Directories: " + str(numDirs))
        print("Average File Size: " + str(aveFileSize))
        print("Average Directory Size: " + str(aveDirSize))
        print("Traversal Time: " + str(traversalTime) + " MS\n")

def findAveSizeAndNum(dict):
    sum = 0
    num = 0
    values = dict.values()
    for size in values:
        sum += size
        num += 1
    ave = sum / num
    return ave, num

singleRootFileSysCreate()
hyFileSysCreate()
fileDict, dirDict, traversalTimeSingle = traverseDirectory(directoryPathSingle)
writeToFile(directoryPathSingle, fileDict)
printToScreen(directoryPathSingle + "/" + "singleLevelFiles.txt", traversalTimeSingle)
fileDict, dirDict, traversalTimeHy = traverseDirectory(directoryPathHy)
writeToFile(directoryPathHy, fileDict, dirDict)
printToScreen(directoryPathHy  + "/" + "hierarchicalFiles.txt", traversalTimeHy)

