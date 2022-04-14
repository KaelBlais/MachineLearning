# This file will load all necessary input and output variables

import pandas as pd

# This function will load all of the required input features from Capfriendly
def GetFeatures():

    # import pandas as np

    print("Getting inputs...")

    PlayerNames = list()
    
    # Import player data. There are 32 pages of active players in Capfriendly
    for i in range (0, 2):
        url = "https://www.capfriendly.com/browse/active?pg=" + str(i+1)
        L = pd.read_html(url)

        # Convert list to data frame using following code
        for j in L:
            DF = j

        # Find number of players in list
        n = DF["PLAYER"].size

        # print("Length of Data: " + str(n))

        for k in range (0, n):
            PlayerNames.append(DF["PLAYER"].iloc[k])


    
    print("done.")

    ActivePlayerList = {"Names": PlayerNames}
    
    XTrain = 0.0
    YTrain = 0.0

    return XTrain, YTrain, ActivePlayerList