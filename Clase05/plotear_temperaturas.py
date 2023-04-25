import random
import statistics
import os
import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas():
    b = np.load(os.path.join('Data','temperaturas.npy'))
    plt.hist(b,bins=30)
    plt.show()  

