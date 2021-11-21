from lib.figproc import FigGen
from lib.dataproc import FeatureGen
from lib.rmsproc import RMSGen
import os
import shutil
import json


TARGETS = ["s3","s4"]
CONC = [50,100]

class ScoreManager(object):
    def __init__(self) -> None:
        super().__init__()
        pass

    def figgen(self, source_path):
        SOURCE = source_path
        meas_files = os.listdir(SOURCE)
        for m in meas_files:
            FILEPATH = SOURCE+ m + "/"
            SAVEPATH = "./png/" + m + "/"
            try:
                shutil.rmtree(SAVEPATH)
            except Exception:
                pass
            os.makedirs(SAVEPATH)
            fg = FigGen(filepath=FILEPATH, savepath=SAVEPATH)
            for target in TARGETS:
                for conc in CONC:
                    fg.pnggen(target=target,rc=conc)

    def featgen(self, source_path):
        SOURCE = source_path
        meas_files = os.listdir(SOURCE)
        for m in meas_files:
            FILEPATH = SOURCE+ m + "/"
            SAVEPATH = "./features/" + m + "/"
            try:
                shutil.rmtree(SAVEPATH)
            except Exception:
                pass
            os.makedirs(SAVEPATH)
            ft = FeatureGen(filepath= FILEPATH, savepath=SAVEPATH)
            for conc in CONC:
                ft.featcsvgen(rc=conc,targets=TARGETS)
    
    def scoregen(self, feature_path):
        SOURCE = feature_path
        meas_files = os.listdir(SOURCE)
        for m in meas_files:
            FILEPATH = SOURCE+ m + "/"
            SAVEPATH = "./scores/" + m + "/"
            try:
                shutil.rmtree(SAVEPATH)
            except Exception:
                pass
            os.makedirs(SAVEPATH)
            rm = RMSGen(filepath=FILEPATH, savepath=SAVEPATH)
            for conc in CONC:
                for target in TARGETS:
                    score1, score2 = rm.get_rms(conc=conc,label=target)
                    print("Scores:  (%.4f, %.4f)" % (score1,score2) + " conc: %s, sample: %s" % (conc,target))
                    scores = {
                        'score1': score1,
                        'score2' : score2,
                    }
                    with open(SAVEPATH+ str(conc)+ "_" + target+ ".json","w+") as f:
                            json.dump(scores,f)

    
if __name__ == "__main__":
    sm = ScoreManager()
    sm.figgen(source_path="./src/")
    sm.featgen(source_path="./src/")
    sm.scoregen(feature_path="./features/")

    