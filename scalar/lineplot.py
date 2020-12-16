import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import pandas as pd 
import json
from plot_utils.plt import *
from plot_utils.sns import *

def lineplot(cfg):
    fig = plt.figure(figsize=cfg['figsize'])
    sns.lineplot(x=cfg['x'], y=cfg['y'], data=cfg['data'])

    custom_plt_plot(fig, **cfg['plt_info'])
    custom_sns_plot(**cfg['sns_info'])

    plt.show()

if __name__=="__main__":
    with open("config.json")  as jsonfile:
        cfg = json.load(jsonfile)



    