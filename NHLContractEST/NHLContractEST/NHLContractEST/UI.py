from GetData import *
import sys
from ML import *


playerStatsDefaultFilename = 'PlayerStats.txt'
salaryCapDefaultFilename = 'SalaryCap.txt'
teamStatsDefaultFilename = 'TeamStats.txt'


def GetInputsUI(CurrentYear, LoadDefaults = False):



    # If LoadDefaults is on, UI will be bypassed and default files will be read
    if(LoadDefaults == True):
        ActivePlayerList = ReadFromFile(playerStatsDefaultFilename)
        SalaryCapTable = ReadFromFile(salaryCapDefaultFilename)
        TeamStatsList = ReadFromFile(teamStatsDefaultFilename)

        

        return ActivePlayerList, SalaryCapTable, TeamStatsList
        

    c = input('Load player stats from file? (y/n)')


    while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
        c = input('Invalid input. Load player stats from file? (y/n)')


    if(c == 'y' or c == 'Y'):
        fileName = input('WARNING: This will read using pickle I/O, only use files you trust. Enter q to abort. Please enter name of file to read from: ')
        if(fileName == 'q' or fileName == 'Q'):
            c = input('Read Aborted. Fetch new player stats from CapFriendly? (y/n)')
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                c = input('Invalid Input. Fetch new player stats from CapFriendly? (y/n)')
            if(c == 'y' or c == 'Y'):
                ActivePlayerList = GetPlayerStatsFromCapFriendly(CurrentYear)
                s = 'Save results to "' + playerStatsDefaultFilename + '"? (y/n)'
                c = input(s)
                while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                    s = 'Invalid Input. Save results to "' + playerStatsDefaultFilename + '"? (y/n)'
                    c = input(s)
                if(c == 'y' or c == 'Y'):
                    print('Saving output to ' + str(playerStatsDefaultFilename) + '...')
                    DumpToFile(ActivePlayerList, playerStatsDefaultFilename)

            elif(c == 'n' or c == 'N'):
                print('No data available. Aborting...')
                sys.exit()
        else:
            # Filename available
            ActivePlayerList = ReadFromFile(fileName)

    elif(c == 'n' or c == 'N'):
        c = input('Fetch new player stats from CapFriendly? (y/n)')
        while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
            c = input('Invalid Input. Fetch new player stats from CapFriendly? (y/n)')
        if(c == 'y' or c == 'Y'):
            ActivePlayerList = GetPlayerStatsFromCapFriendly(CurrentYear)
            s = 'Save results to "' + playerStatsDefaultFilename + '"? (y/n)'
            c = input(s)
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                s = 'Invalid Input. Save results to "' + playerStatsDefaultFilename + '"? (y/n)'
                c = input(s)
            if(c == 'y' or c == 'Y'):
                print('Saving output to ' + str(playerStatsDefaultFilename) + '...')
                DumpToFile(ActivePlayerList, playerStatsDefaultFilename)
        elif(c == 'n' or c == 'N'):
            print('No data available. Aborting...')
            sys.exit()



    c = input('Load salary cap data from file? (y/n)')


    while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
        c = input('Invalid input. Load salary cap data from file? (y/n)')


    if(c == 'y' or c == 'Y'):
        fileName = input('WARNING: This will read using pickle I/O, only use files you trust. Enter q to abort. Please enter name of file to read from: ')
        if(fileName == 'q' or fileName == 'Q'):
            c = input('Read Aborted. Fetch new salary cap data from CapFriendly? (y/n)')
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                c = input('Invalid Input. Fetch new salary cap data from CapFriendly? (y/n)')
            if(c == 'y' or c == 'Y'):
                SalaryCapTable = GetSalaryCapFromCapFriendly()
                s = 'Save results to "' + salaryCapDefaultFilename + '"? (y/n)'
                c = input(s)
                while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                    s = 'Invalid Input. Save results to "' + salaryCapDefaultFilename + '"? (y/n)'
                    c = input(s)
                if(c == 'y' or c == 'Y'):
                    print('Saving output to ' + str(salaryCapDefaultFilename) + '...')
                    DumpToFile(SalaryCapTable, salaryCapDefaultFilename)

            elif(c == 'n' or c == 'N'):
                print('No data available. Aborting...')
                sys.exit()
        else:
            # Filename available
            SalaryCapTable = ReadFromFile(fileName)

    elif(c == 'n' or c == 'N'):
        c = input('Fetch new salary cap data from CapFriendly? (y/n)')
        while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
            c = input('Invalid Input. Fetch new salary cap data from CapFriendly? (y/n)')
        if(c == 'y' or c == 'Y'):
            SalaryCapTable = GetSalaryCapFromCapFriendly()
            s = 'Save results to "' + salaryCapDefaultFilename + '"? (y/n)'
            c = input(s)
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                s = 'Invalid Input. Save results to "' + salaryCapDefaultFilename + '"? (y/n)'
                c = input(s)
            if(c == 'y' or c == 'Y'):
                print('Saving output to ' + str(salaryCapDefaultFilename) + '...')
                DumpToFile(SalaryCapTable, salaryCapDefaultFilename)
        elif(c == 'n' or c == 'N'):
            print('No data available. Aborting...')
            sys.exit()



    # Get year list from current year-1 to first year of salary cap
    # Current year doesn't get included in team list because contracts are signed in the offseason
    # For example, if current year is 2022 (offseason), the last team stats available are from "2021-2022" or 2021
    yearList = SalaryCapTable["Seasons"]
    idx = list(yearList).index(CurrentYear-1)


    # Trim everything before current year (future salary cap values)
    yearList = yearList[idx:len(yearList)]

    # Add 3 extra years to team list. This will grab previous 3 years' worth of data from team list
    # which are then used as features for contracts signed in the first salary cap year
    lastYear = yearList[len(yearList)-1]
    yearList = np.append(yearList, (lastYear-1))
    yearList = np.append(yearList, (lastYear-2))
    yearList = np.append(yearList, (lastYear-3))

    c = input('Load team stats from file? (y/n)')


    while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
        c = input('Invalid input. Load team stats from file? (y/n)')


    if(c == 'y' or c == 'Y'):
        fileName = input('WARNING: This will read using pickle I/O, only use files you trust. Enter q to abort. Please enter name of file to read from: ')
        if(fileName == 'q' or fileName == 'Q'):
            c = input('Read Aborted. Fetch new team stats from ESPN? (y/n)')
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                c = input('Invalid Input. Fetch new team stats from ESPN? (y/n)')
            if(c == 'y' or c == 'Y'):
                TeamStatsList = GetTeamStatsFromESPN(yearList)
                s = 'Save results to "' + teamStatsDefaultFilename + '"? (y/n)'
                c = input(s)
                while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                    s = 'Invalid Input. Save results to "' + teamStatsDefaultFilename + '"? (y/n)'
                    c = input(s)
                if(c == 'y' or c == 'Y'):
                    print('Saving output to ' + str(teamStatsDefaultFilename) + '...')
                    DumpToFile(TeamStatsList, teamStatsDefaultFilename)

            elif(c == 'n' or c == 'N'):
                print('No data available. Aborting...')
                sys.exit()
        else:
            # Filename available
            TeamStatsList = ReadFromFile(fileName)

    elif(c == 'n' or c == 'N'):
        c = input('Fetch new new team stats from ESPN? (y/n)')
        while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
            c = input('Invalid Input. Fetch new new team stats from ESPN? (y/n)')
        if(c == 'y' or c == 'Y'):
            TeamStatsList = GetTeamStatsFromESPN(yearList)
            s = 'Save results to "' + teamStatsDefaultFilename + '"? (y/n)'
            c = input(s)
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                s = 'Invalid Input. Save results to "' + teamStatsDefaultFilename + '"? (y/n)'
                c = input(s)
            if(c == 'y' or c == 'Y'):
                print('Saving output to ' + str(teamStatsDefaultFilename) + '...')
                DumpToFile(TeamStatsList, teamStatsDefaultFilename)
        elif(c == 'n' or c == 'N'):
            print('No data available. Aborting...')
            sys.exit()
    

    return ActivePlayerList, SalaryCapTable, TeamStatsList


# This will prompt the user to enter a player name and contract length and predict the corresponding salary 
# predicted using modelParam
def PlayerPredictionsUI(PlayerList, SalaryCapTable, TeamStatsList, CurrentYear, modelParam,  xMean, xVar, UseTeamsInfo):

   name = input('Please enter a player name: ')
   found = 0

   # Try to find player in list
   for p in PlayerList:
       if(FormatURL(p.Name) == FormatURL(name)):
           found = 1
           break
   if(found == 0):
       print("Error: Player not found")
       return -1;


   if(UseTeamsInfo == True):
       # Try to find current team
       team = p.StatHistory[-1].Team
       inputStr = "Resign with " + team + " ? (y/n)"
       c = input(inputStr)
       inputStr = "Invalid Input. " + inputStr
       while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
            c = input(inputStr)

       if(c == 'y'):
           newTeam = team
       else:
           team = input("Please enter a new team: ")
           if((team in TeamList) == False):
               print("Error: Invalid team name")
               return -1
           newTeam = team

   else:
       newTeam = "N/A"  # Assign newTeam to arbitrary value

   contractLength = input('Please enter number of years: ')

   y = FindPlayerWorth(p, SalaryCapTable, TeamStatsList, \
           float(contractLength), CurrentYear, modelParam, CurrentYear, xMean, xVar, \
           UseTeamsInfo, newTeam)


   
   print("Predicted Salary = " + str(round(y, 0)) + "$")
   return y


# Sort players by contract values and print the outputs
# This will essentially compare the player's remaining contract with the
# predicted salary of that player for a new contract of the same duration
def SortPlayersUI(ActivePlayerList, SalaryCapTable, TeamStatsList, CurrentYear, param, xMean, xVar, UseTeamsInfo):
    
    NameList = []
    CurrentSalaryList = [] 
    PredictedSalaryList = []

    print("Sorting active players from best contracts to worst...")

    for p in ActivePlayerList:

        # For this list, only players that are not goaltenders and are not on ELCs are considered valid
        if(p.Position != 'G' and len(p.ContractDates) > 1):
            # Find the latest contract of this player
            dates = p.ContractDates
            idx = dates.index(max(dates))
            nYears = p.ContractLength[idx]
            yearsLeft = (dates[idx] + nYears) - CurrentYear

            # Note that we only add players to list if they have a contract that goes beyond the current year
            if(yearsLeft > 0):

                # Add current salary
                NameList.append(p.Name)
                CurrentSalaryList.append(p.ContractAAV[idx])

                if(len(p.StatHistory) == 0):
                    team = "N/A"
                else:
                    team = p.StatHistory[-1].Team

                prediction = FindPlayerWorth(p, SalaryCapTable, TeamStatsList, \
                float(yearsLeft), CurrentYear, param, CurrentYear, xMean, xVar, \
                UseTeamsInfo, team)

                PredictedSalaryList.append(prediction)



    # Now sort players
    # First convert all lists to numpy arrays for sorting
    NameList = np.array(NameList)
    CurrentSalaryList = np.array(CurrentSalaryList)
    PredictedSalaryList = np.array(PredictedSalaryList)

    # Now generate contract offsets
    SalaryDifferenceList = PredictedSalaryList - CurrentSalaryList

    # Reorganize list from best contract to worst
    idxList = sorted(range(len(SalaryDifferenceList)), key=lambda k: SalaryDifferenceList[k], reverse = True)
    NameList = NameList[idxList]
    CurrentSalaryList = CurrentSalaryList[idxList]
    PredictedSalaryList = PredictedSalaryList[idxList]
    SalaryDifferenceList = SalaryDifferenceList[idxList]


    n = input("How many players do you want to display?")
    n = int(n)

    print("Contracts from best to worse: ")


    for i in range(n):
        print(str(i) + ": " + str(NameList[i]) + "  Current Salary: " + str(CurrentSalaryList[i]) + \
            "$  Predicted Salary: " + str(PredictedSalaryList[i]) + "$  Difference: " + str(SalaryDifferenceList[i]) + "$")


    print("...")
    for i in range(len(NameList) - n, len(NameList)):
        print(str(i) + ": " + str(NameList[i]) + "  Current Salary: " + str(CurrentSalaryList[i]) + \
            "$  Predicted Salary: " + str(PredictedSalaryList[i]) + "$  Difference: " + str(SalaryDifferenceList[i]) + "$")



