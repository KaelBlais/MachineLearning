# This file will house the necessary functions to convert the contract entries 
# into a contract list and a training set


from ContractStructure import *
import numpy as np

# This function will take in a player list and create contract entries for each valid contract in the player list
# The returned list will maintain the original order. This will need to be randomized later before 
# getting converted into a training/test set.
def CreateContractList(PlayerList, SalaryCapTable, TeamStatsList, CurrentYear):
    ContractList = []

    print("Creating Contract List...")

    # Note that the cutoff year represents the earliest year where new contracts can be used
    # Since the team list only covers up to the start of the salary cap era, and we need 3 years of team history
    # prior to the contract, only contracts signed at least 3 years after the start of salary cap era will be used. 
    # In the future, the team list could be changed to cover 3 years before the salary cap era to add more data. 
    # For now, this is left as is. It's not the worst thing to add a bit of a buffer after the introduction of the salary cap
    # and focus on recent years instead. 
    CutoffYear = TeamStatsList[len(TeamStatsList) - 4].year
    for player in PlayerList:
        if(player.Position != "G"): # Ignore goalies for now
            for i in range(1, player.NumContracts): # Always skip first contract (ELC) 
                if(player.ContractDates[i] >= CutoffYear):
                    # Found a valid contract, enter it in list
                    c = CreateContractEntry(player, player.ContractDates[i], SalaryCapTable, TeamStatsList, \
                        CurrentYear, player.ContractLength[i], player.ContractAAV[i])
                    ContractList.append(c)


    print("Done Creating Contract List.")

    return ContractList


# This function will take in a contract list and create the corresponding feature matrix X and 
# output vector Y (salary). Note that the X values will not be normalized.
# X will be an n x m column vector where n is the number of features and m is the number of contracts
def CreateFeatureMatrix(ContractList):
    m = len(ContractList)
    n = len(FeatureNames)

    X = np.zeros((n, m))
    Y = np.zeros((1, m))

    for i in range(m):
        x, y = CreateFeatureVector(ContractList[i])
        X[:, i] = np.squeeze(x) # column vector needs to be reshaped to (n, :) from (n, 1) before getting copied to matrix
        Y[:, i] = y

    assert(np.shape(X) == (n, m))
    assert(np.shape(Y) == (1, m))

    return X, Y


# This will host the names of all features in the same order as the feature vectors.
# This will be used to debug and plot individual features
FeatureNames = [
                "Contract Duration", "Player Age", "Position == LD", "Position == RD", 
                "Position == LW", "Position == RW", "Position == C", 
                
                "Last Year Games Played (Regular Season)", "Last Year Goals (Regular Season)",
                "Last Year Assists (Regular Season)", "Last Year +/- (Regular Season)", "Last Year PIM (Regular Season)", "Last Year Even Strength TOI (Regular Season)",
                "Last Year Even Strength Goals (Regular Season)","Last Year Individual Expected Goals (Regular Season)","Last Expected Goal Differential Per 60 Minutes (Regular Season)",
                "Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Regular Season)","Last Year Corsi Differential per 60 Minutes (Regular Season)",
                "Last Year Corsi Differential Relative to Teammates per 60 Minutes (Regular Season)",
                
                "Last Year Games Played (Playoffs)", "Last Year Goals (Playoffs)",
                "Last Year Assists (Playoffs)", "Last Year +/- (Playoffs)", "Last Year PIM (Playoffs)", "Last Year Even Strength TOI (Playoffs)",
                "Last Year Even Strength Goals (Playoffs)","Last Year Individual Expected Goals (Playoffs)","Last Expected Goal Differential Per 60 Minutes (Playoffs)",
                "Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Playoffs)","Last Year Corsi Differential per 60 Minutes (Playoffs)",
                "Last Year Corsi Differential Relative to Teammates per 60 Minutes (Playoffs)",

                "2nd Last Year Games Played (Regular Season)", "2nd Last Year Goals (Regular Season)",
                "2nd Last Year Assists (Regular Season)", "2nd Last Year +/- (Regular Season)", "2nd Last Year PIM (Regular Season)", "2nd Last Year Even Strength TOI (Regular Season)",
                "2nd Last Year Even Strength Goals (Regular Season)","2nd Last Year Individual Expected Goals (Regular Season)","Last Expected Goal Differential Per 60 Minutes (Regular Season)",
                "2nd Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Regular Season)","2nd Last Year Corsi Differential per 60 Minutes (Regular Season)",
                "2nd Last Year Corsi Differential Relative to Teammates per 60 Minutes (Regular Season)",
                
                "2nd Last Year Games Played (Playoffs)", "2nd Last Year Goals (Playoffs)",
                "2nd Last Year Assists (Playoffs)", "2nd Last Year +/- (Playoffs)", "2nd Last Year PIM (Playoffs)", "2nd Last Year Even Strength TOI (Playoffs)",
                "2nd Last Year Even Strength Goals (Playoffs)","2nd Last Year Individual Expected Goals (Playoffs)","Last Expected Goal Differential Per 60 Minutes (Playoffs)",
                "2nd Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Playoffs)","2nd Last Year Corsi Differential per 60 Minutes (Playoffs)",
                "2nd Last Year Corsi Differential Relative to Teammates per 60 Minutes (Playoffs)",

                "3rd Last Year Games Played (Regular Season)", "3rd Last Year Goals (Regular Season)",
                "3rd Last Year Assists (Regular Season)", "3rd Last Year +/- (Regular Season)", "3rd Last Year PIM (Regular Season)", "3rd Last Year Even Strength TOI (Regular Season)",
                "3rd Last Year Even Strength Goals (Regular Season)","3rd Last Year Individual Expected Goals (Regular Season)","Last Expected Goal Differential Per 60 Minutes (Regular Season)",
                "3rd Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Regular Season)","3rd Last Year Corsi Differential per 60 Minutes (Regular Season)",
                "3rd Last Year Corsi Differential Relative to Teammates per 60 Minutes (Regular Season)",
                
                "3rd Last Year Games Played (Playoffs)", "3rd Last Year Goals (Playoffs)",
                "3rd Last Year Assists (Playoffs)", "3rd Last Year +/- (Playoffs)", "3rd Last Year PIM (Playoffs)", "3rd Last Year Even Strength TOI (Playoffs)",
                "3rd Last Year Even Strength Goals (Playoffs)","3rd Last Year Individual Expected Goals (Playoffs)","Last Expected Goal Differential Per 60 Minutes (Playoffs)",
                "3rd Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Playoffs)","3rd Last Year Corsi Differential per 60 Minutes (Playoffs)",
                "3rd Last Year Corsi Differential Relative to Teammates per 60 Minutes (Playoffs)",

                "Next Year Salary Cap", "Salary Cap in 2 Years", "Salary Cap in 3 Years",
                "Next Year Minimum Salary", "Minimum Salary in 2 Years", "Minimum Salary in 3 Years",

                "Last Year Team Position", "Last Year Team Games Played", "Last Year Team Wins", "Last Year Team Losses",
                "Last Year Team Overtime Losses", "Last Year Team Goals For", "Last Year Team Goals Against", 

                "2nd Last Year Team Position", "2nd Last Year Team Games Played", "2nd Last Year Team Wins", "2nd Last Year Team Losses",
                "2nd Last Year Team Overtime Losses", "2nd Last Year Team Goals For", "2nd Last Year Team Goals Against", 

                "3rd Last Year Team Position", "3rd Last Year Team Games Played", "3rd Last Year Team Wins", "3rd Last Year Team Losses",
                "3rd Last Year Team Overtime Losses", "3rd Last Year Team Goals For", "3rd Last Year Team Goals Against"
                ]



# This function will take in a contract entry and create the corresponding feature vector x and 
# output value y (salary) for that entry. Note that the x values will not be normalized.
# X will be an n x 1 column vector where n is the number of features
def CreateFeatureVector(Contract):

    n = len(FeatureNames)
    x = np.zeros((n, 1))

    x[0] = Contract.NumYears
    x[1] = Contract.PlayerAge
    x[2] = Contract.PlayerPosition == "LD"
    x[3] = Contract.PlayerPosition == "RD"
    x[4] = Contract.PlayerPosition == "LW"
    x[5] = Contract.PlayerPosition == "RW"
    x[6] = Contract.PlayerPosition == "C"

    # Stats from last regular season
    x[7] = Contract.Year1RegSeasonGP
    x[8] = Contract.Year1RegSeasonG
    x[9] = Contract.Year1RegSeasonA
    x[10] = Contract.Year1RegSeasonPlusMinus
    x[11] = Contract.Year1RegSeasonPIM
    x[12] = Contract.Year1RegSeasonEVTOI
    x[13] = Contract.Year1RegSeasonEVG
    x[14] = Contract.Year1RegSeasonixG
    x[15] = Contract.Year1RegSeasonxG60
    x[16] = Contract.Year1RegSeasonRelxG60
    x[17] = Contract.Year1RegSeasonC60
    x[18] = Contract.Year1RegSeasonRelC60

    # Stats from last playoffs
    x[19] = Contract.Year1PlayoffsGP
    x[20] = Contract.Year1PlayoffsG
    x[21] = Contract.Year1PlayoffsA
    x[22] = Contract.Year1PlayoffsPlusMinus
    x[23] = Contract.Year1PlayoffsPIM
    x[24] = Contract.Year1PlayoffsEVTOI
    x[25] = Contract.Year1PlayoffsEVG
    x[26] = Contract.Year1PlayoffsixG
    x[27] = Contract.Year1PlayoffsxG60
    x[28] = Contract.Year1PlayoffsRelxG60
    x[29] = Contract.Year1PlayoffsC60
    x[30] = Contract.Year1PlayoffsRelC60

    # Stats from 2nd last regular season
    x[31] = Contract.Year2RegSeasonGP
    x[32] = Contract.Year2RegSeasonG
    x[33] = Contract.Year2RegSeasonA
    x[34] = Contract.Year2RegSeasonPlusMinus
    x[35] = Contract.Year2RegSeasonPIM
    x[36] = Contract.Year2RegSeasonEVTOI
    x[37] = Contract.Year2RegSeasonEVG
    x[38] = Contract.Year2RegSeasonixG
    x[39] = Contract.Year2RegSeasonxG60
    x[40] = Contract.Year2RegSeasonRelxG60
    x[41] = Contract.Year2RegSeasonC60
    x[42] = Contract.Year2RegSeasonRelC60

    # Stats from 2nd last playoffs
    x[43] = Contract.Year2PlayoffsGP
    x[44] = Contract.Year2PlayoffsG
    x[45] = Contract.Year2PlayoffsA
    x[46] = Contract.Year2PlayoffsPlusMinus
    x[47] = Contract.Year2PlayoffsPIM
    x[48] = Contract.Year2PlayoffsEVTOI
    x[49] = Contract.Year2PlayoffsEVG
    x[50] = Contract.Year2PlayoffsixG
    x[51] = Contract.Year2PlayoffsxG60
    x[52] = Contract.Year2PlayoffsRelxG60
    x[53] = Contract.Year2PlayoffsC60
    x[54] = Contract.Year2PlayoffsRelC60

    # Stats from 3rd last regular season
    x[55] = Contract.Year3RegSeasonGP
    x[56] = Contract.Year3RegSeasonG
    x[57] = Contract.Year3RegSeasonA
    x[58] = Contract.Year3RegSeasonPlusMinus
    x[59] = Contract.Year3RegSeasonPIM
    x[60] = Contract.Year3RegSeasonEVTOI
    x[61] = Contract.Year3RegSeasonEVG
    x[62] = Contract.Year3RegSeasonixG
    x[63] = Contract.Year3RegSeasonxG60
    x[64] = Contract.Year3RegSeasonRelxG60
    x[65] = Contract.Year3RegSeasonC60
    x[66] = Contract.Year3RegSeasonRelC60

    # Stats from 3rd last playoffs
    x[67] = Contract.Year3PlayoffsGP
    x[68] = Contract.Year3PlayoffsG
    x[69] = Contract.Year3PlayoffsA
    x[70] = Contract.Year3PlayoffsPlusMinus
    x[71] = Contract.Year3PlayoffsPIM
    x[72] = Contract.Year3PlayoffsEVTOI
    x[73] = Contract.Year3PlayoffsEVG
    x[74] = Contract.Year3PlayoffsixG
    x[75] = Contract.Year3PlayoffsxG60
    x[76] = Contract.Year3PlayoffsRelxG60
    x[77] = Contract.Year3PlayoffsC60
    x[78] = Contract.Year3PlayoffsRelC60

    # Salary cap info from next 3 years
    # In this case, year 1 refers to next year instead of last
    x[79] = Contract.Year1Cap
    x[80] = Contract.Year2Cap
    x[81] = Contract.Year3Cap
    x[82] = Contract.Year1MinSalary
    x[83] = Contract.Year2MinSalary
    x[84] = Contract.Year3MinSalary


    # Team stats from last regular season
    x[85] = Contract.Year1TeamPosition
    x[86] = Contract.Year1TeamGP
    x[87] = Contract.Year1TeamWins
    x[88] = Contract.Year1TeamLosses
    x[89] = Contract.Year1TeamOTLosses
    x[90] = Contract.Year1TeamGF
    x[91] = Contract.Year1TeamGA

    # Team stats from 2nd last regular season
    x[92] = Contract.Year2TeamPosition
    x[93] = Contract.Year2TeamGP
    x[94] = Contract.Year2TeamWins
    x[95] = Contract.Year2TeamLosses
    x[96] = Contract.Year2TeamOTLosses
    x[97] = Contract.Year2TeamGF
    x[98] = Contract.Year2TeamGA

    # Team stats from 3rd last regular season
    x[99] = Contract.Year3TeamPosition
    x[100] = Contract.Year3TeamGP
    x[101] = Contract.Year3TeamWins
    x[102] = Contract.Year3TeamLosses
    x[103] = Contract.Year3TeamOTLosses
    x[104] = Contract.Year3TeamGF
    x[105] = Contract.Year3TeamGA

    y = Contract.Salary


    return x, y