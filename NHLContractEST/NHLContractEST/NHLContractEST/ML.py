# This file will house the general ML functions 
# used for the different approaches

import numpy as np
from Util import *
from ContractStructure import *
from FormatData import *

# Relu function used for learning models.
# Takes z and returns a
# Note that z can be a vector or a scalar
def ReLU(z):
    a = np.maximum(z, 0.0)
    return a

# Derivative of relu function used for learning models.
# Takes a and returns gprime
# Note that a can be a vector or a scalar
def ReLUPrime(a):
    
    # This is simply 1 for nonzero values and 0 otherwise
    gprime = (a > 0).astype(int)
    return gprime


# This will calculate the cost function for a relu activation function
# In this case, a difference of squares is used.
# A represents the prediction vector and Y represents the true output
# dA is also returned, the derivative of the cost function with respect to "A"
def ReLUCost(A, Y):

    m = A.shape[1] 

    assert(m == Y.shape[1])

    J = np.sum((A - Y) ** 2)

    J = J / (2*m)
    dA = A - Y

    return J, dA

# This will take in a set of parameters Wl, bl, gl and L and return
#  the predicted outputs y for the input X
# Wl and bl are weights and biases for each layer for l = 1:L
# gl is the name of the activation function for that layer
# This will also return a cache variable of stored intermediate values
# so that these can be used in backpropagation
def ForwardPropagation(X, param):
    
    cache = {}
    
    n = X.shape[0]
    m = X.shape[1]

    # First find nunmber of layers L
    L = param["L"]

    # Input is A0
    cache["A0"] = X

    for l in range (1, L+1):
        W = param["W" + str(l)]
        b = param["b" + str(l)]
        g = param["g" + str(l)]

        cache["Z" + str(l)] = np.dot(W,cache["A" + str(l-1)]) + b
        
        if(g == "relu"):
            cache["A" + str(l)] = ReLU(cache["Z" + str(l)])

        if(g == "linear"):
            cache["A" + str(l)] = cache["Z" + str(l)]

        # Copy W and b into cache as well (needed for backpropagation)
        cache["W" + str(l)] = W
        cache["b" + str(l)] = b

    Y = cache["A" + str(L)]

    assert(Y.shape == (1, m))

    return Y, cache

# This will take in a cost J and a set of parameters Wl, bl, gl and L and return
# the gradients dWl and dBl for each layer
# Note that this also requires dA, the derivative of the cost function with respect 
# to the predicted output.
def BackPropagation(dA, cache, param):

    grad = {}

    # Grab sizes from input
    n = cache["A0"].shape[0]
    m = cache["A0"].shape[1]

    L = param["L"]

    # First entry is passed in
    grad["dA" + str(L)] = dA

    for l in range(L, 0, -1):

        g = param["g" + str(l)]

        if(g == "relu"):
            gprime = ReLUPrime(cache["Z" + str(L)])

        if(g == "linear"):
            # Linear gprime is just an array of ones
            gprime = np.ones(cache["Z" + str(l)].shape)

        grad["dZ" + str(l)] = grad["dA" + str(L)] * gprime
        grad["dW" + str(l)] = (1/m)* np.dot(grad["dZ" + str(l)], cache["A" + str(l-1)].T)
        grad["db" + str(l)] = (1/m) * np.sum(grad["dZ" + str(l)], axis = 1, keepdims = True)
        grad["dA" + str(l-1)] = np.dot(cache["W" + str(l)].T , grad["dZ" + str(l)])

        # Double check that shapes of all gradients match expected variables
        assert(grad["dZ" + str(l)].shape == cache["Z" + str(l)].shape)
        assert(grad["dW" + str(l)].shape == cache["W" + str(l)].shape)
        assert(grad["db" + str(l)].shape == cache["b" + str(l)].shape)
        assert(grad["dA" + str(l-1)].shape == cache["A" + str(l-1)].shape)

    return grad


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

    y, cache = ForwardPropagation(xNorm, modelParam)

    y = np.squeeze(y)

    print("Predicted Salary = " + str(y) + "$")


    return y

