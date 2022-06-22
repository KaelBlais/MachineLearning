import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from GetData import *
from Util import *
from UI import *
from ContractStructure import *
from FormatData import *
from CustomModels import *
from TensorFlowModels import *

CurrentYear = 2022 


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
random.seed(1)
random.shuffle(ContractList)

'''
print("CONTRACTS AFTER SHUFFLE: \n\n")
for i in range(5):
    PrintContractEntry(ContractList[i])
for i in range(5):
    PrintContractEntry(ContractList[len(ContractList) - i - 1])
'''


X, Y = CreateFeatureMatrix(ContractList)

# Normalize X
xMean, xVar = FindFeatureStats(X)
XNorm = NormalizeFeatureVector(X, xMean, xVar)

avgSalary = np.mean(Y) * 1000000

print("Average Player Salary: " + str(int(avgSalary)) + "$ (above minimum salary)")

# Plot each feature 1 by 1. This is only useful if run through debugger.
n = X.shape[0]

'''
for i in range(n):
    PlotFeatureVector(X[i, :], Y, FeatureNames[i])
'''

# param, JHistory, trainE, devE = LinearRegressionModel_Custom(XNorm, Y)
# param, JHistory, trainE, devE = NeuralNetworkModel_Custom(XNorm, Y)
# param, JHistory, trainE, devE = TensorFlow_SimpleNeuralNet(XNorm, Y)
param, JHistory, trainE, devE = TensorFlow_ComplexNeuralNet(XNorm, Y)

# Plot cost function
PlotCostFunction(JHistory)


while(1):
    PlayerPredictionsUI(ActivePlayerList, SalaryCapTable, TeamStatsList, CurrentYear, param, xMean, xVar)

# Print random player for debug
# PrintPlayerInfo(ActivePlayerList[1])

# Print salary cap value
# print(SalaryCapTable["Seasons"])
# print(SalaryCapTable["Upper Cap"])
# print(SalaryCapTable["Min Salary"])