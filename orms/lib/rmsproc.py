import math
import pandas as pd
import numpy as np
import json

class RMSGen(object):
    def __init__(self, filepath, savepath) -> None:
        super().__init__()
        self.filepath = filepath
        self.savepath = savepath

    def get_rms(self, conc:int, label:str):
        filename = self.filepath + "feature_rc" + str(conc) + ".csv"
        df = pd.read_csv(filename)
        X = df.iloc[:,1:len(df.columns)-1].values
        y = df['target'].values
        X_ = np.zeros(801)
        for i in range(0,len(X)):
            if y[i]==label:
                X_ = np.vstack((X_,X[i,:]))
        X_ = np.delete(X_,0,0)
        b = np.mean(X_[4:5,:],axis=0)
        g = np.mean(X_[9:10,:],axis=0)
        r = np.mean(X_[19:20,:],axis=0)

        def rmse(x,y):
            temp = 0
            for i in range(0,len(x)):
                temp = temp+((x[i]-y[i])**2)
            return math.sqrt(temp/len(x))

        scores = [rmse(b,g),rmse(g,r)]
        return scores


if __name__=="__main__":
    res = RMSGen("../features/m1/","")
    score1, score2 = res.get_rms(conc=100,label="s4")
    print("Scores:  (%.4f, %.4f)" % (score1,score2))
    scores = {
        'score1': score1,
        'score2' : score2
    }
    with open("./test.json","w+") as f:
        json.dump(scores,f)
