import os
import configparser
configFileName = "Data/config.conf"

def writeFile(path, data):
    try:
        with open(path, 'w') as f:
            f.write(data)
            f.close
    except IOError:
        return 0
    else:
        return 1

def setToFile(links, file_name):
    try:
        with open(file_name,"w") as f:
            for l in sorted(links):
                f.write(l + "\n")
                f.close
    except IOError:
        return 0
    else:
        return 1

def fileToSet(file_name):
    results = set()
    try:
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
        return results
    except IOError:
        return 0

def fileOps(filename , mode):
    try:
        f = open(filename , mode)
    except IOError:
        print('Problem reading '+ filename )
        return 0
    else:    
        return f

def appendtoFile(path, data):
    try:
        with open(path, 'a') as file:
            file.write(data + '\n')
    except IOError:
        return 0
    else:
        return 1

def readEachLine(filename):
    try:
        f = fileHandler.readline()
    except IOError:
        return 0
    else:
        return 1

def deleteFile(filename):
    try:
        os.remove(filename)
    except IOError:
        return 0
    else:
        return 1

def createFile(filename):
    try:
        os.mknod(filename)
    except IOError:
        return 0
    else:
        return 1

def deleteDir(fname):
    try:
        os.remove(fname)
    except IOError:
        return 0
    else:
        return 1

def createDir(fname):
    try:
        os.mkdir(fname)
    except IOError:
        return 0
    else:
        return 1    

def readConfig(section,query):
    config = configparser.ConfigParser()
    config.read(configFileName)
    f = config[section][query]
    return f

def writeConfig(section,query,value):
    config = configparser.ConfigParser()
    config[section][query] = value
    with open(configFileName,'w') as f:
        config.write(f)    
