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
    # This requires 3 years of previous data. Since the team list has 3 years prior to the salary cap year
    # added, this should correspond to the first year of the salary cap era (2005)
    CutoffYear = TeamStatsList[len(TeamStatsList) - 4].year
    assert(CutoffYear == 2005)

    for player in PlayerList:
        if(player.Position != "G"): # Ignore goalies for now

            # To check for valid conditions:
            # This must be from a valid year (salary cap era)
            # This must also exclude ELCs. This is always the contract
            # With the earliest date in the list.
            elcIdx = player.ContractDates.index(min(player.ContractDates))
            for i in range(0, player.NumContracts):
                if(player.ContractDates[i] >= CutoffYear and i != elcIdx):
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

                # Basic Contract Into
                "Contract Duration", "Player Age", "Position == LD", "Position == RD", 
                "Position == LW", "Position == RW", "Position == C", "Resigning With Team",
                "Player Height (cm)", "Player Weight (lbs)", "Draft Position", "Career Earnings to Date ($)",
                "Previous Salary ($)", "Player Age at End of Contract",

                # General Career Stats
                "Career Games Played (Regular Season)", "Career Goals (Regular Season)","Career Assists (Regular Season)", 
                "Career Point (Regular Season)", "Career Point-Per-Game (Regular Season)",
                "Career Games Played (Playoffs)", "Career Goals (Playoffs)","Career Assists (Playoffs)", 
                "Career Point (Playoffs)", "Career Point-Per-Game (Playoffs)",
                

                # Last 3 Years of Player Stats
                "Last Year Games Played (Regular Season)", "Last Year Goals (Regular Season)",
                "Last Year Assists (Regular Season)", "Last Year +/- (Regular Season)", "Last Year PIM (Regular Season)", "Last Year Even Strength TOI (Regular Season)",
                "Last Year Even Strength Goals (Regular Season)","Last Year Individual Expected Goals (Regular Season)","Last Expected Goal Differential Per 60 Minutes (Regular Season)",
                "Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Regular Season)","Last Year Corsi Differential per 60 Minutes (Regular Season)",
                "Last Year Corsi Differential Relative to Teammates per 60 Minutes (Regular Season)",
                "Last Year Point Per Game (Regular Season)", "Last Year Games Played Ratio (Regular Season)", 
                "Last Year Ratio of Team Offense (Regular Season)", "Last Year +/- Compared to Team +/- (Regular Season)",

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
                "2nd Last Year Point Per Game (Regular Season)",  "2nd Last Year Games Played Ratio (Regular Season)", 
                "2nd Last Year Ratio of Team Offense (Regular Season)", "2nd Last Year +/- Compared to Team +/- (Regular Season)", 
                
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
                "3rd Last Year Point Per Game (Regular Season)", "3rd Last Year Games Played Ratio (Regular Season)", 
                "3rd Last Year Ratio of Team Offense (Regular Season)",  "3rd Last Year +/- Compared to Team +/- (Regular Season)", 

                "3rd Last Year Games Played (Playoffs)", "3rd Last Year Goals (Playoffs)",
                "3rd Last Year Assists (Playoffs)", "3rd Last Year +/- (Playoffs)", "3rd Last Year PIM (Playoffs)", "3rd Last Year Even Strength TOI (Playoffs)",
                "3rd Last Year Even Strength Goals (Playoffs)","3rd Last Year Individual Expected Goals (Playoffs)","Last Expected Goal Differential Per 60 Minutes (Playoffs)",
                "3rd Last Year Expected Goal Differential Relative to Teammates per 60 Minutes (Playoffs)","3rd Last Year Corsi Differential per 60 Minutes (Playoffs)",
                "3rd Last Year Corsi Differential Relative to Teammates per 60 Minutes (Playoffs)",

                # Salary Cap Info for Next 3 Years
                "Next Year Salary Cap", "Salary Cap in 2 Years", "Salary Cap in 3 Years",
                "Next Year Minimum Salary", "Minimum Salary in 2 Years", "Minimum Salary in 3 Years",


                # Last 3 years of team stats
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

    idx = 0; # Use idk to keep track of section indexes


    ##### Basic Info ######
    x[idx+0] = Contract.NumYears
    x[idx+1] = Contract.PlayerAge
    x[idx+2] = Contract.PlayerPosition == "LD"
    x[idx+3] = Contract.PlayerPosition == "RD"
    x[idx+4] = Contract.PlayerPosition == "LW"
    x[idx+5] = Contract.PlayerPosition == "RW"
    x[idx+6] = Contract.PlayerPosition == "C"
    x[idx+7] = Contract.Resigning
    x[idx+8] = Contract.PlayerHeight
    x[idx+9] = Contract.PlayerWeight
    if(Contract.PlayerDraftPosition == 0):
        x[idx+10] = 7*32 # If undrafted, set to last position of draft (end of 7th round)
    else:
        x[idx+10] = Contract.PlayerDraftPosition
    x[idx+11] = Contract.EarningsToDate
    x[idx+12] = Contract.PreviousSalary
    x[idx+13] = Contract.PlayerAge + Contract.NumYears # Age at end of contract

    idx = idx + 14

    ##### General Career Statistics #####
    x[idx+0] = Contract.CareerRegularGP
    x[idx+1] = Contract.CareerRegularGoals
    x[idx+2] = Contract.CareerRegularAssists
    x[idx+3] = Contract.CareerRegularPoints
    x[idx+4] = Contract.CareerRegularPPG
    x[idx+5] = Contract.CareerPlayoffsGP
    x[idx+6] = Contract.CareerPlayoffsGoals
    x[idx+7] = Contract.CareerPlayoffsAssists
    x[idx+8] = Contract.CareerPlayoffsPoints
    x[idx+9] = Contract.CareerPlayoffsPPG

    idx = idx + 10

    ##### Stats from last regular season ######
    x[idx+0] = Contract.Year1RegSeasonGP
    x[idx+1] = Contract.Year1RegSeasonG
    x[idx+2] = Contract.Year1RegSeasonA
    x[idx+3] = Contract.Year1RegSeasonPlusMinus
    x[idx+4] = Contract.Year1RegSeasonPIM
    x[idx+5] = Contract.Year1RegSeasonEVTOI
    x[idx+6] = Contract.Year1RegSeasonEVG
    x[idx+7] = Contract.Year1RegSeasonixG
    x[idx+8] = Contract.Year1RegSeasonxG60
    x[idx+9] = Contract.Year1RegSeasonRelxG60
    x[idx+10] = Contract.Year1RegSeasonC60
    x[idx+11] = Contract.Year1RegSeasonRelC60

    # Points per game. If player didn't play, set ratio to 0
    if(Contract.Year1RegSeasonGP == 0):
        x[idx+12] = 0
    else:
        x[idx+12] = (Contract.Year1RegSeasonG + Contract.Year1RegSeasonA) / Contract.Year1RegSeasonGP 


    # Ratio of games played. If the team didn't play games, set ratio to 1
    if(Contract.Year1TeamGP == 0):
        x[idx+13] = 1
    else:
        x[idx+13] = Contract.Year1RegSeasonGP / Contract.Year1TeamGP 

    # Ratio of team offense generated. If team didn't score any goals, set ratio to 0
    if(Contract.Year1TeamGF == 0):
        x[idx+14] = 0
    else:
        x[idx+14] = (Contract.Year1RegSeasonG + Contract.Year1RegSeasonA) / Contract.Year1TeamGF 

    # Difference between player +/- and team +/-
    x[idx+15] = Contract.Year1RegSeasonPlusMinus - (Contract.Year1TeamGF -  Contract.Year1TeamGA)

    idx = idx + 16

    ##### Stats from last playoffs #####
    x[idx+0] = Contract.Year1PlayoffsGP
    x[idx+1] = Contract.Year1PlayoffsG
    x[idx+2] = Contract.Year1PlayoffsA
    x[idx+3] = Contract.Year1PlayoffsPlusMinus
    x[idx+4] = Contract.Year1PlayoffsPIM
    x[idx+5] = Contract.Year1PlayoffsEVTOI
    x[idx+6] = Contract.Year1PlayoffsEVG
    x[idx+7] = Contract.Year1PlayoffsixG
    x[idx+8] = Contract.Year1PlayoffsxG60
    x[idx+9] = Contract.Year1PlayoffsRelxG60
    x[idx+10] = Contract.Year1PlayoffsC60
    x[idx+11] = Contract.Year1PlayoffsRelC60

    idx = idx + 12

     ##### Stats from 2nd last regular season ######
    x[idx+0] = Contract.Year2RegSeasonGP
    x[idx+1] = Contract.Year2RegSeasonG
    x[idx+2] = Contract.Year2RegSeasonA
    x[idx+3] = Contract.Year2RegSeasonPlusMinus
    x[idx+4] = Contract.Year2RegSeasonPIM
    x[idx+5] = Contract.Year2RegSeasonEVTOI
    x[idx+6] = Contract.Year2RegSeasonEVG
    x[idx+7] = Contract.Year2RegSeasonixG
    x[idx+8] = Contract.Year2RegSeasonxG60
    x[idx+9] = Contract.Year2RegSeasonRelxG60
    x[idx+10] = Contract.Year2RegSeasonC60
    x[idx+11] = Contract.Year2RegSeasonRelC60

    # Points per game. If player didn't play, set ratio to 0
    if(Contract.Year2RegSeasonGP == 0):
        x[idx+12] = 0
    else:
        x[idx+12] = (Contract.Year2RegSeasonG + Contract.Year2RegSeasonA) / Contract.Year2RegSeasonGP 


    # Ratio of games played. If the team didn't play games, set ratio to 1
    if(Contract.Year2TeamGP == 0):
        x[idx+13] = 1
    else:
        x[idx+13] = Contract.Year2RegSeasonGP / Contract.Year2TeamGP 

    # Ratio of team offense generated. If team didn't score any goals, set ratio to 0
    if(Contract.Year2TeamGF == 0):
        x[idx+14] = 0
    else:
        x[idx+14] = (Contract.Year2RegSeasonG + Contract.Year2RegSeasonA) / Contract.Year2TeamGF 

    # Difference between player +/- and team +/-
    x[idx+15] = Contract.Year2RegSeasonPlusMinus - (Contract.Year2TeamGF -  Contract.Year2TeamGA)

    idx = idx + 16

    ##### Stats from 2nd last playoffs #####
    x[idx+0] = Contract.Year2PlayoffsGP
    x[idx+1] = Contract.Year2PlayoffsG
    x[idx+2] = Contract.Year2PlayoffsA
    x[idx+3] = Contract.Year2PlayoffsPlusMinus
    x[idx+4] = Contract.Year2PlayoffsPIM
    x[idx+5] = Contract.Year2PlayoffsEVTOI
    x[idx+6] = Contract.Year2PlayoffsEVG
    x[idx+7] = Contract.Year2PlayoffsixG
    x[idx+8] = Contract.Year2PlayoffsxG60
    x[idx+9] = Contract.Year2PlayoffsRelxG60
    x[idx+10] = Contract.Year2PlayoffsC60
    x[idx+11] = Contract.Year2PlayoffsRelC60

    idx = idx + 12

     ##### Stats from 3rd last regular season ######
    x[idx+0] = Contract.Year3RegSeasonGP
    x[idx+1] = Contract.Year3RegSeasonG
    x[idx+2] = Contract.Year3RegSeasonA
    x[idx+3] = Contract.Year3RegSeasonPlusMinus
    x[idx+4] = Contract.Year3RegSeasonPIM
    x[idx+5] = Contract.Year3RegSeasonEVTOI
    x[idx+6] = Contract.Year3RegSeasonEVG
    x[idx+7] = Contract.Year3RegSeasonixG
    x[idx+8] = Contract.Year3RegSeasonxG60
    x[idx+9] = Contract.Year3RegSeasonRelxG60
    x[idx+10] = Contract.Year3RegSeasonC60
    x[idx+11] = Contract.Year3RegSeasonRelC60

    # Points per game. If player didn't play, set ratio to 0
    if(Contract.Year3RegSeasonGP == 0):
        x[idx+12] = 0
    else:
        x[idx+12] = (Contract.Year3RegSeasonG + Contract.Year3RegSeasonA) / Contract.Year3RegSeasonGP 


    # Ratio of games played. If the team didn't play games, set ratio to 1
    if(Contract.Year3TeamGP == 0):
        x[idx+13] = 1
    else:
        x[idx+13] = Contract.Year3RegSeasonGP / Contract.Year3TeamGP 

    # Ratio of team offense generated. If team didn't score any goals, set ratio to 0
    if(Contract.Year3TeamGF == 0):
        x[idx+14] = 0
    else:
        x[idx+14] = (Contract.Year3RegSeasonG + Contract.Year3RegSeasonA) / Contract.Year3TeamGF 

    # Difference between player +/- and team +/-
    x[idx+15] = Contract.Year3RegSeasonPlusMinus - (Contract.Year3TeamGF -  Contract.Year3TeamGA)

    idx = idx + 16

    ##### Stats from 3rd last playoffs #####
    x[idx+0] = Contract.Year3PlayoffsGP
    x[idx+1] = Contract.Year3PlayoffsG
    x[idx+2] = Contract.Year3PlayoffsA
    x[idx+3] = Contract.Year3PlayoffsPlusMinus
    x[idx+4] = Contract.Year3PlayoffsPIM
    x[idx+5] = Contract.Year3PlayoffsEVTOI
    x[idx+6] = Contract.Year3PlayoffsEVG
    x[idx+7] = Contract.Year3PlayoffsixG
    x[idx+8] = Contract.Year3PlayoffsxG60
    x[idx+9] = Contract.Year3PlayoffsRelxG60
    x[idx+10] = Contract.Year3PlayoffsC60
    x[idx+11] = Contract.Year3PlayoffsRelC60

    idx = idx + 12

    ##### Salary cap info from next 3 years #####
    # In this case, year 1 refers to next year instead of last
    x[idx+0] = Contract.Year1Cap
    x[idx+1] = Contract.Year2Cap
    x[idx+2] = Contract.Year3Cap
    x[idx+3] = Contract.Year1MinSalary
    x[idx+4] = Contract.Year2MinSalary
    x[idx+5] = Contract.Year3MinSalary

    idx = idx + 6

    ##### Team stats from last regular season #####
    x[idx+0] = Contract.Year1TeamPosition
    x[idx+1] = Contract.Year1TeamGP
    x[idx+2] = Contract.Year1TeamWins
    x[idx+3] = Contract.Year1TeamLosses
    x[idx+4] = Contract.Year1TeamOTLosses
    x[idx+5] = Contract.Year1TeamGF
    x[idx+6] = Contract.Year1TeamGA

    idx = idx + 7

    ##### Team stats from 2nd last regular season #####
    x[idx+0] = Contract.Year2TeamPosition
    x[idx+1] = Contract.Year2TeamGP
    x[idx+2] = Contract.Year2TeamWins
    x[idx+3] = Contract.Year2TeamLosses
    x[idx+4] = Contract.Year2TeamOTLosses
    x[idx+5] = Contract.Year2TeamGF
    x[idx+6] = Contract.Year2TeamGA

    idx = idx + 7

    ##### Team stats from 3rd last regular season #####
    x[idx+0] = Contract.Year3TeamPosition
    x[idx+1] = Contract.Year3TeamGP
    x[idx+2] = Contract.Year3TeamWins
    x[idx+3] = Contract.Year3TeamLosses
    x[idx+4] = Contract.Year3TeamOTLosses
    x[idx+5] = Contract.Year3TeamGF
    x[idx+6] = Contract.Year1TeamGA

    idx = idx + 7
    
    # idx should have reached end of features now
    assert(idx == n)

    # Salary is everything above minimum salary. This will be a better fit for the ReLU model
    # Note that this is stored in millions of dollars. 
    # Keeping it as dollars caused the weights to become too large and the networks became unstable
    # Changing this to millions of dollars (range from 0 to 12) fixed that
    y = (Contract.Salary - Contract.Year1MinSalary) / 1000000;

    return x, y

# This function will take in an input matrix X (dimensions n x m) and 
# find the mean and variance of each feature. The results will be two 
# n x 1 vectors, one for the mean and one for the variance.
def FindFeatureStats(X):
    n = X.shape[0]
    xMean = np.mean(X, axis = 1, keepdims = True)
    xVar = np.var(X, axis = 1, keepdims = True)

    assert(xMean.shape == xVar.shape == (n, 1))

    return xMean, xVar

# This function will take in a feature vector x, a mean vector u and a 
# variance vector var. The result will be the normalized version of x
def NormalizeFeatureVector(X, xMean, xVar):
    XNorm = X - xMean
    XNorm = X / xVar

    # Replace categorical features with original ones.
    # These should remain 0/1
    XNorm[2:8, :] = X[2:8, :]

    return XNorm