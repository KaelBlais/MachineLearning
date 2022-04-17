# This file will load all necessary input and output variables

import pandas as pd
import urllib

class Player:
    Name = ""
    Age = 0
    Position  = ""

# This function will load all of the required input features from Capfriendly
def GetStatsFromCapFriendly():

    # import pandas as np
    P = Player()

    print(P.Age)

    print("Getting stats from CapFriendly...")

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

        data = urllib.request.urlopen(url).read(10000000)
        s = str(data)

        # print(data)
        idx = s.find(" year old ");

        # Age comes right before this
        sAge = s[idx-2:idx]
        P.Age = int(sAge)

    print("done.")

    ActivePlayerList = {"Names": PlayerNames}
    
    XTrain = 0.0
    YTrain = 0.0

    return XTrain, YTrain, ActivePlayerList