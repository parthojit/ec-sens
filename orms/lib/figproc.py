import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sg
from scipy.signal import medfilt
import matplotlib as mpl
import os


class FigGen(object):
    def __init__(self,filepath:str , savepath:str) -> None:
        self.filepath = filepath
        self.savepath = savepath
        super().__init__()

    def cvplotter(self, filename:str,clr:str,label:str):
        df = pd.read_csv(self.filepath+filename)
        v = df['v']
        i = df['i']
        i = medfilt(i,kernel_size=9) # median filtering using kernel=9
        plt.plot(v,i,clr,label=label)

    def pnggen(self, target:str,rc:int):
        files = os.listdir(self.filepath)
        print("target: %s rc: %d" % (target,rc))
        mpl.rcParams['font.family'] = 'Verdana'
        fig = plt.figure(figsize=(5,4))
        plt.rcParams['font.size'] = 14
        for file in files:
            try:
                if file[0:2]==target and file[5:7]==str(rc) and int(file[11:13]) in range(1,6):
                    self.cvplotter(file,'k--',label="baseline")
                if file[0:2]==target and file[5:7]==str(rc) and int(file[11:13]) in range(6,11):
                    self.cvplotter(file,'r',label="gas")
                if file[0:2]==target and file[5:7]==str(rc) and int(file[11:13]) in range(11,21):
                    self.cvplotter(file,'g',label="recovery")
            except Exception:
                pass
            
            try:
                if file[0:2]==target and file[5:8]==str(rc) and int(file[12:14]) in range(1,6):
                    self.cvplotter(file,'k--',label="baseline")
                if file[0:2]==target and file[5:8]==str(rc) and int(file[12:14]) in range(6,11):
                    self.cvplotter(file,'r',label="gas")
                if file[0:2]==target and file[5:8]==str(rc) and int(file[12:14]) in range(11,21):
                    self.cvplotter(file,'g',label="recovery")
            except Exception:
                pass
        plt.xlabel("Volt in (V)")
        plt.ylabel("Current in ($\mu$A)")
        filename = target+ "_" + str(rc)
        plt.title(filename)
        plt.savefig(self.savepath + filename +".png",dpi=200,bbox_inches="tight")
        plt.close()

    def debug(self):
        print("ok!")

