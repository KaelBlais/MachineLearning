
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetFeatures import *



# Import data. There are 32 pages of active players in capfriendly


XTrain, YTrain = GetFeatures()

# for i in range (1, 32):

    
    

T0 = pd.read_html("https://www.capfriendly.com/browse/active?pg=1")
T1 = pd.read_html("https://www.capfriendly.com/browse/active?pg=2")


for i in T0:
    B = i


# print(B.columns)

C = B["PLAYER"].iloc[0]

# print(C)