
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
# import json
from GetData import *
from Util import *


playerStatsDefaultFilename = 'playerStats.txt'

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
            c = input('Save results to "playerStats.txt"? (y/n)')
            while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
                c = input('Invalid Input. Save results to "playerStats.txt"? (y/n)')
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
    c = input('Fetch new data from CapFriendly? (y/n)')
    while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
        c = input('Invalid Input. Fetch new data from CapFriendly? (y/n)')
    if(c == 'y' or c == 'Y'):
        ActivePlayerList = GetPlayerStatsFromCapFriendly()
        c = input('Save results to "playerStats.txt"? (y/n)')
        while(c != 'y' and c != 'Y' and c != 'n' and c != 'N'):
            c = input('Invalid Input. Save results to "playerStats.txt"? (y/n)')
        if(c == 'y' or c == 'Y'):
            print('Saving output to ' + str(playerStatsDefaultFilename) + '...')
            DumpToFile(ActivePlayerList, playerStatsDefaultFilename)
    elif(c == 'n' or c == 'N'):
        print('No data available. Aborting...')
        sys.exit()




# Print first 10 players for debug
PrintPlayerList(ActivePlayerList[0:5])
