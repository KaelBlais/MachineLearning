# This file will load all necessary input and output variables from various sources

import pandas as pd
import urllib
import numpy as np
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


# This function will load all of the required player stats from CapFriendly
def GetPlayerStatsFromCapFriendly():


    print("Getting stats from CapFriendly...")

    ActivePlayerList = []
    
    # Import player data. There are 32 pages of active players in Capfriendly
    numPages = 32;
    print("     Getting active player names...")
    for i in range (0, numPages):
        print("     " + str(int((i+1)*100/numPages)) + "% complete", end = '\r')
        url = "https://www.capfriendly.com/browse/active?pg=" + str(i+1)
        L = pd.read_html(url)

        # Convert list to data frame. This list only has one dataframe. 
        DF = L[0]

        # Find number of players in list
        n = DF["PLAYER"].size

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
    # This will contain basic info (age, position, etc.), season stats and contract info
    print("     Getting Player Information...")
    numPlayers = len(ActivePlayerList)
    i = 0
    while(i < numPlayers):
        print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete", end = '\r')
        name = str(ActivePlayerList[i].Name)

        url = "https://www.capfriendly.com/players/" + FormatURL(name)


        # Try the link. If it doesn't work, try appending "1" to name.
        # Some player pages have this for some reason.
        try:
            L = pd.read_html(url)
        except: 
            # print("Invalid url: " + url)
            url = url + "1"
            L = pd.read_html(url)


        # Basic info can be found from the player description using the raw html code
        # Each player description contains a blob of text in the same format. 
        # This blob will contain information
        data = urllib.request.urlopen(url).read(10000000)


        s = str(data)

        # First spot is the age of the player. 
        idx = s.find(" year old ");
        if(idx == -1):
            # Couldn't find the string. This player has a different format (e.g. players who passed away)
            # This is extremely rare. This player will simply be removed from the list.
            del(ActivePlayerList[i])
            i = i - 1
            numPlayers = numPlayers - 1
            continue

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

                   # Some stats will have a '-' to represent missing data. This will be treated as NaN.
                   if(DF[DF.columns[4]].iloc[j] == '-'):
                       statsList[n].RegularGP = float("NaN")
                   else:
                       statsList[n].RegularGP = float(DF[DF.columns[4]].iloc[j])

                   if(DF[DF.columns[5]].iloc[j] == '-'):
                       statsList[n].RegularGoals = float("NaN")
                   else:
                       statsList[n].RegularGoals = float(DF[DF.columns[5]].iloc[j])

                   if(DF[DF.columns[6]].iloc[j] == '-'):
                       statsList[n].RegularAssists = float("NaN")
                   else:
                       statsList[n].RegularAssists = float(DF[DF.columns[6]].iloc[j])

                   if(DF[DF.columns[8]].iloc[j] == '-'):
                       statsList[n].RegularPlusMinus = float("NaN")
                   else:
                       statsList[n].RegularPlusMinus = float(DF[DF.columns[8]].iloc[j])

                   if(DF[DF.columns[9]].iloc[j] == '-'):
                       statsList[n].RegularPIM = float("NaN")
                   else:
                       statsList[n].RegularPIM = float(DF[DF.columns[9]].iloc[j])

                   if(DF[DF.columns[12]].iloc[j] == '-'):
                       statsList[n].PlayoffGP = float("NaN")
                   else:
                       statsList[n].PlayoffGP = float(DF[DF.columns[12]].iloc[j])

                   if(DF[DF.columns[13]].iloc[j] == '-'):
                       statsList[n].PlayoffGoals = float("NaN")
                   else:
                       statsList[n].PlayoffGoals = float(DF[DF.columns[13]].iloc[j])

                   if(DF[DF.columns[14]].iloc[j] == '-'):
                       statsList[n].PlayoffAssists = float("NaN")
                   else:
                       statsList[n].PlayoffAssists = float(DF[DF.columns[14]].iloc[j])

                   if(DF[DF.columns[16]].iloc[j] == '-'):
                       statsList[n].PlayoffPlusMinus = float("NaN")
                   else:
                       statsList[n].PlayoffPlusMinus = float(DF[DF.columns[16]].iloc[j])

                   if(DF[DF.columns[17]].iloc[j] == '-'):
                       statsList[n].PlayoffPIM = float("NaN")
                   else:
                       statsList[n].PlayoffPIM = float(DF[DF.columns[17]].iloc[j])

                
                   statsList[n].RegularEVTOI = DF[DF.columns[18]].iloc[j]

                   if(DF[DF.columns[19]].iloc[j] == '-'):
                       statsList[n].RegularEVG = float("NaN")
                   else:
                       statsList[n].RegularEVG = float(DF[DF.columns[19]].iloc[j])

                   if(DF[DF.columns[20]].iloc[j] == '-'):
                       statsList[n].RegularixG = float("NaN")
                   else:
                       statsList[n].RegularixG = float(DF[DF.columns[20]].iloc[j])

                   if(DF[DF.columns[21]].iloc[j] == '-'):
                       statsList[n].RegularxG60 = float("NaN")
                   else:
                       statsList[n].RegularxG60 = float(DF[DF.columns[21]].iloc[j])

                   if(DF[DF.columns[22]].iloc[j] == '-'):
                       statsList[n].RegularRelxG60 = float("NaN")
                   else:
                       statsList[n].RegularRelxG60 = float(DF[DF.columns[22]].iloc[j])

                   if(DF[DF.columns[23]].iloc[j] == '-'):
                       statsList[n].RegularC60 = float("NaN")
                   else:
                       statsList[n].RegularC60 = float(DF[DF.columns[23]].iloc[j])

                   if(DF[DF.columns[24]].iloc[j] == '-'):
                       statsList[n].RegularRelC60 = float("NaN")
                   else:
                       statsList[n].RegularRelC60 = float(DF[DF.columns[24]].iloc[j])

                   statsList[n].PlayoffEVTOI = DF[DF.columns[26]].iloc[j]

                   if(DF[DF.columns[27]].iloc[j] == '-'):
                       statsList[n].PlayoffEVG = float("NaN")
                   else:
                       statsList[n].PlayoffEVG = float(DF[DF.columns[27]].iloc[j])

                   if(DF[DF.columns[28]].iloc[j] == '-'):
                       statsList[n].PlayoffixG = float("NaN")
                   else:
                       statsList[n].PlayoffixG = float(DF[DF.columns[28]].iloc[j])

                   if(DF[DF.columns[29]].iloc[j] == '-'):
                       statsList[n].PlayoffxG60 = float("NaN")
                   else:
                       statsList[n].PlayoffxG60 = float(DF[DF.columns[29]].iloc[j])

                   if(DF[DF.columns[30]].iloc[j] == '-'):
                       statsList[n].PlayoffRelxG60 = float("NaN")
                   else:
                       statsList[n].PlayoffRelxG60 = float(DF[DF.columns[30]].iloc[j])

                   if(DF[DF.columns[31]].iloc[j] == '-'):
                       statsList[n].PlayoffC60 = float("NaN")
                   else:
                       statsList[n].PlayoffC60 = float(DF[DF.columns[31]].iloc[j])

                   if(DF[DF.columns[32]].iloc[j] == '-'):
                       statsList[n].PlayoffRelC60 = float("NaN")
                   else:
                       statsList[n].PlayoffRelC60 = float(DF[DF.columns[32]].iloc[j])
               else:
                    # Goalies have seperate stats
                   statsList.append(GoalieSeasonStats(season))
                   statsList[n].Team = DF["TEAM"].iloc[j]

                   if(DF[DF.columns[4]].iloc[j] == '-'):
                       statsList[n].RegularGP = float("NaN")
                   else:
                       statsList[n].RegularGP = float(DF[DF.columns[4]].iloc[j])

                   if(DF[DF.columns[5]].iloc[j] == '-'):
                       statsList[n].RegularGAA = float("NaN")
                   else:
                       statsList[n].RegularGAA = float(DF[DF.columns[5]].iloc[j])

                   if(DF[DF.columns[6]].iloc[j] == '-'):
                       statsList[n].RegularSavePercent = float("NaN")
                   else:
                       statsList[n].RegularSavePercent = float(DF[DF.columns[6]].iloc[j])

                   if(DF[DF.columns[9]].iloc[j] == '-'):
                       statsList[n].PlayoffGP = float("NaN")
                   else:
                       statsList[n].PlayoffGP = float(DF[DF.columns[9]].iloc[j])

                   if(DF[DF.columns[10]].iloc[j] == '-'):
                       statsList[n].PlayoffGAA = float("NaN")
                   else:
                       statsList[n].PlayoffGAA = float(DF[DF.columns[10]].iloc[j])

                   if(DF[DF.columns[11]].iloc[j] == '-'):
                       statsList[n].PlayoffSavePercent = float("NaN")
                   else:
                       statsList[n].PlayoffSavePercent = float(DF[DF.columns[11]].iloc[j])

                   if(DF[DF.columns[12]].iloc[j] == '-'):
                       statsList[n].RegularGA60 = float("NaN")
                   else:
                       statsList[n].RegularGA60 = float(DF[DF.columns[12]].iloc[j])

                   if(DF[DF.columns[13]].iloc[j] == '-'):
                       statsList[n].RegularxGA60 = float("NaN")
                   else:
                       statsList[n].RegularxGA60 = float(DF[DF.columns[13]].iloc[j])

                   if(DF[DF.columns[14]].iloc[j] == '-'):
                       statsList[n].RegularGSAx60 = float("NaN")
                   else:
                       statsList[n].RegularGSAx60 = float(DF[DF.columns[14]].iloc[j])

                   if(DF[DF.columns[17]].iloc[j] == '-'):
                       statsList[n].PlayoffGA60 = float("NaN")
                   else:
                       statsList[n].PlayoffGA60 = float(DF[DF.columns[17]].iloc[j])

                   if(DF[DF.columns[18]].iloc[j] == '-'):
                       statsList[n].PlayoffxGA60 = float("NaN")
                   else:
                       statsList[n].PlayoffxGA60 = float(DF[DF.columns[18]].iloc[j])

                   if(DF[DF.columns[19]].iloc[j] == '-'):
                       statsList[n].PlayoffGSAx60 = float("NaN")
                   else:
                       statsList[n].PlayoffGSAx60 = float(DF[DF.columns[19]].iloc[j])


               n = n+1

        # Append this to player
        ActivePlayerList[i].StatHistory = statsList
        i = i + 1;





    print("     " + str(int((i+1)*100/len(ActivePlayerList))) + "% complete")

    print("Done retrieving stats from CapFriendly.")

    

    return ActivePlayerList




def GetSalaryCapFromCapFriendly():
   print("Getting data from CapFriendly...")

   SalaryCapTable = []

   L = pd.read_html("https://www.capfriendly.com/salary-cap")

   # Convert list to data frame. This list only has one dataframe. 
   DF = L[0]

   n = len(DF["SEASON"])

   Seasons = np.zeros(n, dtype = int)
   UpperLimits = np.zeros(n, dtype = int)
   MinSalary = np.zeros(n, dtype = int)

   for i in range(n):

       # Only grab 1st year of seasons (4 first characters)
       s = DF["SEASON"].iloc[i]
       s = s[0:4]
       Seasons[i] = int(s)

       # Remove $ and , from dollar value
       s = DF["UPPER LIMIT"].iloc[i]
       s = s.replace("$", "")
       s = s.replace(",", "")
       UpperLimits[i] = int(s)

       # Remove $ and , from dollar value
       s = DF["MIN. SALARY"].iloc[i]
       s = s.replace("$", "")
       s = s.replace(",", "")
       MinSalary[i] = int(s)

   print("Done retrieving data from CapFriendly.")

   SalaryCapTable = {
       "Seasons" : Seasons, 
       "Upper Cap" : UpperLimits,  
       "Min Salary" : MinSalary 
   }

   return SalaryCapTable