from enum import Enum

NUMEXEC = 10
NUMFOLD = 10
SEEDFACTOR = 10
DATASET = '../dataset/'
RESULT = '../result/'
FRAMES = [4,5,6,7,8]
DATASETTYPE = 'va'
RESULTFILE = 'results.csv'

PARAM = "-L 0.3 -M 0.2 -N 500 -V 0 -S %%SEED%% -E 20 -H %%HIDDEN_LAYERS%%"
HIDDENLAYER = ["a", "40", "30", "20", "10"]

class CoordinateEnum(Enum):
    X = 'X'
    Y = 'Y'
    Z = 'Z'

class Sensor:
    def __init__(self, name, key, *argv):
        self.name = name
        self.key = key
        self.coordinates = list(argv)   

class SensorEnum(Enum):
	LINEAR_ACCELERATION_EARTH = Sensor("aceleracaoLinearTerra", "AclLinE", CoordinateEnum.X, CoordinateEnum.Y, CoordinateEnum.Z)
	ACCELEROMETER_EARTH = Sensor("acelerometroTerra", "AcelE", CoordinateEnum.X, CoordinateEnum.Y, CoordinateEnum.Z)
	MAGNETIC_FIELD_EARTH = Sensor("campoMagneticoTerra", "MagE", CoordinateEnum.Y, CoordinateEnum.Z)
	GYROSCOPE_EARTH = Sensor("giroscopioTerra", "GirE", CoordinateEnum.X, CoordinateEnum.Y, CoordinateEnum.Z)

class EventEnum(Enum):
    AGGRESSIVE_LEFT_TURN = "curva_esquerda_agressiva"
    AGGRESSIVE_RIGHT_TURN = "curva_direita_agressiva"
    AGGRESSIVE_LEFT_LANE_CHANGE = "troca_faixa_esquerda_agressiva"
    AGGRESSIVE_RIGHT_LANE_CHANGE = "troca_faixa_direita_agressiva"
    AGGRESSIVE_ACCELERATION = "aceleracao_agressiva"
    AGGRESSIVE_BRAKE = "freada_agressiva"
    NON_AGGRESSIVE = "evento_nao_agressivo"

