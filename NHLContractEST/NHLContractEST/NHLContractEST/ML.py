# This file will house the general ML functions 
# used for the different approaches

import numpy as np
from Util import *
from ContractStructure import *
from FormatData import *

# Relu function used for learning models.
# Takes z and returns a
# Note that z can be a vector or a scalar
def relu(z):
    a = np.maximum(z, 0.0)
    return a


# This will calculate the cost function for a relu activation function
# In this case, a difference of squares is used.
# A represents the prediction vector and Y represents the true output
def reluCost(A, Y):

    m = A.shape[1] 

    assert(m == Y.shape[1])

    J = np.sum((A - Y) ** 2)

    J = J / (2*m)

    return J

# This will take in a set of parameters Wl, bl, actl and L and return
#  the predicted outputs y for the input X
# Wl and bl are weights and biases for each layer for l = 1:L
# actl is the name of the activation function for that layer
# This will also return a cache variable of stored intermediate values
# in case these are necessary
def predict(X, param):
    
    cache = {}
    
    n = X.shape[0]
    m = X.shape[1]

    # First find nunmber of layers L
    L = param["L"]

    # Now do forward propagation
    cache["A0"] = X
    for l in range (1, L+1):
        W = param["W" + str(l)]
        b = param["b" + str(l)]
        act = param["act" + str(l)]

        cache["Z" + str(l)] = np.dot(W.T,cache["A" + str(l-1)]) + b
        
        if(act == "relu"):
            cache["A" + str(l)] = relu(cache["Z" + str(l)])

        if(act == "linear"):
            cache["A" + str(l)] = cache["Z" + str(l)]

    Y = cache["A" + str(L)]

    assert(Y.shape == (1, m))

    return Y, cache

# This will create a new contract entry for a given player and use modelParam to
# predict that player's value at the time of 'year'
def FindPlayerWorth(PlayerList, SalaryCapTable, TeamStatsList, \
    name, contractLength, year, modelParam, CurrentYear, xMean, xVar):

    found = 0

    print("Making salary prediction for " + str(name) + "...")

    # First find player in list
    for p in PlayerList:
        if(FormatURL(p.Name) == FormatURL(name)):
            found = 1
            break
    if(found == 0):
        print("Error: Player not found")
        return;

    # Create entry with no salary (unecessary for this)
    c = CreateContractEntry(p, year, SalaryCapTable, TeamStatsList, \
        CurrentYear, contractLength)

    # Create feature vectors. Note that y is unecessary. 
    x, garbage = CreateFeatureVector(c)

    xNorm = NormalizeFeatureVector(x, xMean, xVar)

    y, cache = predict(xNorm, modelParam)

    y = np.squeeze(y)

    print("Predicted Salary = " + str(y) + "$")


    return y

