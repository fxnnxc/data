
from scalar.lineplot import *

if __name__=="__main__":
    with open("config.json")  as jsonfile:
        cfg = json.load(jsonfile)
    lineplot(cfg)
    