# This file will contain minor utility function to clean up rest of code

from os import waitpid
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

    # Magic special case - These players have different URLs for some reason
    if(name == "Marc-Andre-Fleury"):
        name = "marc-andre-fleury1"

    if(name == "Danny-DeKeyser"):
        name = "danny-dekeyser1"

    if(name == "Olli-Maatta"):
        name = "olli-maatta1"

    if(name == "Trevor-van-Riemsdyk"):
        name = "trevor-van-riemsdyk1"

    return name

# This function will print all player list info to the console
def PrintPlayerList(list):
    print("Player List: \n")

    for i in range(0, len(list)):
        print("Player " + str(i) + ": " + list[i].Name)
        print("    Age: " + str(list[i].Age) + "   Position: " + list[i].Position)

        for j in range(0, list[i].NumContracts):
            print("        Contract Start: " + str(list[i].ContractDates[j]) + "   Length: " + str(list[i].ContractLength[j]) + " AAV:" + str(list[i].ContractAAV[j]))

        for j in range (0, len(list[i].StatHistory)):
            if(list[i].Position == 'G'):
                print("    " + str(list[i].StatHistory[j].Year) + " Regular Season: Team = " + list[i].StatHistory[j].Team + ", GP = " + \
                      str(list[i].StatHistory[j].RegularGP) + ", GAA = " + str(list[i].StatHistory[j].RegularGAA) \
                      + ", Sv% = " + str(list[i].StatHistory[j].RegularSavePercent) + ", GA60 = " + str(list[i].StatHistory[j].RegularGA60) \
                      + ", xGA60 = " + str(list[i].StatHistory[j].RegularxGA60) + ", GSAx60 " + str(list[i].StatHistory[j].RegularGSAx60))
                print("    " + str(list[i].StatHistory[j].Year) + " Playoffs: Team = " + list[i].StatHistory[j].Team + ", GP = " + \
                      str(list[i].StatHistory[j].PlayoffGP) + ", GAA = " + str(list[i].StatHistory[j].PlayoffGAA) \
                      + ", Sv% = " + str(list[i].StatHistory[j].PlayoffSavePercent) + ", GA60 = " + str(list[i].StatHistory[j].PlayoffGA60) \
                      + ", xGA60 = " + str(list[i].StatHistory[j].PlayoffxGA60) + ", GSAx60 " + str(list[i].StatHistory[j].PlayoffGSAx60))
            else:
                print("    " + str(list[i].StatHistory[j].Year) + " Regular Season: Team = " + list[i].StatHistory[j].Team + ", GP = " + \
                      str(list[i].StatHistory[j].RegularGP) + ", G = " + str(list[i].StatHistory[j].RegularGoals) \
                      + ", A = " + str(list[i].StatHistory[j].RegularAssists) + ", +/- = " + str(list[i].StatHistory[j].RegularPlusMinus) \
                      + ", PIM = " + str(list[i].StatHistory[j].RegularPIM) + "\n             TOI = " + str(list[i].StatHistory[j].RegularEVTOI) \
                      + ", EVG = " + str(list[i].StatHistory[j].RegularEVG) + ", ixG = " + str(list[i].StatHistory[j].RegularixG) \
                      + ", xG+/60 = " + str(list[i].StatHistory[j].RegularxG60) + ", RelxG+/60 = " + str(list[i].StatHistory[j].RegularRelxG60) \
                      + ", C+60 = " + str(list[i].StatHistory[j].RegularC60) + ", RelC+60 = " + str(list[i].StatHistory[j].RegularRelC60))
                print("    " + str(list[i].StatHistory[j].Year) + " Playoffs: Team = " + list[i].StatHistory[j].Team + ", GP = " + \
                      str(list[i].StatHistory[j].PlayoffGP) + ", G = " + str(list[i].StatHistory[j].PlayoffGoals) \
                      + ", A = " + str(list[i].StatHistory[j].PlayoffAssists) + ", +/- = " + str(list[i].StatHistory[j].PlayoffPlusMinus) \
                      + ", PIM = " + str(list[i].StatHistory[j].PlayoffPIM) + "\n             TOI = " + str(list[i].StatHistory[j].PlayoffEVTOI) \
                      + ", EVG = " + str(list[i].StatHistory[j].PlayoffEVG) + ", ixG = " + str(list[i].StatHistory[j].PlayoffixG) \
                      + ", xG+/60 = " + str(list[i].StatHistory[j].PlayoffxG60) + ", RelxG+/60 = " + str(list[i].StatHistory[j].PlayoffRelxG60) \
                      + ", C+60 = " + str(list[i].StatHistory[j].PlayoffC60) + ", RelC+60 = " + str(list[i].StatHistory[j].PlayoffRelC60))
           



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
