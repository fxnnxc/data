import numpy as np



class Annealing():
    def f(self, x):
        return x*x

    def make(self):
        T = 14700*2
        M = 2 
        R = 0.5
        t = np.arange(0,T)
        tau = np.clip(t%np.ceil(T/M)/(T/M),0,1)
        beta = [self.f(t) if t<=R else 1 for t in tau]
        beta = np.array(beta)
        np.save("../data/annealing.npy",beta)   
        print("*--Check data folder--*")


if __name__=="__main__":
    an = Annealing()
    an.make()

