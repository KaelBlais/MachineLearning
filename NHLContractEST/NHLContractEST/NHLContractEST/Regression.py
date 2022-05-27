# This file will attempt to create a salary predictor using simple regression. 
# The activation function used for this will be a ReLU function

import numpy as np
from ML import *

# This function will run a custom linear regression model using X (n x m matrix) and Y (1 x m vector)
# The results will be a dictionary containing the parameters W and b 
# as well as a history of the cost function J
# Note that this assumes the inputs have already been normalized
def LinearRegressionModel_Custom(X, Y, numIterations = 10000, learningRate = 0.001):

    print("Running custom regression with ReLU activation...")

    param = {}

    # First split X and Y into training sets and test sets (70/30 % split)
    # Regression is only used for proof-of-concept so only train and dev sets are used
    n = X.shape[0]
    mTotal = X.shape[1]
    mTrain = int(mTotal * 0.7)
    mDev = mTotal - mTrain

    XTrain = X[: , 0:mTrain+1]
    XDev = X[:, mTrain:mTotal]

    YTrain = Y[: , 0:mTrain+1]
    YDev = Y[:, mTrain:mTotal]

    # Initialize parameters with random Ws and 0 bias
    np.random.seed(1)
    # W = np.random.randn(1, n)
    W = np.zeros((1, n))
    b = np.array([0.0])
    b = np.reshape(b, (1, 1)) # Make b a 1 x 1 array

    # Assign constant parameters 
    param["g1"] = "linear"
    param["L"] = 1

    JHistory = np.zeros((numIterations, 1))

    for i in range(numIterations):

        # Propagate through
        param["W1"] = W
        param["b1"] = b
        A, cache = ForwardPropagation(XTrain, param)

        J, dA = ReLUCost(A, YTrain)

        # Run backpropagation
        grad = BackPropagation(dA, cache, param)
        dW = grad["dW1"]
        db = grad["db1"]

        assert(dW.shape == W.shape == (1, n))

        W = W - learningRate*dW 
        b = b - learningRate*db 

        JHistory[i] = J

        print("Training Progress = " + str(int((i+1)*100/numIterations)) + "% complete", end = '\r')


    # Grab last set of parameters
    param["W1"] = W
    param["b1"] = b

    # run predictions for both sets
    trainPredictions, cache = ForwardPropagation(XTrain, param)
    devPredictions, cache = ForwardPropagation(XDev, param)

    trainE = (1 / mTrain) * np.sum(abs(YTrain - trainPredictions))
    devE = (1 / mDev) * np.sum(abs(YDev - devPredictions))


    print("Done with regression. Training Error = " + str(trainE) + ". Dev Error = " + str(devE))
    return param, JHistory, trainE, devE