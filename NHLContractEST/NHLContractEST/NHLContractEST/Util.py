# This file will contain minor utility function to clean up rest of code

import pickle

# This function will take in a player name and create the proper URL for it
def FormatURL(name):

    # Replace spaces with - for urls for all players
    name = name.replace(" ", "-")

    # Remove certain characters
    name = name.replace("'", "")
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
    name = name.replace(chr(362), "U")

    name = name.replace(chr(221), "Y")

    name = name.replace(chr(199), "C")


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

    name = name.replace(chr(249), "u")
    name = name.replace(chr(250), "u")
    name = name.replace(chr(251), "u")
    name = name.replace(chr(252), "u")
    name = name.replace(chr(363), "u")

    name = name.replace(chr(253), "y")
    name = name.replace(chr(255), "y")

    name = name.replace(chr(231), "c")

    # Special case: Multiple players with the same name
    # These players have both a normal page and a "1" page
    # However, the normal page doesn't have the right info
    # Therefore, force these cases to the "1" or "2" page
    if(name == "Matt-Murray"):
        name = "matt-murray1"

    if(name == "Eric-Robinson"):
        name = "eric-robinson1"

    if(name == "Mikko-Lehtonen"):
        name = "mikko-lehtonen2"

    # This one is just a special case where the url is different 
    if(name == "Jean-Sebastien-Dea"):
        name = "jeansebastien-dea"


    return name

# This function will print all player list info to the console
def PrintPlayerInfo(Player):

    print("Player " + str(i) + ": " + Player.Name)
    print("    Age: " + str(Player.Age) + "   Position: " + Player.Position)

    for j in range(0, Player.NumContracts):
        print("\nContract Start: " + str(Player.ContractDates[j]) + "   Length: " + str(Player.ContractLength[j]) + " AAV:" + str(Player.ContractAAV[j]))

        print("\nStatistics: ")
    for j in range (0, len(Player.StatHistory)):
        if(Player.Position == 'G'):
            print("    " + str(Player.StatHistory[j].Year) + " Regular Season: Team = " + Player.StatHistory[j].Team + ", GP = " + \
                    str(Player.StatHistory[j].RegularGP) + ", GAA = " + str(Player.StatHistory[j].RegularGAA) \
                    + ", Sv% = " + str(Player.StatHistory[j].RegularSavePercent) + ", GA60 = " + str(Player.StatHistory[j].RegularGA60) \
                    + ", xGA60 = " + str(Player.StatHistory[j].RegularxGA60) + ", GSAx60 " + str(Player.StatHistory[j].RegularGSAx60))
            print("    " + str(Player.StatHistory[j].Year) + " Playoffs: Team = " + Player.StatHistory[j].Team + ", GP = " + \
                    str(Player.StatHistory[j].PlayoffGP) + ", GAA = " + str(Player.StatHistory[j].PlayoffGAA) \
                    + ", Sv% = " + str(Player.StatHistory[j].PlayoffSavePercent) + ", GA60 = " + str(Player.StatHistory[j].PlayoffGA60) \
                    + ", xGA60 = " + str(Player.StatHistory[j].PlayoffxGA60) + ", GSAx60 " + str(Player.StatHistory[j].PlayoffGSAx60))
        else:
            print("    " + str(Player.StatHistory[j].Year) + " Regular Season: Team = " + Player.StatHistory[j].Team + ", GP = " + \
                    str(Player.StatHistory[j].RegularGP) + ", G = " + str(Player.StatHistory[j].RegularGoals) \
                    + ", A = " + str(Player.StatHistory[j].RegularAssists) + ", +/- = " + str(Player.StatHistory[j].RegularPlusMinus) \
                    + ", PIM = " + str(Player.StatHistory[j].RegularPIM) + "\n             TOI = " + str(Player.StatHistory[j].RegularEVTOI) \
                    + ", EVG = " + str(Player.StatHistory[j].RegularEVG) + ", ixG = " + str(Player.StatHistory[j].RegularixG) \
                    + ", xG+/60 = " + str(Player.StatHistory[j].RegularxG60) + ", RelxG+/60 = " + str(Player.StatHistory[j].RegularRelxG60) \
                    + ", C+60 = " + str(Player.StatHistory[j].RegularC60) + ", RelC+60 = " + str(Player.StatHistory[j].RegularRelC60))
            print("    " + str(Player.StatHistory[j].Year) + " Playoffs: Team = " + Player.StatHistory[j].Team + ", GP = " + \
                    str(Player.StatHistory[j].PlayoffGP) + ", G = " + str(Player.StatHistory[j].PlayoffGoals) \
                    + ", A = " + str(Player.StatHistory[j].PlayoffAssists) + ", +/- = " + str(Player.StatHistory[j].PlayoffPlusMinus) \
                    + ", PIM = " + str(Player.StatHistory[j].PlayoffPIM) + "\n             TOI = " + str(Player.StatHistory[j].PlayoffEVTOI) \
                    + ", EVG = " + str(Player.StatHistory[j].PlayoffEVG) + ", ixG = " + str(Player.StatHistory[j].PlayoffixG) \
                    + ", xG+/60 = " + str(Player.StatHistory[j].PlayoffxG60) + ", RelxG+/60 = " + str(Player.StatHistory[j].PlayoffRelxG60) \
                    + ", C+60 = " + str(Player.StatHistory[j].PlayoffC60) + ", RelC+60 = " + str(Player.StatHistory[j].PlayoffRelC60))
           



    return 



# NOTE: Pickle IO is not ideal for safety reasons but since I am just creating my own data file
# and re-using it, this should be ok. 
def DumpToFile(data, fileName):
    with open(fileName, 'wb') as handle:
        pickle.dump(data, handle)


def ReadFromFile(fileName):
    with open(fileName, 'rb') as handle:
        data = pickle.loads(handle.read())

    return data
