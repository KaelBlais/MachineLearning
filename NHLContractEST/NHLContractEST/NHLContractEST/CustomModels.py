# This file will attempt to create a salary predictor using simple regression. 
# The activation function used for this will be a ReLU function

import numpy as np
from ML import *

# This function will run a custom linear regression model using X (n x m matrix) and Y (1 x m vector)
# The results will be a dictionary containing the parameters W and b 
# as well as a history of the cost function J
# Note that this assumes the inputs have already been normalized
def LinearRegressionModel_Custom(X, Y, numIterations = 10000, learningRate = 0.001):

    print("Running custom linear regression with ReLU activation...")

    param = {}

    # First split X and Y into training sets and dev sets (70/30 % split)
    # Linear regression is only used for proof-of-concept so only train and dev sets are used
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
    W = np.random.randn(1, n)
    # W = np.zeros((1, n))
    b = np.array([0.0])
    b = np.reshape(b, (1, 1)) # Make b a 1 x 1 array

    # Assign constant parameters 
    param["g1"] = "relu"
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


    print("Done with regression. Training Error = " + str(trainE) + ", Dev Error = " + str(devE))
    return param, JHistory, trainE, devE


# This function will run a custom neural network model using X (n x m matrix) and Y (1 x m vector)
# The results will be a dictionary containing the parameters W and b 
# as well as a history of the cost function J
# Note that this assumes the inputs have already been normalized
def NeuralNetworkModel_Custom(X, Y, numIterations = 10000, learningRate = 0.001):

    print("Running custom neural network model...")

    param = {}

    # Param +/- are used for gradient checking
    paramPlus = {}
    paramMinus = {}

    # First split X and Y into training, dev and test sets (60/20/20 % split)
    n = X.shape[0]
    mTotal = X.shape[1]
    mTrain = int(mTotal * 0.6)
    mDev = int(mTotal * 0.2)
    mTest = mTotal - mTrain - mDev

    XTrain = X[: , 0:mTrain+1]
    XDev = X[:, mTrain:mTrain+mDev]
    XTest = X[:, mTrain+mDev:mTotal]


    YTrain = Y[: , 0:mTrain+1]
    YDev = Y[:, mTrain:mTrain+mDev]
    YTest = Y[:, mTrain+mDev:mTotal]

    # Create model architecture
    L = 2 # L is total number of layers

    # Ll is number of units in layer l
    L1 = 1
    L2 = 1
    L3 = 1


    # Initialize parameters with random Ws and 0 bias
    np.random.seed(1)
    param["W1"] = np.random.randn(L1, n)*0.01
    param["b1"] = np.zeros((L1, 1))

    # param["W2"] = np.random.randn(L2, L1)*0.01
    # Overwrite second layer with ones and zero for debug
    param["W2"] = np.ones((1, 1))
    param["b2"] = np.zeros((L2, 1))

    param["W3"] = np.random.randn(L3, L2)
    param["b3"] = np.zeros((L3, 1))


    # Assign constant parameters 
    param["g1"] = "linear"
    param["g2"] = "linear"
    param["g3"] = "linear"
    param["L"] = L
    param["L1"] = L1
    param["L2"] = L2
    param["L3"] = L3

    JHistory = np.zeros((numIterations, 1))

    # Overwrite with debug values for debug
    # This one works
    # XTrain = np.ones((param["W1"].T.shape))
    # YTrain = np.zeros((1, 1))

    # XTrain = np.ones((XTrain.shape))
    # YTrain = np.zeros((YTrain.shape))
    YTrain = YTrain / 1000000

    for i in range(numIterations):

        # Propagate through
        A, cache = ForwardPropagation(XTrain, param.copy())

        J, dA = ReLUCost(A, YTrain)

        # print("Cost: " + str(J))

        # Run backpropagation
        grad = BackPropagation(dA, cache.copy(), param.copy())


        # Perform gradient checking
        # gradCopy = grad.copy()
        # gradDiff = GradientCheck(XTrain, YTrain, param.copy(), gradCopy)


        # Update parameters
        
        for l in range(1, L+1):    
            dW = grad["dW" + str(l)]
            db = grad["db" + str(l)]
            W = param["W" + str(l)]
            b = param["b" + str(l)]
            assert(dW.shape == W.shape)
            assert(db.shape == b.shape)

            W = W - learningRate*dW 
            b = b - learningRate*db 

            if l <= 3: # for now, only use 1st layer for debug
                param["W" + str(l)] = W
                param["b" + str(l)] = b

        JHistory[i] = J

        print("Training Progress = " + str(int((i+1)*100/numIterations)) + "% complete", end = '\r')
        

    # run predictions for all sets
    trainPredictions, cache = ForwardPropagation(XTrain, param)
    devPredictions, cache = ForwardPropagation(XDev, param)
    testPredictions, cache = ForwardPropagation(XTest, param)

    trainE = (1 / mTrain) * np.sum(abs(YTrain - trainPredictions))
    devE = (1 / mDev) * np.sum(abs(YDev - devPredictions))
    testE = (1 / mTest) * np.sum(abs(YTest - testPredictions))


    print("Done with regression. Training Error = " + str(trainE) + ". Dev Error = " + str(devE) + ", Test Error = " + str(testE))
    return param, JHistory, trainE, devE