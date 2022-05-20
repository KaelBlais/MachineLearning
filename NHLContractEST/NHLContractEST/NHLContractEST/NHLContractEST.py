import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetData import *
from Util import *
from UI import *
from ContractStructure import *

CurrentYear = 2021 

# NOTE: Use this command to change VS interactive window directory to desired path
# import os
# os.getcwd() to view current directory
# os.chdir("Path\\To\\File")


ActivePlayerList, SalaryCapTable, TeamStatsList = GetInputsUI(CurrentYear, LoadDefaults = True)


# Print random player for debug
# PrintPlayerInfo(ActivePlayerList[300])


testContract = CreateContractEntry(ActivePlayerList[46], 2020, SalaryCapTable, TeamStatsList, \
    CurrentYear, 5, 1000000)


PrintContractEntry(testContract)

# Print salary cap value
# print(SalaryCapTable["Seasons"])
# print(SalaryCapTable["Upper Cap"])
# print(SalaryCapTable["Min Salary"])