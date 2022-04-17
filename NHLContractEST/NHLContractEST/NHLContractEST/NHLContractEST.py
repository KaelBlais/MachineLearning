
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetFeatures import *
import urllib


# data = urllib.request.urlopen("https://www.capfriendly.com/players/connor-mcdavid").read(10000000)
# print(data)

# test = "Age" in data


XTrain, YTrain, ActivePlayerList = GetStatsFromCapFriendly()

Names = ActivePlayerList["Names"]

print(Names)

