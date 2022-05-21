import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetData import *
from Util import *
from UI import *
from ContractStructure import *
from FormatData import *
from random import shuffle

CurrentYear = 2021 

# NOTE: Use this command to change VS interactive window directory to desired path
# import os
# os.getcwd() to view current directory
# os.chdir("Path\\To\\File")


ActivePlayerList, SalaryCapTable, TeamStatsList = GetInputsUI(CurrentYear, LoadDefaults = True)

ContractList = CreateContractList(ActivePlayerList, SalaryCapTable, TeamStatsList, CurrentYear)


'''
print("CONTRACTS BEFORE SHUFFLE: \n\n")
for i in range(5):
    PrintContractEntry(ContractList[i])
for i in range(5):
    PrintContractEntry(ContractList[len(ContractList) - i - 1])
'''

# Randomize list before converting to X, Y
shuffle(ContractList)

'''
print("CONTRACTS AFTER SHUFFLE: \n\n")
for i in range(5):
    PrintContractEntry(ContractList[i])
for i in range(5):
    PrintContractEntry(ContractList[len(ContractList) - i - 1])
'''

# Print random player for debug
# PrintPlayerInfo(ActivePlayerList[300])

# Print salary cap value
# print(SalaryCapTable["Seasons"])
# print(SalaryCapTable["Upper Cap"])
# print(SalaryCapTable["Min Salary"])