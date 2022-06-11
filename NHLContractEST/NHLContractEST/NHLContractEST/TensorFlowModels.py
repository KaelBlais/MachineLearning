# This file will attempt to create a salary predictor using models
# built from tensorflow packages

# Turn off annoying tensorflow W and I messages before importing
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import tensorflow.keras.layers as tfl
import numpy as np

# This model should have the same performance as the NeuralNetworkModel_Custom function
# NOTE: For some reason, a learning rate of 0.001 did not converge here, even though this converged 
# on the custom model. Reducing this to 0.0001 seems to converge
# This might be tied to the use of the Adams optimization and/or other inherent regularization
# in the model
def TensorFlow_SimpleNeuralNet(X, Y, numIterations = 10000, learningRate = 0.0001):

    print("Running TensorFlow Model...")

    # First split X and Y into training, dev and test sets (60/20/20 % split)
    n = X.shape[0]
    mTotal = X.shape[1]
    mTrain = int(mTotal * 0.6)
    mDev = int(mTotal * 0.2)
    mTest = mTotal - mTrain - mDev

    XTrain = X[: , 0:mTrain]
    XDev = X[:, mTrain:mTrain+mDev]
    XTest = X[:, mTrain+mDev:mTotal]

    YTrain = Y[: , 0:mTrain]
    YDev = Y[:, mTrain:mTrain+mDev]
    YTest = Y[:, mTrain+mDev:mTotal]


    # Reshape Xmatrices into correct shape (3D input)
    XTrain_Reshaped = np.zeros((mTrain, 1, n))
    XDev_Reshaped = np.zeros((mDev, 1, n))
    XTest_Reshaped = np.zeros((mTest, 1, n))

    # X inputs have to be converted to 3D shapes
    for i in range(n):
        temp = np.reshape(XTrain[i, :], (mTrain, 1))
        XTrain_Reshaped[:, :, i] = temp
        temp = np.reshape(XDev[i, :], (mDev, 1))
        XDev_Reshaped[:, :, i] = temp
        temp = np.reshape(XTest[i, :], (mTest, 1))
        XTest_Reshaped[:, :, i] = temp


    # Y vectors are simply transposed
    YTrain_Reshaped = YTrain.T
    YDev_Reshaped = YDev.T
    YTest_Reshaped = YTest.T


    model = tf.keras.Sequential([
        tfl.Dense(100, activation = 'relu', input_shape = (1, n)),
        tfl.Dense(50, activation = 'relu'),
        tfl.Dense(1, activation = 'relu')
        ])

    # Uncomment the following to double-check parameter dimensions
    # model.summary()

    # Set up model with adam optimizer. Note that this is different from the custom neural
    # network model which just used standard gradient descent
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = learningRate),
                  loss = 'MeanSquaredError',
                  metrics = ['MeanSquaredError']
                  )

    history = model.fit(XTrain_Reshaped, YTrain_Reshaped, epochs = numIterations, batch_size = mTrain,
              verbose = 0)

    # run predictions for all sets
    trainPredictions = np.squeeze(model.predict(XTrain_Reshaped, verbose = '0'))
    devPredictions = np.squeeze(model.predict(XDev_Reshaped, verbose = '0'))
    testPredictions = np.squeeze(model.predict(XTest_Reshaped, verbose = '0'))

    # Find errors and convert back to dollar values
    trainE = (1 / mTrain) * np.sum(abs(np.squeeze(YTrain_Reshaped) - trainPredictions)) * 1000000
    devE = (1 / mDev) * np.sum(abs(np.squeeze(YDev_Reshaped) - devPredictions)) * 1000000
    testE = (1 / mTest) * np.sum(abs(np.squeeze(YTest_Reshaped) - testPredictions)) * 1000000


    print("Done with model training. Training Error = " + str(int(trainE)) + "$, Dev Error = " + str(int(devE))\
    + "$, Test Error = " + str(int(testE)) + "$") 

    JHistory = history.history["loss"]

    return model, JHistory, trainE, devE


# This model will be a more elaborate model designed to achieve better performance
def TensorFlow_ComplexNeuralNet(X, Y, numIterations = 10000, learningRate = 0.0001):

    print("Running TensorFlow Model...")

    # First split X and Y into training, dev and test sets (60/20/20 % split)
    n = X.shape[0]
    mTotal = X.shape[1]
    mTrain = int(mTotal * 0.6)
    mDev = int(mTotal * 0.2)
    mTest = mTotal - mTrain - mDev

    XTrain = X[: , 0:mTrain]
    XDev = X[:, mTrain:mTrain+mDev]
    XTest = X[:, mTrain+mDev:mTotal]

    YTrain = Y[: , 0:mTrain]
    YDev = Y[:, mTrain:mTrain+mDev]
    YTest = Y[:, mTrain+mDev:mTotal]


    # Reshape Xmatrices into correct shape (3D input)
    XTrain_Reshaped = np.zeros((mTrain, 1, n))
    XDev_Reshaped = np.zeros((mDev, 1, n))
    XTest_Reshaped = np.zeros((mTest, 1, n))

    # X inputs have to be converted to 3D shapes
    for i in range(n):
        temp = np.reshape(XTrain[i, :], (mTrain, 1))
        XTrain_Reshaped[:, :, i] = temp
        temp = np.reshape(XDev[i, :], (mDev, 1))
        XDev_Reshaped[:, :, i] = temp
        temp = np.reshape(XTest[i, :], (mTest, 1))
        XTest_Reshaped[:, :, i] = temp


    # Y vectors are simply transposed
    YTrain_Reshaped = YTrain.T
    YDev_Reshaped = YDev.T
    YTest_Reshaped = YTest.T

    initializer = tf.keras.initializers.RandomNormal(seed = 1)

    regularizer = tf.keras.regularizers.L1L2(l1= 0.00, l2 = 0.07)

    model = tf.keras.Sequential([
        tfl.Dense(100, activation = 'relu', kernel_regularizer = regularizer, kernel_initializer = initializer, input_shape = (1, n)),
        # tfl.Dense(100, activation = 'relu', kernel_regularizer = regularizer, kernel_initializer = initializer ),
        tfl.Dense(50, activation = 'relu', kernel_regularizer = regularizer, kernel_initializer = initializer),
        # tfl.Dense(25, activation = 'relu', kernel_regularizer = regularizer, kernel_initializer = initializer),
        tfl.Dense(1, activation = 'relu', kernel_regularizer = regularizer, kernel_initializer = initializer)
        ])


    # Uncomment the following to double-check parameter dimensions
    # model.summary()

    # Set up model with adam optimizer. Note that this is different from the custom neural
    # network model which just used standard gradient descent
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = learningRate),
                  loss = 'MeanSquaredError',
                  metrics = ['MeanSquaredError']
                  )

    history = model.fit(XTrain_Reshaped, YTrain_Reshaped, epochs = numIterations, batch_size = mTrain,
              verbose = 0)

    # run predictions for all sets
    trainPredictions = np.squeeze(model.predict(XTrain_Reshaped, verbose = '0'))
    devPredictions = np.squeeze(model.predict(XDev_Reshaped, verbose = '0'))
    testPredictions = np.squeeze(model.predict(XTest_Reshaped, verbose = '0'))

    # Find errors and convert back to dollar values
    trainE = (1 / mTrain) * np.sum(abs(np.squeeze(YTrain_Reshaped) - trainPredictions)) * 1000000
    devE = (1 / mDev) * np.sum(abs(np.squeeze(YDev_Reshaped) - devPredictions)) * 1000000
    testE = (1 / mTest) * np.sum(abs(np.squeeze(YTest_Reshaped) - testPredictions)) * 1000000


    print("Done with model training. Training Error = " + str(int(trainE)) + "$, Dev Error = " + str(int(devE))\
    + "$, Test Error = " + str(int(testE)) + "$") 

    JHistory = history.history["loss"]

    return model, JHistory, trainE, devE

