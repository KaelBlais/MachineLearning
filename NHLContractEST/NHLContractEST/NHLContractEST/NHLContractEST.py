
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
# import json
from GetData import *
from Util import *
from UI import *


ActivePlayerList, SalaryCapTable, TeamStatsList = GetInputsUI(LoadDefaults = True)


# Print random player for debug
# PrintPlayerInfo(ActivePlayerList[300])

# Print salary cap value
# print(SalaryCapTable["Seasons"])
# print(SalaryCapTable["Upper Cap"])
# print(SalaryCapTable["Min Salary"])

