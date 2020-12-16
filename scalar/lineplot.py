import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import json

def lineplot(cfg):
    xList = cfg['line']['x']
    plt.figure(figsize=cfg['figsize'])
    for xName in xList:
        x = np.load(xName)
        sns.lineplot(x=x)

    custom_plot(**cfg['plot_info'])
    plt.savefig(cfg['save_name'], dpi=300)

if __name__=="__main__":
    with open("config.json")  as jsonfile:
        cfg = json.load(jsonfile)



    