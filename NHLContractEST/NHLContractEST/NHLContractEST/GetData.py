# This file will load all necessary input and output variables from various sources

import pandas as pd
import urllib
from Util import *

class SkaterSeasonStats:
    def __init__(self, Year):
        self.Year = Year
    Team = ""
    RegularGP = 0
    RegularGoals = 0
    RegularAssists = 0
    RegularPlusMinus = 0
    RegularPIM = 0
    RegularEVTOI = 0
    RegularEVG = 0
    RegularixG = 0.0
    RegularxG60 = 0.0
    RegularRelxG60 = 0.0
    RegularC60 = 0.0
    RegularRelC60 = 0.0
    PlayoffGP = 0
    PlayoffGoals = 0
    PlayoffAssists = 0
    PlayoffPlusMinus = 0
    PlayoffPIM = 0
    PlayoffEVTOI = 0
    PlayoffEVG = 0
    PlayoffixG = 0.0
    PlayoffxG60 = 0.0
    PlayoffRelxG60 = 0.0
    PlayoffC60 = 0.0
    PlayoffRelC60 = 0.0

class GoalieSeasonStats:
    def __init__(self, Year):
        self.Year = Year
    Team = ""
    RegularGP = 0
    RegularGAA = 0
    RegularSavePercent = 0
    RegularGA60 = 0
    RegularxGA60 = 0
    RegularGSAx60 = 0
    PlayoffGP = 0
    PlayoffGAA = 0
    PlayoffSavePercent = 0
    PlayoffGA60 = 0
    PlayoffxGA60 = 0
    PlayoffGSAx60 = 0



class Player:
    def __init__(self, Name):
        self.Name = Name
    Age = 0
    Position  = ""
    NumContracts = 0
    ContractDates = []
    ContractAAV = []
    ContractLength = []
    StatHistory = []

# Note: Might need to add old team e.g. Atlanta Trashers to this list
TeamList = ["Anaheim Duck", "Arizona Coyotes", "Boston Bruins",
            "Buffalo Sabres", "Calgary Flame", "Carolina Hurricanes",
            "Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets",
            "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers",
            "Florida Panthers", "Los Angeles Kings", "Minnesota Wild",
            "Montreal Canadiens", "Nashville Predators", "New Jersey Devils",
            "New York Islanders", "New York Rangers", "Ottawa Senators", 
            "Philadelphia Flyers", "Phoenix Coyotes", "Pittsburgh Penguins",
            "St. Louis Blues", "San Jose Sharks", "Tampa Bay Lighting",
            "Toronto Maple Leafs", "Vancouver Canucks", "Vegas Golden Knights",
            "Washington Capitals", "Winnipeg Jets"]


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
    # for i in range(0, len(ActivePlayerList)):
    for i in range(0, 1): # Shorten list for now
        print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete", end = '\r')
        name = str(ActivePlayerList[i].Name)

        url = "https://www.capfriendly.com/players/" + FormatURL(name)



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




        L = pd.read_html(url)

        # Set up temporary lists. Appending straight to the player list causes the same element for all players to be appended.
        # Instead, these temporary lists are cleared and re-used every time to give each player his own independent list. 
        yearList = []
        aavList = []
        lengthList = []
        statsList = []
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

        # The last DF contains all of the individual player stats
        DF = L[len(L)-1]
        n = 0
        for j in range(0, DF["SEASON"].size - 1):

            # Only NHL stats will be stored.
            if(DF["LEAGUE"].iloc[j] == "NHL"):
               season = DF["SEASON"].iloc[j]

               if(ActivePlayerList[i].Position != "G"):

                   # For normal stats, some of these column names will repeat.
                   # Therefore, the column index must be specified instead
                   statsList.append(SkaterSeasonStats(season))
                   statsList[n].Team = DF["TEAM"].iloc[j]

                   statsList[n].RegularGP = DF[DF.columns[4]].iloc[j]
                   statsList[n].RegularGoals = DF[DF.columns[5]].iloc[j]
                   statsList[n].RegularAssists = DF[DF.columns[6]].iloc[j]
                   statsList[n].RegularPlusMinus = DF[DF.columns[8]].iloc[j]
                   statsList[n].RegularPIM = DF[DF.columns[9]].iloc[j]
                   statsList[n].PlayoffGP = DF[DF.columns[12]].iloc[j]
                   statsList[n].PlayoffGoals = DF[DF.columns[13]].iloc[j]
                   statsList[n].PlayoffAssists = DF[DF.columns[14]].iloc[j]
                   statsList[n].PlayoffPlusMinus = DF[DF.columns[16]].iloc[j]
                   statsList[n].PlayoffPIM = DF[DF.columns[17]].iloc[j]
                   statsList[n].RegularEVTOI = DF[DF.columns[18]].iloc[j]
                   statsList[n].RegularEVG = DF[DF.columns[19]].iloc[j]
                   statsList[n].RegularixG = DF[DF.columns[20]].iloc[j]
                   statsList[n].RegularxG60 = DF[DF.columns[21]].iloc[j]
                   statsList[n].RegularRelxG60 = DF[DF.columns[22]].iloc[j]
                   statsList[n].RegularC60 = DF[DF.columns[23]].iloc[j]
                   statsList[n].RegularRelC60 = DF[DF.columns[24]].iloc[j]
                   statsList[n].PlayoffEVTOI = DF[DF.columns[26]].iloc[j]
                   statsList[n].PlayoffEVG = DF[DF.columns[27]].iloc[j]
                   statsList[n].PlayoffixG = DF[DF.columns[28]].iloc[j]
                   statsList[n].PlayoffxG60 = DF[DF.columns[29]].iloc[j]
                   statsList[n].PlayoffRelxG60 = DF[DF.columns[30]].iloc[j]
                   statsList[n].PlayoffC60 = DF[DF.columns[31]].iloc[j]
                   statsList[n].PlayoffRelC60 = DF[DF.columns[32]].iloc[j]
               else:
                    # Goalies have seperate stats
                   statsList.append(GoalieSeasonStats(season))
                   statsList[n].Team = DF["TEAM"].iloc[j]

                   statsList[n].RegularGP = DF[DF.columns[4]].iloc[j]
                   statsList[n].RegularGAA = DF[DF.columns[5]].iloc[j]
                   statsList[n].RegularSavePercent = DF[DF.columns[6]].iloc[j]
                   statsList[n].PlayoffGP = DF[DF.columns[9]].iloc[j]
                   statsList[n].PlayoffGAA = DF[DF.columns[10]].iloc[j]
                   statsList[n].PlayoffSavePercent = DF[DF.columns[11]].iloc[j]
                   statsList[n].RegularGA60 = DF[DF.columns[12]].iloc[j]
                   statsList[n].RegularxGA60 = DF[DF.columns[13]].iloc[j]
                   statsList[n].RegularGSAx60 = DF[DF.columns[14]].iloc[j]
                   statsList[n].PlayoffGA60 = DF[DF.columns[17]].iloc[j]
                   statsList[n].PlayoffxGA60 = DF[DF.columns[18]].iloc[j]
                   statsList[n].PlayoffGSAx60 = DF[DF.columns[19]].iloc[j]


               n = n+1

        # Append this to player
        ActivePlayerList[i].StatHistory = statsList





    print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete")

    print("Done retrieving stats from capfriendly.")

    

    return ActivePlayerList