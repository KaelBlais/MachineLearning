# This file will load all necessary input and output variables

import pandas as pd
import urllib

class Player:
    def __init__(self, Name):
        self.Name = Name
    Age = 0
    Position  = ""

# This function will load all of the required input features from Capfriendly
def GetStatsFromCapFriendly():


    print("Getting stats from CapFriendly...")

    ActivePlayerList = []
    
    # Import player data. There are 32 pages of active players in Capfriendly
    for i in range (0, 1):
        url = "https://www.capfriendly.com/browse/active?pg=" + str(i+1)
        L = pd.read_html(url)

        # Convert list to data frame. This list only has one dataframe. 
        DF = L[0]

        # Find number of players in list
        n = DF["PLAYER"].size

        # print("Length of Data: " + str(n))

        for j in range (0, n):
            s = (DF["PLAYER"].iloc[j])
            # First trim everything before name
            k = 0;
            while(s[k] < 'A' or s[k] > 'Z'):
                k = k + 1
            name = s[k:len(s)]
            
            # Append this player to the list
            ActivePlayerList.append(Player(name))


    
    # Now go through data list and fill out info for each player.
    # This will contain basic info (age, position, etc.) and contract info
    for i in range(0, len(ActivePlayerList)):
        name = str(ActivePlayerList[i].Name);

        # Replace spaces with - for urls for all players
        name = name.replace(" ", "-")
        name = name.replace(".", "")

        # Replace other foreign characters with their corresponding equivalent
        name = name.replace(chr(192), "A")
        name = name.replace(chr(193), "A")
        name = name.replace(chr(194), "A")
        name = name.replace(chr(195), "A")
        name = name.replace(chr(196), "A")
        name = name.replace(chr(197), "A")

        name = name.replace(chr(200), "E")
        name = name.replace(chr(201), "E")
        name = name.replace(chr(202), "E")
        name = name.replace(chr(203), "E")

        name = name.replace(chr(204), "I")
        name = name.replace(chr(205), "I")
        name = name.replace(chr(206), "I")
        name = name.replace(chr(207), "I")

        name = name.replace(chr(209), "N")

        name = name.replace(chr(210), "O")
        name = name.replace(chr(211), "O")
        name = name.replace(chr(212), "O")
        name = name.replace(chr(213), "O")
        name = name.replace(chr(214), "O")
        name = name.replace(chr(216), "O")

        name = name.replace(chr(217), "U")
        name = name.replace(chr(218), "U")
        name = name.replace(chr(219), "U")
        name = name.replace(chr(220), "U")

        name = name.replace(chr(221), "Y")


        name = name.replace(chr(224), "a")
        name = name.replace(chr(225), "a")
        name = name.replace(chr(226), "a")
        name = name.replace(chr(227), "a")
        name = name.replace(chr(228), "a")
        name = name.replace(chr(229), "a")

        name = name.replace(chr(232), "e")
        name = name.replace(chr(233), "e")
        name = name.replace(chr(234), "e")
        name = name.replace(chr(235), "e")

        name = name.replace(chr(236), "i")
        name = name.replace(chr(237), "i")
        name = name.replace(chr(238), "i")
        name = name.replace(chr(239), "i")

        name = name.replace(chr(241), "n")

        name = name.replace(chr(242), "o")
        name = name.replace(chr(243), "o")
        name = name.replace(chr(244), "o")
        name = name.replace(chr(245), "o")
        name = name.replace(chr(246), "o")
        name = name.replace(chr(248), "o")

        name = name.replace(chr(249), "U")
        name = name.replace(chr(250), "U")
        name = name.replace(chr(251), "U")
        name = name.replace(chr(252), "U")

        name = name.replace(chr(253), "y")
        name = name.replace(chr(255), "y")


        url = "https://www.capfriendly.com/players/" + name
        L = pd.read_html(url)

        # Contract info can be found from tables using the read_html pandas command
        for j in L:
            DF = j
            # print(DF)


        # Basic info can be found from the player description using the raw html code
        # Each player description contains a blob of text in the same format. 
        # This blob will contain information
        data = urllib.request.urlopen(url).read(10000000)
        s = str(data)

        # Firt spot is the age of the player. 
        idx = s.find(" year old ");
        # Age comes right before this. This is always 2 digits. 
        sAge = s[idx-2:idx]
        ActivePlayerList[i].Age = int(sAge)

    print("done.")

    

    return ActivePlayerList