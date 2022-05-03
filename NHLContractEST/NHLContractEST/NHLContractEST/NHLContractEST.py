
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
# import json
from GetData import *
from Util import *
from UI import *


ActivePlayerList = GetInputsUI()


# Print first 10 players for debug
PrintPlayerList(ActivePlayerList[0:5])
