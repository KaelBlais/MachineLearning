from GetData import *
import sys


playerStatsDefaultFilename = 'PlayerStats.txt'
salaryCapDefaultFilename = 'SalaryCap.txt'


def GetInputsUI(LoadDefaults = False):



    # If LoadDefaults is on, UI will be bypassed and default files will be read
    if(LoadDefaults == True):
        ActivePlayerList = ReadFromFile(playerStatsDefaultFilename)
        SalaryCapTable = ReadFromFile(salaryCapDefaultFilename)

        return ActivePlayerList, SalaryCapTable
        

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

    return ActivePlayerList, SalaryCapTable


