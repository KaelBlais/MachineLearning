from GetData import *
import sys


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
                ActivePlayerList = GetPlayerStatsFromCapFriendly()
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
            ActivePlayerList = GetPlayerStatsFromCapFriendly()
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
