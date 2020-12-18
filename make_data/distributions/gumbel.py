import numpy as np
import pandas as pd 

class Gumbel():
     def make(self, n=100, loc=0.0, scale=1.0, size=None):
        x = np.random.gumbel(loc=loc, scale=scale, size=n)
        df = pd.DataFrame(x, columns=["x"])
        df.to_csv("data/gumbel.csv", index=False)   
        print("*--Generate Gumbel. Check data folder--*")



if __name__=="__main__":
    gb = Gumbel()
    gb.make()

