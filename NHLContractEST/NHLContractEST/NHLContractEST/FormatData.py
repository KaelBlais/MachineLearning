# This file will house the necessary functions to convert the various statistics into
# player contract objects. These objects will then be used to create the feature list of the model


from GetData import *
import math

class ContractEntry:
    def __init__(self, Name, year):
        self.Name = Name
        self.year = year

    # Basic contract info
    NumYears = 0
    Salary = 0 # This entry will eventually become the output of the predictor
    PlayerAge = 0
    PlayerPosition = ""


    # Stats from last regular season
    Year1RegSeasonGP = 0
    Year1RegSeasonG = 0
    Year1RegSeasonA = 0
    Year1RegSeasonPlusMinus = 0
    Year1RegSeasonPIM = 0
    Year1RegSeasonEVTOI = 0
    Year1RegSeasonEVG = 0
    Year1RegSeasonixG = 0
    Year1RegSeasonxG60 = 0
    Year1RegSeasonC60 = 0
    Year1RegSeasonRelC60 = 0
    Year1RegSeasonA = 0

    # Stats from last playoffs
    Year1PlayoffsGP = 0
    Year1PlayoffsG = 0
    Year1PlayoffsA = 0
    Year1PlayoffsPlusMinus = 0
    Year1PlayoffsPIM = 0
    Year1PlayoffsEVTOI = 0
    Year1PlayoffsEVG = 0
    Year1PlayoffsixG = 0
    Year1PlayoffsxG60 = 0
    Year1PlayoffsC60 = 0
    Year1PlayoffsRelC60 = 0
    Year1PlayoffsA = 0

    # Stats from 2nd last regular season
    Year2RegSeasonGP = 0
    Year2RegSeasonG = 0
    Year2RegSeasonA = 0
    Year2RegSeasonPlusMinus = 0
    Year2RegSeasonPIM = 0
    Year2RegSeasonEVTOI = 0
    Year2RegSeasonEVG = 0
    Year2RegSeasonixG = 0
    Year2RegSeasonxG60 = 0
    Year2RegSeasonC60 = 0
    Year2RegSeasonRelC60 = 0
    Year2RegSeasonA = 0

    # Stats from 2nd last playoffs
    Year2PlayoffsGP = 0
    Year2PlayoffsG = 0
    Year2PlayoffsA = 0
    Year2PlayoffsPlusMinus = 0
    Year2PlayoffsPIM = 0
    Year2PlayoffsEVTOI = 0
    Year2PlayoffsEVG = 0
    Year2PlayoffsixG = 0
    Year2PlayoffsxG60 = 0
    Year2PlayoffsC60 = 0
    Year2PlayoffsRelC60 = 0
    Year2PlayoffsA = 0

    # Stats from 3rd last regular season
    Year3RegSeasonGP = 0
    Year3RegSeasonG = 0
    Year3RegSeasonA = 0
    Year3RegSeasonPlusMinus = 0
    Year3RegSeasonPIM = 0
    Year3RegSeasonEVTOI = 0
    Year3RegSeasonEVG = 0
    Year3RegSeasonixG = 0
    Year3RegSeasonxG60 = 0
    Year3RegSeasonC60 = 0
    Year3RegSeasonRelC60 = 0
    Year3RegSeasonA = 0

    # Stats from 3rd last playoffs
    Year3PlayoffsGP = 0
    Year3PlayoffsG = 0
    Year3PlayoffsA = 0
    Year3PlayoffsPlusMinus = 0
    Year3PlayoffsPIM = 0
    Year3PlayoffsEVTOI = 0
    Year3PlayoffsEVG = 0
    Year3PlayoffsixG = 0
    Year3PlayoffsxG60 = 0
    Year3PlayoffsC60 = 0
    Year3PlayoffsRelC60 = 0
    Year3PlayoffsA = 0

    # Salary cap info from last 3 years
    Year1Cap = 0
    Year2Cap = 0
    Year3Cap = 0
    Year1MinSalary = 0
    Year2MinSalary = 0
    Year3MinSalary = 0


    # Team stats from last regular season
    Year1TeamPosition = 0
    Year1TeamGP = 0
    Year1TeamWins = 0
    Year1TeamLosses = 0
    Year1TeamOTLosses = 0
    Year1TeamGF = 0
    Year1TeamGA = 0

    # Team stats from 2nd last regular season
    Year2TeamPosition = 0
    Year2TeamGP = 0
    Year2TeamWins = 0
    Year2TeamLosses = 0
    Year2TeamOTLosses = 0
    Year2TeamGF = 0
    Year2TeamGA = 0

    # Team stats from 3rd last regular season
    Year3TeamPosition = 0
    Year3TeamGP = 0
    Year3TeamWins = 0
    Year3TeamLosses = 0
    Year3TeamOTLosses = 0
    Year3TeamGF = 0
    Year3TeamGA = 0


# This function will take in a player object and a year from which to construct the contract. 
# The contract constructed (Salary and years) must also be specified for training purposes. 
# Note that for prediction purposes, the salary can be left unspecified. 
# Additionally, this will also take in the full team stats list and the salary cap table. 
def CreateContractEntry(Player, year, SalaryCapTable, TeamStatsList, CurrentYear, numYears, Salary = 0):

    # Create basic contract entry
    c = ContractEntry(Player.Name, year)

    # Age at year of contract is current age - how long ago contract was signed
    c.PlayerAge = Player.Age - (CurrentYear - year)
    c.PlayerPosition = Player.Position
    c.NumYears = numYears
    c.Salary = Salary

    # Add season stats. Note that this is only done for skaters right now. Goalies will be handled later

    # First we need to find the right index in the stats table.
    # Note that player seasons are stored in this format: "20xx-20xx"
    # The later year will correspond to the contract year for the last regular season
    StatHistory = Player.StatHistory

    year0Index = len(StatHistory) # This one defaults to end of table
    year1Index = -1 # Default to invalid value
    year2Index = -1 # Default to invalid value
    year3Index = -1 # Default to invalid value

    for i in range (0, len(StatHistory)):
        try: 
            seasonYear = int(StatHistory[i].Year[0:4])

            if(seasonYear == year - 1):
                # This is the last season
                year1Index = i

            if(seasonYear == year - 2):
                # This is the 2nd last season
                year2Index = i

            if(seasonYear == year - 3):
                # This is the 3rd last season
                year3Index = i

            if(seasonYear == year):
                # This is the current season
                # Note that this might not always be found if the year corresponds to the current year
                # In that case, this will grab all stats until the end of the table
                year0Index = i


        except: 
            # Invalid season
            seasonYear = 0


    if(year1Index != -1):
        for i in range(year1Index, year0Index):
            # All of these indeces correspond to year 1 stats
            # Most of the time, this should only be one or no entries. 
            # However, if a player gets traded halfway through the year, 
            # This will be multiple entries
            # For multiple entries, some values will be added (e.g. goals, assists, etc.)
            # and some will be averaged (e.g. time on ice, goals per 60 etc.)

            # First handle all entries that are simply added
            if(math.isnan(StatHistory[i].RegularGP) == False):
               c.Year1RegSeasonGP += StatHistory[i].RegularGP

            if(math.isnan(StatHistory[i].RegularGoals) == False):
               c.Year1RegSeasonG += StatHistory[i].RegularGoals

            if(math.isnan(StatHistory[i].RegularAssists) == False):
               c.Year1RegSeasonA += StatHistory[i].RegularAssists

            if(math.isnan(StatHistory[i].RegularPlusMinus) == False):
               c.Year1RegSeasonPlusMinus += StatHistory[i].RegularPlusMinus

            if(math.isnan(StatHistory[i].RegularPIM) == False):
               c.Year1RegSeasonPIM += StatHistory[i].RegularPIM

            if(math.isnan(StatHistory[i].RegularEVG) == False):
               c.Year1RegSeasonEVG += StatHistory[i].RegularEVG

            if(math.isnan(StatHistory[i].RegularixG) == False):
               c.Year1RegSeasonixG += StatHistory[i].RegularixG

            if(math.isnan(StatHistory[i].PlayoffGP) == False):
               c.Year1PlayoffsGP += StatHistory[i].PlayoffGP

            if(math.isnan(StatHistory[i].PlayoffGoals) == False):
               c.Year1PlayoffsG += StatHistory[i].PlayoffGoals

            if(math.isnan(StatHistory[i].PlayoffAssists) == False):
               c.Year1PlayoffsA += StatHistory[i].PlayoffAssists

            if(math.isnan(StatHistory[i].PlayoffPlusMinus) == False):
               c.Year1PlayoffsPlusMinus += StatHistory[i].PlayoffPlusMinus

            if(math.isnan(StatHistory[i].PlayoffPIM) == False):
               c.Year1PlayoffsPIM += StatHistory[i].PlayoffPIM

            if(math.isnan(StatHistory[i].PlayoffEVG) == False):
               c.Year1PlayoffsEVG += StatHistory[i].PlayoffEVG

            if(math.isnan(StatHistory[i].PlayoffixG) == False):
               c.Year1PlayoffsixG += StatHistory[i].PlayoffixG


    # Do the same thing for the 2nd last year
    if(year2Index != -1):
        for i in range(year2Index, year1Index):

            # First handle all entries that are simply added
            if(math.isnan(StatHistory[i].RegularGP) == False):
               c.Year2RegSeasonGP += StatHistory[i].RegularGP

            if(math.isnan(StatHistory[i].RegularGoals) == False):
               c.Year2RegSeasonG += StatHistory[i].RegularGoals

            if(math.isnan(StatHistory[i].RegularAssists) == False):
               c.Year2RegSeasonA += StatHistory[i].RegularAssists

            if(math.isnan(StatHistory[i].RegularPlusMinus) == False):
               c.Year2RegSeasonPlusMinus += StatHistory[i].RegularPlusMinus

            if(math.isnan(StatHistory[i].RegularPIM) == False):
               c.Year2RegSeasonPIM += StatHistory[i].RegularPIM

            if(math.isnan(StatHistory[i].RegularEVG) == False):
               c.Year2RegSeasonEVG += StatHistory[i].RegularEVG

            if(math.isnan(StatHistory[i].RegularixG) == False):
               c.Year2RegSeasonixG += StatHistory[i].RegularixG

            if(math.isnan(StatHistory[i].PlayoffGP) == False):
               c.Year2PlayoffsGP += StatHistory[i].PlayoffGP

            if(math.isnan(StatHistory[i].PlayoffGoals) == False):
               c.Year2PlayoffsG += StatHistory[i].PlayoffGoals

            if(math.isnan(StatHistory[i].PlayoffAssists) == False):
               c.Year2PlayoffsA += StatHistory[i].PlayoffAssists

            if(math.isnan(StatHistory[i].PlayoffPlusMinus) == False):
               c.Year2PlayoffsPlusMinus += StatHistory[i].PlayoffPlusMinus

            if(math.isnan(StatHistory[i].PlayoffPIM) == False):
               c.Year2PlayoffsPIM += StatHistory[i].PlayoffPIM

            if(math.isnan(StatHistory[i].PlayoffEVG) == False):
               c.Year2PlayoffsEVG += StatHistory[i].PlayoffEVG

            if(math.isnan(StatHistory[i].PlayoffixG) == False):
               c.Year2PlayoffsixG += StatHistory[i].PlayoffixG


    # Do the same thing for the 3rd last year
    if(year3Index != -1):
        for i in range(year3Index, year2Index):

            # First handle all entries that are simply added
            if(math.isnan(StatHistory[i].RegularGP) == False):
               c.Year3RegSeasonGP += StatHistory[i].RegularGP

            if(math.isnan(StatHistory[i].RegularGoals) == False):
               c.Year3RegSeasonG += StatHistory[i].RegularGoals

            if(math.isnan(StatHistory[i].RegularAssists) == False):
               c.Year3RegSeasonA += StatHistory[i].RegularAssists

            if(math.isnan(StatHistory[i].RegularPlusMinus) == False):
               c.Year3RegSeasonPlusMinus += StatHistory[i].RegularPlusMinus

            if(math.isnan(StatHistory[i].RegularPIM) == False):
               c.Year3RegSeasonPIM += StatHistory[i].RegularPIM

            if(math.isnan(StatHistory[i].RegularEVG) == False):
               c.Year3RegSeasonEVG += StatHistory[i].RegularEVG

            if(math.isnan(StatHistory[i].RegularixG) == False):
               c.Year3RegSeasonixG += StatHistory[i].RegularixG

            if(math.isnan(StatHistory[i].PlayoffGP) == False):
               c.Year3PlayoffsGP += StatHistory[i].PlayoffGP

            if(math.isnan(StatHistory[i].PlayoffGoals) == False):
               c.Year3PlayoffsG += StatHistory[i].PlayoffGoals

            if(math.isnan(StatHistory[i].PlayoffAssists) == False):
               c.Year3PlayoffsA += StatHistory[i].PlayoffAssists

            if(math.isnan(StatHistory[i].PlayoffPlusMinus) == False):
               c.Year3PlayoffsPlusMinus += StatHistory[i].PlayoffPlusMinus

            if(math.isnan(StatHistory[i].PlayoffPIM) == False):
               c.Year3PlayoffsPIM += StatHistory[i].PlayoffPIM

            if(math.isnan(StatHistory[i].PlayoffEVG) == False):
               c.Year3PlayoffsEVG += StatHistory[i].PlayoffEVG

            if(math.isnan(StatHistory[i].PlayoffixG) == False):
               c.Year3PlayoffsixG += StatHistory[i].PlayoffixG

    return c
