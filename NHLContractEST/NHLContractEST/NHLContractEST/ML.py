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

    # Also store L in cache
    cache["L"] = L

    for l in range (1, L+1):
        W = param["W" + str(l)]
        b = param["b" + str(l)]
        g = param["g" + str(l)]
        Zl = np.dot(W,cache["A" + str(l-1)]) + b

        cache["Z" + str(l)] = Zl
        
        if(g == "relu"):
            Al = ReLU(Zl)

        if(g == "linear"):
            Al = Zl

        cache["A" + str(l)] = Al

        # Copy W,g and b into cache as well (needed for backpropagation)
        cache["W" + str(l)] = W
        cache["b" + str(l)] = b
        cache["g" + str(l)] = g

    Y = cache["A" + str(L)]

    assert(Y.shape == (1, m))

    return Y, cache

# This will take in a cost J and a set of parameters Wl, bl, gl and L and return
# the gradients dWl and dBl for each layer
# Note that this also requires dA, the derivative of the cost function with respect 
# to the predicted output.
def BackPropagation(dA, cache):

    grad = {}

    # Grab sizes from input
    n = cache["A0"].shape[0]
    m = cache["A0"].shape[1]

    L = cache["L"]

    # First entry is passed in
    grad["dA" + str(L)] = dA


    for l in range(L, 0, -1):

        g = cache["g" + str(l)]
        Zl = cache["Z" + str(l)]

        if(g == "relu"):
            gprime = ReLUPrime(Zl)

        if(g == "linear"):
            # Linear gprime is just an array of ones
            gprime = np.ones(Zl.shape)

        dAl = grad["dA" + str(l)]
        dZl = dAl * gprime
        Alminus1 = cache["A" + str(l-1)]
        dWl = (1/m)* np.dot(dZl, Alminus1.T)
        dbl = (1/m) * np.sum(dZl, axis = 1, keepdims = True)
        Wl = cache["W" + str(l)]
        dAlminus1 = np.dot(Wl.T , dZl)


        grad["dZ" + str(l)] = dZl
        grad["dW" + str(l)] = dWl
        grad["db" + str(l)] = dbl
        grad["dA" + str(l-1)] = dAlminus1

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

    # Check whether param represents a custom model dictionary or a tensorflow model
    if(type(modelParam) == dict):
        # This is a dictionary, use custom function
        y, cache = ForwardPropagation(xNorm, modelParam)
    else:
        # This is a tensorflow object, use tf model prediction
        n = xNorm.shape[0]
        XNorm_Reshaped = np.reshape(xNorm, (1, 1, n))
        y = modelParam.predict(XNorm_Reshaped, verbose = '0')

    y = np.squeeze(y)

    yearIndex = np.squeeze(np.where(SalaryCapTable["Seasons"] == year))
    y = y*1000000 + SalaryCapTable["Min Salary"][yearIndex]

    print("Predicted Salary = " + str(y) + "$")


    return y


# This function will flatten relevent parameters from param into a big array.
# This is necessary for gradient checking. 
def FlattenParam(param): 
    L = param["L"]
    first = 1

    for l in range(1, L+1):
        v = np.reshape(param["W" + str(l)], (-1, 1))
        if(first):
            vector = v
            first = 0
        else:
            vector = np.concatenate((vector, v), axis=0)

        v = np.reshape(param["b" + str(l)], (-1, 1))
        vector = np.concatenate((vector, v), axis=0)

    return vector

# This function will unflatten relevent parameters from vector into the proper dictionary
# This is necessary for gradient checking. 
def UnflattenParam(array, param): 
    L = param["L"]
    newParam = param.copy()
    idx = 0


    for l in range(1, L+1):
        s0 = param["W" + str(l)].shape[0]
        s1 = param["W" + str(l)].shape[1]
        idxEnd = idx + s0*s1
        newParam["W" + str(l)] = array[idx:idxEnd].reshape((s0, s1))
        idx = idxEnd
        s0 = param["b" + str(l)].shape[0]
        s1 = param["b" + str(l)].shape[1]
        idxEnd = idx + s0*s1
        newParam["b" + str(l)] = array[idx:idxEnd].reshape((s0, s1))
        idx = idxEnd

    return newParam


# This function will flatten relevent gradients from grad into a big array.
# This is necessary for gradient checking. 
def FlattenGrad(grad, L):
    first = 1

    for l in range(1, L+1):
        v = np.reshape(grad["dW" + str(l)], (-1, 1))
        if(first):
            vector = v
            first = 0
        else:
            vector = np.concatenate((vector, v), axis=0)

        v = np.reshape(grad["db" + str(l)], (-1, 1))
        vector = np.concatenate((vector, v), axis=0)

    return vector

# This function will run gradient checking on all parameters in param
def GradientCheck(X, Y, param, grad, epsilon = 1e-7):
    L = param["L"]
    
    # Only need last activation function to determine cost
    g = param["g" + str(L)]

    # First reshape all necessary parameters into a giant vector
    paramVector = FlattenParam(param)


    numParam = paramVector.shape[0]
    Jplus = np.zeros((numParam, 1))
    Jminus = np.zeros((numParam, 1))
    gradApprox = np.zeros((numParam, 1))

    flatGrad = FlattenGrad(grad, L)
    for i in range(numParam):

        # Nudge one param up by epsilon
        paramPlus = np.copy(paramVector) 
        paramPlus[i] = paramPlus[i] + epsilon
        A, cache = ForwardPropagation(X, UnflattenParam(paramPlus, param))
        if(g == "linear" or g == "relu"):
            Jplus[i], dA = ReLUCost(A, Y)

        # Nudge one param down by epsilon
        paramMinus = np.copy(paramVector) 
        paramMinus[i] = paramMinus[i] - epsilon
        A, cache = ForwardPropagation(X, UnflattenParam(paramMinus, param))
        if(g == "linear" or g == "relu"):
            Jminus[i], dA = ReLUCost(A, Y)

        # Calculate approximate gradient from slope
        gradApprox[i] = (Jplus[i] - Jminus[i]) / (2*epsilon)
        
        
    # Compare performance
    numDiff = abs(flatGrad - gradApprox)
    numerator =  np.linalg.norm(flatGrad - gradApprox)
    denominator = np.linalg.norm(flatGrad) + np.linalg.norm(gradApprox)
    gradDiff =  numerator / denominator

    if(gradDiff > 2e-7):
        print("\n\n\nGradDiff:" + str(gradDiff) + "\n\n\n")

    return gradDiff