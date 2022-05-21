# This file will house the necessary functions to convert the contract entries 
# into a contract list and a training set


from ContractStructure import *

# This function will take in a player list and create contract entries for each valid contract in the player list
# The returned list will maintain the original order. This will need to be randomized later before 
# getting converted into a training/test set.
def CreateContractList(PlayerList, SalaryCapTable, TeamStatsList, CurrentYear):
    ContractList = []

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

    return ContractList
