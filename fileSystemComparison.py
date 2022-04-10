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
    # print(fileDict)
    # print(dirDict)
    aveFileSize, numFiles = findAveSizeAndNum(fileDict)
    if dirDict != None:
        aveDirSize, numDirs = findAveSizeAndNum(dirDict)
    if file == directoryPathSingle + "/" + "singleLevelFiles.txt":
        print("\nSingle Level File System")
        print("Number of files: " + str(numFiles))
        print("Average File Size: " + str(aveFileSize))
        print("Traversal Time: ")
    else:
        print("\nHierarchical Level File System")
        print("Number of files: " + str(numFiles))
        print("Number of Directories: " + str(numDirs))
        print("Average File Size: " + str(aveFileSize))
        print("Average Directory Size: " + str(aveDirSize))
        print("Traversal Time: ")

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
fileDict, dirDict = traverseDirectory(directoryPathSingle)
writeToFile(directoryPathSingle, fileDict)
printToScreen(directoryPathSingle + "/" + "singleLevelFiles.txt")
fileDict, dirDict = traverseDirectory(directoryPathHy)
writeToFile(directoryPathHy, fileDict, dirDict)
printToScreen(directoryPathHy  + "/" + "hierarchicalFiles.txt")

