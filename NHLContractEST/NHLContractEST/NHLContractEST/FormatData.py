# This file will house the necessary functions to convert the various statistics into
# player contract objects. These objects will then be used to create the feature list of the model


from GetData import *

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
    Year11PlayoffSeasonGP = 0
    Year11PlayoffSeasonG = 0
    Year1PlayoffSeasonA = 0
    Year1PlayoffSeasonPlusMinus = 0
    Year1PlayoffSeasonPIM = 0
    Year1PlayoffSeasonEVTOI = 0
    Year1PlayoffSeasonEVG = 0
    Year1PlayoffSeasonixG = 0
    Year1PlayoffSeasonxG60 = 0
    Year1PlayoffSeasonC60 = 0
    Year1PlayoffSeasonRelC60 = 0
    Year1PlayoffSeasonA = 0

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
    Year2PlayoffSeasonGP = 0
    Year2PlayoffSeasonG = 0
    Year2PlayoffSeasonA = 0
    Year2PlayoffSeasonPlusMinus = 0
    Year2PlayoffSeasonPIM = 0
    Year2PlayoffSeasonEVTOI = 0
    Year2PlayoffSeasonEVG = 0
    Year2PlayoffSeasonixG = 0
    Year2PlayoffSeasonxG60 = 0
    Year2PlayoffSeasonC60 = 0
    Year2PlayoffSeasonRelC60 = 0
    Year2PlayoffSeasonA = 0

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
    Year3PlayoffSeasonGP = 0
    Year3PlayoffSeasonG = 0
    Year3PlayoffSeasonA = 0
    Year3PlayoffSeasonPlusMinus = 0
    Year3PlayoffSeasonPIM = 0
    Year3PlayoffSeasonEVTOI = 0
    Year3PlayoffSeasonEVG = 0
    Year3PlayoffSeasonixG = 0
    Year3PlayoffSeasonxG60 = 0
    Year3PlayoffSeasonC60 = 0
    Year3PlayoffSeasonRelC60 = 0
    Year3PlayoffSeasonA = 0

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


    return c
