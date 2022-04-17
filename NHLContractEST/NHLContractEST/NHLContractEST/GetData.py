# This file will load all necessary input and output variables from various sources

import pandas as pd
import urllib
from Util import *

class Player:
    def __init__(self, Name):
        self.Name = Name
    Age = 0
    Position  = ""

# This function will load all of the required input features from Capfriendly
def GetStatsFromCapFriendly():


    print("Getting stats from CapFriendly...")

    ActivePlayerList = []
    
    # Import player data. There are 32 pages of active players in Capfriendly
    numPages = 2;
    print("     Getting active player names...")
    for i in range (0, numPages):
        print("     " + str(int((i+1)*100/numPages)) + "% complete", end = '\r')
        url = "https://www.capfriendly.com/browse/active?pg=" + str(i+1)
        L = pd.read_html(url)

        # Convert list to data frame. This list only has one dataframe. 
        DF = L[0]

        # Find number of players in list
        n = DF["PLAYER"].size

        # print("Length of Data: " + str(n))

        for j in range (0, n):
            s = (DF["PLAYER"].iloc[j])
            # First trim everything before name
            k = 0;
            while(s[k] < 'A' or s[k] > 'Z'):
                k = k + 1
            name = s[k:len(s)]
            
            # Append this player to the list
            ActivePlayerList.append(Player(name))

    print("     " + str(int((i+1)*100/numPages)) + "% complete")


    
    # Now go through data list and fill out info for each player.
    # This will contain basic info (age, position, etc.) and contract info
    print("     Getting Player Information...")
    for i in range(0, len(ActivePlayerList)):
        print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete", end = '\r')
        name = str(ActivePlayerList[i].Name)

        url = "https://www.capfriendly.com/players/" + FormatURL(name)
        L = pd.read_html(url)

        # Contract info can be found from tables using the read_html pandas command
        for j in L:
            DF = j
            # print(DF)


        # Basic info can be found from the player description using the raw html code
        # Each player description contains a blob of text in the same format. 
        # This blob will contain information
        data = urllib.request.urlopen(url).read(10000000)
        s = str(data)

        # Firt spot is the age of the player. 
        idx = s.find(" year old ");
        # Age comes right before this. This is always 2 digits. 
        sAge = s[idx-2:idx]
        ActivePlayerList[i].Age = int(sAge)

    print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete")

    print("Done retrieving stats from capfriendly.")

    

    return ActivePlayerList