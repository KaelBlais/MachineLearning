# This file will load all necessary input and output variables from various sources

import pandas as pd
import urllib
from Util import *

class Player:
    def __init__(self, Name):
        self.Name = Name
    Age = 0
    Position  = ""
    NumContracts = 0
    ContractDates = []
    ContractAAV = []
    ContractLength = []
    TeamHistory = []


# This function will load all of the required input features from Capfriendly
def GetStatsFromCapFriendly():


    print("Getting stats from CapFriendly...")

    ActivePlayerList = []
    
    # Import player data. There are 32 pages of active players in Capfriendly
    numPages = 1;
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

        # Set up temporary lists. Appending straight to the player list causes the same element for all players to be appended.
        # Instead, these temporary lists are cleared and re-used every time to give each player his own independent list. 
        yearList = []
        aavList = []
        lengthList = []
        numContracts = 0;

        # Get contract info. First will be current contract. Last will be stats. Go from 1 to last - 1.
        for j in range(1, len(L) - 1):
            DF = L[j]

            # Check size to make sure this matches. Some old entries have an invalid format. 
            if(DF.shape[1] == 9):
                n = DF[0].size

                # Contract length is number of rows - 2 
                length = n-2

                # AAV is total amount (last row) divided by contract length
                s = DF[7].iloc[n-1] # total salary amount

                # strip $ and , from salary
                s = s.replace("$", "")
                s = s.replace(",", "")
                AAV = int(int(s) / (length))

                # Find contract start date from second row
                s = DF[0].iloc[1]
                s = s[0:4] # First year is first 4 digits
                startYear = int(s)
            
                # Append to temporary list
                yearList.append(startYear)
                aavList.append(AAV)
                lengthList.append(length)
                numContracts = numContracts + 1;

        # Now add current contract after (index 0)
        DF = L[0]
        n = DF[0].size

        # Contract length is number of rows - 2 
        length = n-2

        # AAV is total amount (last row) divided by contract length
        s = DF[7].iloc[n-1] # total salary amount

        # strip $ and , from salary
        s = s.replace("$", "")
        s = s.replace(",", "")
        AAV = int(s) / (length)

        # Find contract start date from second row
        s = DF[0].iloc[1]
        s = s[0:4] # First year is first 4 digits
        startYear = int(s)
            
        # Append current contract to end of list
        yearList.append(startYear)
        aavList.append(AAV)
        lengthList.append(length)
        numContracts = numContracts + 1;

        # Store back in player list
        ActivePlayerList[i].ContractDates = yearList
        ActivePlayerList[i].ContractAAV = aavList
        ActivePlayerList[i].ContractLength = lengthList
        ActivePlayerList[i].NumContracts = numContracts


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

        # Position comes right after age
        idx = idx + 10
        if(s[idx:idx+6] == "centre"):
            ActivePlayerList[i].Position = "C"
        if(s[idx:idx+12] == "left defense"):
            ActivePlayerList[i].Position = "LD"
        if(s[idx:idx+13] == "right defense"):
            ActivePlayerList[i].Position = "RD"
        if(s[idx:idx+11] == "left winger"):
            ActivePlayerList[i].Position = "LW"
        if(s[idx:idx+12] == "right winger"):
            ActivePlayerList[i].Position = "RW"
        if(s[idx:idx+10] == "goaltender"):
            ActivePlayerList[i].Position = "G"


    print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete")

    print("Done retrieving stats from capfriendly.")

    

    return ActivePlayerList