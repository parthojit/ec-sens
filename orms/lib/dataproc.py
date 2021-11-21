import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import medfilt
import os
import shutil


class FeatureGen(object):
    def __init__(self, filepath, savepath) -> None:
        super().__init__()
        self.filepath = filepath
        self.savepath = savepath

    def featuregen(self, filename:str):
        df = pd.read_csv(filename)
        v = np.sort(df['v'].values)
        i = medfilt(df['i'].values,kernel_size=9)
        i1 = []
        i2 = []
        for item in v:
            index = df.index[df['v']==item].tolist()
            try:
                i1.append(i[index[0]]) # forward or backward scan
                i2.append(i[index[1]]) # backward or forward scan
            except Exception:
                i2.append(df['i'][index[0]])
                pass
        i1 = np.array(i1)
        i2 = np.array(i2)
        plt.plot(v,abs(i1-i2))
        return abs(i1-i2)

    def featcsvgen(self, rc:int, targets:list):
        CONC = [rc]
        X = np.zeros(801)
        y = []
        for index,target in enumerate(targets):
            for conc in CONC:
                for cycle in range(1,21):
                    cyc = "%02d" % cycle
                    filename = self.filepath + target + "_rc" + str(conc) + "_cyc"+ cyc + ".csv"
                    print(filename)
                    X = np.vstack((X, self.featuregen(filename)))
                    y.append(target)
        X = np.delete(X,0,0)
        y = np.array(y)
        df = pd.DataFrame(X)
        df['target'] = y 
        df.to_csv(self.savepath + "feature_rc"+str(rc)+".csv")

if __name__== "__main__":
    pass