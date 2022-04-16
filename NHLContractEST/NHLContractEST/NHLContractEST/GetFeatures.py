# This file will load all necessary input and output variables

import pandas as pd

# This function will load all of the required input features from Capfriendly
def GetFeaturesFromCapFriendly():

    # import pandas as np

    print("Getting inputs...")

    PlayerNames = list()
    
    # Import player data. There are 32 pages of active players in Capfriendly
    for i in range (0, 1):
        url = "https://www.capfriendly.com/browse/active?pg=" + str(i+1)
        L = pd.read_html(url)

        # Convert list to data frame. This list only has one dataframe. 
        DF = L[0]

        # Find number of players in list
        n = DF["PLAYER"].size

        # print("Length of Data: " + str(n))

        for k in range (0, n):
            PlayerNames.append(DF["PLAYER"].iloc[k])


    
    # Now go through data list and create inputs for each player
    for i in range(0, len(PlayerNames)):
        s1 = str(PlayerNames[i]);
        # First trim everything before name
        k = 0;
        while(s1[k] < 'A' or s1[k] > 'Z'):
            k = k + 1
        name = s1[k:len(s1)]

        # Now replace spaces with - for urls
        name = name.replace(" ", "-")
        url = "https://www.capfriendly.com/players/" + name
        L = pd.read_html(url)


        for j in L:
            DF = j
            print(DF)

        url = "https://www.nhl.com/player/connor-mcdavid-8478402"
        L = pd.read_html(url)


        for j in L:
            DF = j
            print(DF)
        '''
        # Convert to data frame
        DF0 = L[0]
      #   age = DF0["Age"]
        DF1 = L[1]
        # age = DF1["Age"]
        DF2 = L[2]
       #  age = DF2["Age"]
       '''



        print(L)

    print("done.")

    ActivePlayerList = {"Names": PlayerNames}
    
    XTrain = 0.0
    YTrain = 0.0

    return XTrain, YTrain, ActivePlayerList