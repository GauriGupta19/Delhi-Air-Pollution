from constants import PARAM

class ClassifierExecuter:
    def __init__(self,*argv) -> None:
        if(len(argv) > 1):
            sensor,coordinate,hiddenLayers,numframes,seeds = argv
            self.sensor = sensor
            self.coordinate = coordinate
            self.Param = PARAM.replace("%%HIDDEN_LAYERS%%",hiddenLayers)
            self.numframes = numframes
            self.seeds = seeds
            self.isDir = True
        else:
            filename = argv[0]
            self.file = filename
            self.isDir = False

        