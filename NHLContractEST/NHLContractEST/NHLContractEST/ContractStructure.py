# This file will house the necessary functions to convert the various statistics into
# player contract objects. These objects will then be used to create the feature list of the model


from GetData import *
from Util import *
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
    Resigning = 0
    PreviousTeam = ""
    NewTeam = ""
    PlayerHeight = 0
    PlayerWeight = 0
    PlayerDraftPosition = 0
    EarningsToDate = 0
    PreviousSalary = 0

    # General Career Stats
    CareerRegularGP = 0
    CareerRegularGoals = 0
    CareerRegularAssists = 0
    CareerRegularPoints = 0
    CareerRegularPPG = 0
    CareerPlayoffsGP = 0
    CareerPlayoffsGoals = 0
    CareerPlayoffsAssists = 0
    CareerPlayoffsPoints = 0
    CareerPlayoffsPPG = 0

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
    Year1RegSeasonRelxG60 = 0
    Year1RegSeasonC60 = 0
    Year1RegSeasonRelC60 = 0

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
    Year1PlayoffsRelxG60 = 0
    Year1PlayoffsC60 = 0
    Year1PlayoffsRelC60 = 0

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
    Year2RegSeasonRelxG60 = 0
    Year2RegSeasonC60 = 0
    Year2RegSeasonRelC60 = 0

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
    Year2PlayoffsRelxG60 = 0
    Year2PlayoffsC60 = 0
    Year2PlayoffsRelC60 = 0

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
    Year3RegSeasonRelxG60 = 0
    Year3RegSeasonC60 = 0
    Year3RegSeasonRelC60 = 0

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
    Year3PlayoffsRelxG60 = 0
    Year3PlayoffsC60 = 0
    Year3PlayoffsRelC60 = 0

    # Salary cap info from next 3 years
    # In this case, year 1 refers to next year instead of last
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
    c.PlayerHeight = Player.Height
    c.PlayerWeight = Player.Weight
    c.PlayerDraftPosition = Player.DraftPosition

    # Since we are only looking at 2nd contracts and higher, no player should ever be younger than 20
    # Technically this should be 21 but 20 is used in case of rounding errors with calculating age from current year
    assert(c.PlayerAge >= 20)



    # Find previous salary and career earnings
    cDates = Player.ContractDates
    cAAV = Player.ContractAAV
    cLength = Player.ContractLength

    earnings = 0
    closestYearIdx = 0
    for i in range(len(cDates)):
        if(cDates[i] < year):
            earnings = earnings + cAAV[i] * cLength[i]
            if((year - cDates[i]) < (year - cDates[closestYearIdx])):
                closestYearIdx = i


    c.EarningsToDate = earnings
    c.PreviousSalary = cAAV[closestYearIdx]


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

            
            if(seasonYear >= year and year0Index == len(StatHistory)):
                # This is the start of the new contract, marking the end of the old one
                # This is >= instead of > in case a player missed a full NHL year and the index gets skipped
                # In this scenario, the year0 index will be set to the first index it finds that is greater than the current year
                year0Index = i

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


    
    # Compute career stats to date
    totalRegGP = 0
    totalRegG = 0
    totalRegA = 0
    totalPlayoffGP = 0
    totalPlayoffG = 0
    totalPlayoffA = 0
    for i in range (0, year0Index):
        if(math.isnan(StatHistory[i].RegularGP) == False):
            totalRegGP = totalRegGP + StatHistory[i].RegularGP
        if(math.isnan(StatHistory[i].RegularGoals) == False):
            totalRegG = totalRegG + StatHistory[i].RegularGoals
        if(math.isnan(StatHistory[i].RegularAssists) == False):
            totalRegA = totalRegA + StatHistory[i].RegularAssists
        if(math.isnan(StatHistory[i].PlayoffGP) == False):
            totalPlayoffGP = totalPlayoffGP + StatHistory[i].PlayoffGP
        if(math.isnan(StatHistory[i].PlayoffGoals) == False):
            totalPlayoffG = totalPlayoffG + StatHistory[i].PlayoffGoals
        if(math.isnan(StatHistory[i].PlayoffAssists) == False):
            totalPlayoffA = totalPlayoffA + StatHistory[i].PlayoffAssists

    c.CareerRegularGP = totalRegGP
    c.CareerRegularGoals = totalRegG
    c.CareerRegularAssists = totalRegA
    c.CareerRegularPoints = totalRegG + totalRegA
    if(totalRegGP == 0):
        c.CareerRegularPPG = 0
    else: 
        c.CareerRegularPPG = (totalRegG + totalRegA) / totalRegGP
      
    c.CareerPlayoffsGP = totalPlayoffGP
    c.CareerPlayoffsGoals = totalPlayoffG
    c.CareerPlayoffsAssists = totalPlayoffA
    c.CareerPlayoffsPoints = totalPlayoffG + totalPlayoffA
    if(totalPlayoffGP == 0):
        c.CareerPlayoffsPPG = 0
    else: 
        c.CareerPlayoffsPPG = (totalPlayoffG + totalPlayoffA) / totalPlayoffGP 


    # Process years with valid indeces. 
    # Note that an invalid index means a year with no NHL games played
    # In those cases, it is ok to leave all stats at 0
    if(year1Index != -1):

        # All of these indeces correspond to year 1 stats
        # Most of the time, this should only be one or no entries. 
        # However, if a player gets traded halfway through the year, 
        # This will be multiple entries
        # For multiple entries, some values will be added (e.g. goals, assists, etc.)
        # and some will be averaged (e.g. time on ice, goals per 60 etc.)
        for i in range(year1Index, year0Index):
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

        # Now handle all entries that need to be averaged
        # These will be weighted by how many games the player played for each team
        for i in range(year1Index, year0Index):

            if(c.Year1RegSeasonGP == 0 or math.isnan(StatHistory[i].RegularGP) == True):
                ratio = 0 # If there are no GP, all entries will be 0 anyways
            else:
                ratio = StatHistory[i].RegularGP / c.Year1RegSeasonGP

            if(math.isnan(StatHistory[i].RegularxG60) == False):
               c.Year1RegSeasonxG60 += ratio * StatHistory[i].RegularxG60

            if(math.isnan(StatHistory[i].RegularRelxG60) == False):
               c.Year1RegSeasonRelxG60 += ratio * StatHistory[i].RegularRelxG60

            if(math.isnan(StatHistory[i].RegularC60) == False):
               c.Year1RegSeasonC60 += ratio * StatHistory[i].RegularC60

            if(math.isnan(StatHistory[i].RegularRelC60) == False):
               c.Year1RegSeasonRelC60 += ratio * StatHistory[i].RegularRelC60


            # TOI has to be converted to number of seconds first

            # Check if this is even a valid number
            try: 

                # First 2 digits are minutes
                numSec = int(StatHistory[i].RegularEVTOI[0:2])
                numSec *= 60;
                numSec += int(StatHistory[i].RegularEVTOI[3:5])

            except:
                numSec = 0

            c.Year1RegSeasonEVTOI += numSec * ratio

            # Now use the same ratio for team stats
            TeamName = RenameOldTeam(StatHistory[i].Team)

            # Need to find the right index for this year.
            # This does not necessarily correspond to the index in StatHistory since that one can have multiple
            # entries per year.

            rank = -1 # Invalid Entry
            for j in range(0, len(TeamStatsList)):
                if(TeamStatsList[j].year == year - 1): # Last year
                    rank = TeamStatsList[j].TeamList.index(TeamName)
                    c.Year1TeamPosition += rank * ratio
                    c.Year1TeamGP += TeamStatsList[j].GPList[rank] * ratio
                    c.Year1TeamWins += TeamStatsList[j].WinList[rank] * ratio
                    c.Year1TeamLosses += TeamStatsList[j].LossList[rank] * ratio
                    c.Year1TeamOTLosses += TeamStatsList[j].OTLossList[rank] * ratio
                    c.Year1TeamGF += TeamStatsList[j].GFList[rank] * ratio
                    c.Year1TeamGA += TeamStatsList[j].GAList[rank] * ratio

            if(rank == -1):
                print("\nERROR: Team stats could not be retrieved. This contract is invalid\n")


            # Playoff entries are handled the same way
            # This isn't technically necessary since it's impossible for a player 
            # to play on multiple teams in the playoffs. 
            # Simply set up in here for organization's sake.
            if(c.Year1PlayoffsGP == 0 or math.isnan(StatHistory[i].PlayoffGP) == True):
                ratio = 0 # If there are no GP, all entries will be 0 anyways
            else:
                ratio = StatHistory[i].PlayoffGP / c.Year1PlayoffsGP

            if(math.isnan(StatHistory[i].PlayoffxG60) == False):
               c.Year1PlayoffsxG60 += ratio * StatHistory[i].PlayoffxG60

            if(math.isnan(StatHistory[i].PlayoffRelxG60) == False):
               c.Year1PlayoffsRelxG60 += ratio * StatHistory[i].PlayoffRelxG60

            if(math.isnan(StatHistory[i].PlayoffC60) == False):
               c.Year1PlayoffsC60 += ratio * StatHistory[i].PlayoffC60

            if(math.isnan(StatHistory[i].PlayoffRelC60) == False):
               c.Year1PlayoffsRelC60 += ratio * StatHistory[i].PlayoffRelC60

            # Check if this is even a valid number
            try: 

                # First 2 digits are minutes
                numSec = int(StatHistory[i].PlayoffEVTOI[0:2])
                numSec *= 60;
                numSec += int(StatHistory[i].PlayoffEVTOI[3:5])

            except:
                numSec = 0

            c.Year1PlayoffsEVTOI += numSec * ratio

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


        # Now handle all entries that need to be averaged
        # These will be weighted by how many games the player played for each team
        for i in range(year2Index, year1Index):

            if(c.Year2RegSeasonGP == 0 or math.isnan(StatHistory[i].RegularGP) == True):
                ratio = 0 # If there are no GP, all entries will be 0 anyways
            else:
                ratio = StatHistory[i].RegularGP / c.Year2RegSeasonGP

            if(math.isnan(StatHistory[i].RegularxG60) == False):
               c.Year2RegSeasonxG60 += ratio * StatHistory[i].RegularxG60

            if(math.isnan(StatHistory[i].RegularRelxG60) == False):
               c.Year2RegSeasonRelxG60 += ratio * StatHistory[i].RegularRelxG60

            if(math.isnan(StatHistory[i].RegularC60) == False):
               c.Year2RegSeasonC60 += ratio * StatHistory[i].RegularC60

            if(math.isnan(StatHistory[i].RegularRelC60) == False):
               c.Year2RegSeasonRelC60 += ratio * StatHistory[i].RegularRelC60


            # TOI has to be converted to number of seconds first

            # Check if this is even a valid number
            try: 

                # First 2 digits are minutes
                numSec = int(StatHistory[i].RegularEVTOI[0:2])
                numSec *= 60;
                numSec += int(StatHistory[i].RegularEVTOI[3:5])

            except:
                numSec = 0

            c.Year2RegSeasonEVTOI += numSec * ratio

            # Now use the same ratio for team stats
            TeamName = RenameOldTeam(StatHistory[i].Team)

            # Need to find the right index for this year.
            # This does not necessarily correspond to the index in StatHistory since that one can have multiple
            # entries per year.

            rank = -1 # Invalid Entry
            for j in range(0, len(TeamStatsList)):
                if(TeamStatsList[j].year == year - 2): 
                    rank = TeamStatsList[j].TeamList.index(TeamName)
                    c.Year2TeamPosition += rank * ratio
                    c.Year2TeamGP += TeamStatsList[j].GPList[rank] * ratio
                    c.Year2TeamWins += TeamStatsList[j].WinList[rank] * ratio
                    c.Year2TeamLosses += TeamStatsList[j].LossList[rank] * ratio
                    c.Year2TeamOTLosses += TeamStatsList[j].OTLossList[rank] * ratio
                    c.Year2TeamGF += TeamStatsList[j].GFList[rank] * ratio
                    c.Year2TeamGA += TeamStatsList[j].GAList[rank] * ratio

            if(rank == -1):
                print("\nERROR: Team stats could not be retrieved. This contract is invalid\n")
    

            # Playoff entries are handled the same way
            # This isn't technically necessary since it's impossible for a player 
            # to play on multiple teams in the playoffs. 
            # Simply set up in here for organization's sake.
            if(c.Year2PlayoffsGP == 0 or math.isnan(StatHistory[i].PlayoffGP) == True):
                ratio = 0 # If there are no GP, all entries will be 0 anyways
            else:
                ratio = StatHistory[i].PlayoffGP / c.Year2PlayoffsGP

            if(math.isnan(StatHistory[i].PlayoffxG60) == False):
               c.Year2PlayoffsxG60 += ratio * StatHistory[i].PlayoffxG60

            if(math.isnan(StatHistory[i].PlayoffRelxG60) == False):
               c.Year2PlayoffsRelxG60 += ratio * StatHistory[i].PlayoffRelxG60

            if(math.isnan(StatHistory[i].PlayoffC60) == False):
               c.Year2PlayoffsC60 += ratio * StatHistory[i].PlayoffC60

            if(math.isnan(StatHistory[i].PlayoffRelC60) == False):
               c.Year2PlayoffsRelC60 += ratio * StatHistory[i].PlayoffRelC60

            # Check if this is even a valid number
            try: 

                # First 2 digits are minutes
                numSec = int(StatHistory[i].PlayoffEVTOI[0:2])
                numSec *= 60;
                numSec += int(StatHistory[i].PlayoffEVTOI[3:5])

            except:
                numSec = 0

            c.Year2PlayoffsEVTOI += numSec * ratio


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


        # Now handle all entries that need to be averaged
        # These will be weighted by how many games the player played for each team
        for i in range(year3Index, year2Index):

            if(c.Year3RegSeasonGP == 0 or math.isnan(StatHistory[i].RegularGP) == True):
                ratio = 0 # If there are no GP, all entries will be 0 anyways
            else:
                ratio = StatHistory[i].RegularGP / c.Year3RegSeasonGP

            if(math.isnan(StatHistory[i].RegularxG60) == False):
               c.Year3RegSeasonxG60 += ratio * StatHistory[i].RegularxG60

            if(math.isnan(StatHistory[i].RegularRelxG60) == False):
               c.Year3RegSeasonRelxG60 += ratio * StatHistory[i].RegularRelxG60

            if(math.isnan(StatHistory[i].RegularC60) == False):
               c.Year3RegSeasonC60 += ratio * StatHistory[i].RegularC60

            if(math.isnan(StatHistory[i].RegularRelC60) == False):
               c.Year3RegSeasonRelC60 += ratio * StatHistory[i].RegularRelC60


            # TOI has to be converted to number of seconds first

            # Check if this is even a valid number
            try: 

                # First 2 digits are minutes
                numSec = int(StatHistory[i].RegularEVTOI[0:2])
                numSec *= 60;
                numSec += int(StatHistory[i].RegularEVTOI[3:5])

            except:
                numSec = 0

            c.Year3RegSeasonEVTOI += numSec * ratio


            # Now use the same ratio for team stats
            TeamName = RenameOldTeam(StatHistory[i].Team)

            # Need to find the right index for this year.
            # This does not necessarily correspond to the index in StatHistory since that one can have multiple
            # entries per year.

            rank = -1 # Invalid Entry
            for j in range(0, len(TeamStatsList)):
                if(TeamStatsList[j].year == year - 3):
                    rank = TeamStatsList[j].TeamList.index(TeamName)
                    c.Year3TeamPosition += rank * ratio
                    c.Year3TeamGP += TeamStatsList[j].GPList[rank] * ratio
                    c.Year3TeamWins += TeamStatsList[j].WinList[rank] * ratio
                    c.Year3TeamLosses += TeamStatsList[j].LossList[rank] * ratio
                    c.Year3TeamOTLosses += TeamStatsList[j].OTLossList[rank] * ratio
                    c.Year3TeamGF += TeamStatsList[j].GFList[rank] * ratio
                    c.Year3TeamGA += TeamStatsList[j].GAList[rank] * ratio

            if(rank == -1):
                print("\nERROR: Team stats could not be retrieved. This contract is invalid\n")

            # Playoff entries are handled the same way
            # This isn't technically necessary since it's impossible for a player 
            # to play on multiple teams in the playoffs. 
            # Simply set up in here for organization's sake.
            if(c.Year3PlayoffsGP == 0 or math.isnan(StatHistory[i].PlayoffGP) == True):
                ratio = 0 # If there are no GP, all entries will be 0 anyways
            else:
                ratio = StatHistory[i].PlayoffGP / c.Year3PlayoffsGP

            if(math.isnan(StatHistory[i].PlayoffxG60) == False):
               c.Year3PlayoffsxG60 += ratio * StatHistory[i].PlayoffxG60

            if(math.isnan(StatHistory[i].PlayoffRelxG60) == False):
               c.Year3PlayoffsRelxG60 += ratio * StatHistory[i].PlayoffRelxG60

            if(math.isnan(StatHistory[i].PlayoffC60) == False):
               c.Year3PlayoffsC60 += ratio * StatHistory[i].PlayoffC60

            if(math.isnan(StatHistory[i].PlayoffRelC60) == False):
               c.Year3PlayoffsRelC60 += ratio * StatHistory[i].PlayoffRelC60

            # Check if this is even a valid number
            try: 

                # First 2 digits are minutes
                numSec = int(StatHistory[i].PlayoffEVTOI[0:2])
                numSec *= 60;
                numSec += int(StatHistory[i].PlayoffEVTOI[3:5])

            except:
                numSec = 0

            c.Year3PlayoffsEVTOI += numSec * ratio

    # Now fill in previous and new team values
    # Note that if index is end of list, the player has yet to play for his new contract
    # In that case, assume new team is the same as current team
    # If there is no year0 nor year 1 index, new team is N/A
    if(year0Index < len(StatHistory) and len(StatHistory) > 0):
        c.NewTeam = StatHistory[year0Index].Team
    elif (year1Index >= 0):
        c.NewTeam = StatHistory[year1Index].Team
    else:
        c.NewTeam = "N/A"


    # If there is no previous year, player has yet to play in the NHL
    # In that case, assume previous team is current team
    if(year1Index >= 0):
        c.PreviousTeam = StatHistory[year1Index].Team
    else:
        c.PreviousTeam = c.NewTeam


    if(c.NewTeam == c.PreviousTeam):
        c.Resigning = 1
    else:
        c.Resigning = 0



    # Lastly, add salary cap info for next 3 years
    seasons = SalaryCapTable["Seasons"]
        
    for i in range(0, len(seasons)):
        if(seasons[i] == year):
            # Next season's cap starts at this current offseason year
            c.Year1Cap = float(SalaryCapTable["Upper Cap"][i])
            c.Year1MinSalary = float(SalaryCapTable["Min Salary"][i])

        if(seasons[i] == year + 1):
            c.Year2Cap = float(SalaryCapTable["Upper Cap"][i])
            c.Year2MinSalary = float(SalaryCapTable["Min Salary"][i])

        if(seasons[i] == year + 2):
            c.Year3Cap = float(SalaryCapTable["Upper Cap"][i])
            c.Year3MinSalary = float(SalaryCapTable["Min Salary"][i])
            

    assert(c.Year1Cap != 0 and c.Year2Cap != 0 and c.Year3Cap != 0)

    return c
