from constants import *
from sys import argv
from os import path
from ClassifierExecuter import ClassifierExecuter
from typing import List

# Reading the arguments
ISDIR = True
if(len(argv) > 1):
    newpath = argv[1]
    if(path.isdir(newpath)):
        DATASET = newpath
        print("[INFO] Using dataset directory:", newpath)
    elif(path.isfile(newpath)):
        DATASET = newpath
        print("[INFO] Using dataset file:", newpath)
        ISDIR = False

    if(len(argv) > 2):
        respath = argv[2]
        if(path.isdir(respath)):
            RESULT = respath
else:
    print("[INFO] Using dataset directory:", DATASET)
print("[INFO] Using result directory:", RESULT,'\n')

# Adds all possible combinations of classifiers
def addAllClassifier(toexecute : List[ClassifierExecuter]) -> None:
    seeds = [SEEDFACTOR*i for i in range(1,NUMEXEC+1)]
    for sensor in SensorEnum:
        for coordinate in sensor.value.coordinates:
            for hiddenLayers in HIDDENLAYER:
                for numframes in FRAMES:
                    # print("[INFO] Adding classifier:", sensor.name, coordinate.name, hiddenLayers, numframes)

                    # TODO: Chcek if seeds.copy() id required or not
                    toexecute.append(ClassifierExecuter(sensor, coordinate, hiddenLayers, numframes, seeds))

toexecute = []
if(not ISDIR):
    toexecute.append(ClassifierExecuter(DATASET))
else:
    addAllClassifier(toexecute)

# FOR TESTING
# for i in toexecute:
#     if(i.isDir):
#         print('sensor',i.sensor)
#         print('coordinate',i.coordinate)
#         print('param',i.Param)
#         print('numframes',i.numframes)
#         print('seeds',i.seeds)
#     else:
#         print('file',i.file)
#     print()



# TODO: train and predict each classifier
