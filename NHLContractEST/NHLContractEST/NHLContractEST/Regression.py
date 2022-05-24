# This file will attempt to create a salary predictor using simple regression. 
# The activation function used for this will be a ReLU function

import numpy as np
from ML import *

# This function will run a custom linear regression model using X (n x m matrix) and Y (1 x m vector)
# The results will be a dictionary containing the parameters W and b 
# as well as a history of the cost function J
# Note that this assumes the inputs have already been normalized
def LinearRegressionModel_Custom(X, Y, numIterations = 100, learningRate = 0.01):

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
    W = np.random.randn(n, 1)
    b = 0.0

    JHistory = np.zeros((numIterations, 1))

    for i in range(numIterations):

        # Propagate through
        Z = np.dot(W.T, XTrain) + b
        # A = relu(Z)

        A = Z

        J = reluCost(A, YTrain)

        # For ReLU, gradient is 0 for entries where z was 0 (A is also 0)

        # First calculate linear portion of gradient
        temp = A-YTrain
        # temp = temp * (A > 0) # zero out sections where A = 0

        # Note that dW should have shape of (n, 1) and dB (1, 1)

        dW = (1/mTrain) * np.dot(XTrain,temp.T)
        dB = np.sum(temp)

        assert(dW.shape == W.shape == (n, 1))

        W = W - learningRate*dW 
        b = b - learningRate*dB 

        JHistory[i] = J


    param["W1"] = W
    param["b1"] = b
    param["act1"] = "relu"
    param["L"] = 1

    # run predictions for both sets
    trainPredictions, cache = predict(XTrain, param)
    devPredictions, cache = predict(XDev, param)

    trainE = (1 / mTrain) * np.sum(abs(YTrain - trainPredictions))
    devE = (1 / mDev) * np.sum(abs(YDev - devPredictions))


    print("Done with regression. Training Error = " + str(trainE) + ". Dev Error = " + str(devE))
    return param, JHistory, trainE, devE