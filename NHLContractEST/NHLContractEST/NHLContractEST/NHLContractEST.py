
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetData import *
from Util import *
from UI import *
from FormatData import *

CurrentYear = 2021 


ActivePlayerList, SalaryCapTable, TeamStatsList = GetInputsUI(CurrentYear, LoadDefaults = True)


# Print random player for debug
PrintPlayerInfo(ActivePlayerList[300])


testContract = CreateContractEntry(ActivePlayerList[46], 2020, SalaryCapTable, TeamStatsList, \
    CurrentYear, 5, 1000000)


# Print salary cap value
print(SalaryCapTable["Seasons"])
# print(SalaryCapTable["Upper Cap"])
# print(SalaryCapTable["Min Salary"])

