
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import json
from GetData import *
from Util import *


capfriendlyFilename = 'CapfriendlyData.txt'

ActivePlayerList = GetStatsFromCapFriendly()

# json.dump(ActivePlayerList, open("CapfriendlyData.txt", 'w'))

PrintPlayerList(ActivePlayerList)


print("Saving outputs to " + capfriendlyFilename)
DumpToFile(ActivePlayerList, capfriendlyFilename)

print("Reading back data from " + capfriendlyFilename)
data = ReadFromFile(capfriendlyFilename)
if(ActivePlayerList[0:len(ActivePlayerList)] == data[0:len(data)]):
    print("File Data Matches")
else:
     print("File Data Doesn't Match")