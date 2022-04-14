
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetFeatures import *


XTrain, YTrain, ActivePlayerList = GetFeatures()

Names = ActivePlayerList["Names"]

print(Names)

