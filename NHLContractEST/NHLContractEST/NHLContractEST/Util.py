# This file will contain minor utility function to clean up rest of code

import pickle
import matplotlib.pyplot as plt
import numpy as np

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


# In some sources e.g. CapFriendly, old team names are used
# In other websites e.g. NHL, those old team names have been renamed
# This creates a mismatch. To avoid this, all old team names will be renamed
# using this function
def RenameOldTeam(name):

    if(name == "Phoenix Coyotes"):
        name = "Arizona Coyotes"

    if(name == "Atlanta Thrashers"):
        name = "Winnipeg Jets"

    if(name == "Mighty Ducks of Anaheim"):
        name = "Anaheim Ducks"

    return name

# This function will print a player's information to the screen
def PrintPlayerInfo(Player):

    print("Player Name: " + Player.Name)
    print("    Age: " + str(Player.Age) + "   Position: " + Player.Position + "   Height: " + str(Player.Height) + " cm" + \
        "   Weight: " + str(Player.Weight) + " lbs" + "    Draft Position: " + str(Player.DraftPosition))

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
        print("\n")   



    return 


# This function will print all info from a contract entry to the screen
def PrintContractEntry(c):
    print("CONTRACT ENTRY:             PLAYER: " + c.Name + "  AGE: " + str(c.PlayerAge) + "  POSITION: " + c.PlayerPosition)
    print("Contract Signed in " + str(c.year) + "     AAV: " + str(c.Salary) + "$  Length: " + str(c.NumYears) + " years")
    
    print("Year-1 Stats (Regular Season):     GP: " + str(round(c.Year1RegSeasonGP, 2)) + "  G: " + str(round(c.Year1RegSeasonG, 2)) + "  A: " \
         + str(round(c.Year1RegSeasonA, 2)) + "  +/-: " + str(round(c.Year1RegSeasonPlusMinus, 2)) + "  PIM: " + str(round(c.Year1RegSeasonPIM, 2)))
    print("                                   EVTOI: " + str(round(c.Year1RegSeasonEVTOI, 2)) + "  ixG: " + str(round(c.Year1RegSeasonixG, 2)) + "  xG+/60: " \
        + str(round(c.Year1RegSeasonxG60, 2)) + " RelxG+/60: " + str(round(c.Year1RegSeasonRelxG60, 2)) + "  C+60: " + str(round(c.Year1RegSeasonC60, 2)) + "  RelC+60: " + str(round(c.Year1RegSeasonRelC60, 2)))
    print("Year-1 Stats (Playoffs):           GP: " + str(round(c.Year1PlayoffsGP, 2)) + "  G: " + str(round(c.Year1PlayoffsG, 2)) + "  A: " \
         + str(round(c.Year1PlayoffsA, 2)) + "  +/-: " + str(round(c.Year1PlayoffsPlusMinus, 2)) + "  PIM: " + str(round(c.Year1PlayoffsPIM, 2))) 
    print("                                   EVTOI: " + str(round(c.Year1PlayoffsEVTOI, 2)) + "  ixG: " + str(round(c.Year1PlayoffsixG, 2)) + "  xG+/60: " \
        + str(round(c.Year1PlayoffsxG60, 2)) + " RelxG+/60: " + str(round(c.Year1PlayoffsRelxG60, 2)) + "  C+60: " + str(round(c.Year1PlayoffsC60, 2)) + "  RelC+60: " + str(round(c.Year1PlayoffsRelC60, 2)))
    

    print("Year-2 Stats (Regular Season):     GP: " + str(round(c.Year2RegSeasonGP, 2)) + "  G: " + str(round(c.Year2RegSeasonG, 2)) + "  A: " \
         + str(round(c.Year2RegSeasonA, 2)) + "  +/-: " + str(round(c.Year2RegSeasonPlusMinus, 2)) + "  PIM: " + str(round(c.Year2RegSeasonPIM, 2)))
    print("                                   EVTOI: " + str(round(c.Year2RegSeasonEVTOI, 2)) + "  ixG: " + str(round(c.Year2RegSeasonixG, 2)) + "  xG+/60: " \
        + str(round(c.Year2RegSeasonxG60, 2)) + " RelxG+/60: " + str(round(c.Year2RegSeasonRelxG60, 2)) + "  C+60: " + str(round(c.Year2RegSeasonC60, 2)) + "  RelC+60: " + str(round(c.Year2RegSeasonRelC60, 2)))
    print("Year-2 Stats (Playoffs):           GP: " + str(round(c.Year2PlayoffsGP, 2)) + "  G: " + str(round(c.Year2PlayoffsG, 2)) + "  A: " \
         + str(round(c.Year2PlayoffsA, 2)) + "  +/-: " + str(round(c.Year2PlayoffsPlusMinus, 2)) + "  PIM: " + str(round(c.Year2PlayoffsPIM, 2)))
    print("                                   EVTOI: " + str(round(c.Year2PlayoffsEVTOI, 2)) + "  ixG: " + str(round(c.Year2PlayoffsixG, 2)) + "  xG+/60: " \
        + str(round(c.Year2PlayoffsxG60, 2)) + " RelxG+/60: " + str(round(c.Year2PlayoffsRelxG60, 2)) + "  C+60: " + str(round(c.Year2PlayoffsC60, 2)) + "  RelC+60: " + str(round(c.Year2PlayoffsRelC60, 2)))
    
    print("Year-3 Stats (Regular Season):     GP: " + str(round(c.Year3RegSeasonGP, 2)) + "  G: " + str(round(c.Year3RegSeasonG, 2)) + "  A: " \
         + str(round(c.Year3RegSeasonA, 2)) + "  +/-: " + str(round(c.Year3RegSeasonPlusMinus, 2)) + "  PIM: " + str(round(c.Year3RegSeasonPIM, 2)))
    print("                                   EVTOI: " + str(round(c.Year3RegSeasonEVTOI, 2)) + "  ixG: " + str(round(c.Year3RegSeasonixG, 2)) + "  xG+/60: " \
        + str(round(c.Year3RegSeasonxG60, 2)) + " RelxG+/60: " + str(round(c.Year3RegSeasonRelxG60, 2)) + "  C+60: " + str(round(c.Year3RegSeasonC60, 2)) + "  RelC+60: " + str(round(c.Year1RegSeasonRelC60, 2)))
  
    print("Year-3 Stats (Playoffs):           GP: " + str(round(c.Year3PlayoffsGP, 2)) + "  G: " + str(round(c.Year3PlayoffsG, 2)) + "  A: " \
         + str(round(c.Year3PlayoffsA, 2)) + "  +/-: " + str(round(c.Year3PlayoffsPlusMinus, 2)) + "  PIM: " + str(round(c.Year3PlayoffsPIM, 2)))
    print("                                   EVTOI: " + str(round(c.Year3PlayoffsEVTOI, 2)) + "  ixG: " + str(round(c.Year3PlayoffsixG, 2)) + "  xG+/60: " \
        + str(round(c.Year3PlayoffsxG60, 2)) + " RelxG+/60: " + str(round(c.Year3PlayoffsRelxG60, 2)) + "  C+60: " + str(round(c.Year3PlayoffsC60, 2)) + "  RelC+60: " + str(round(c.Year3PlayoffsRelC60, 2)))
    
    
    print("Team Stats (Year-1 Season):         Rank: " + str(round(c.Year1TeamPosition, 2)) + " GP: " + str(round(c.Year1TeamGP, 2)) + " W: " \
        + str(round(c.Year1TeamWins, 2)) + " L: "+ str(round(c.Year1TeamLosses, 2)) + " OT: " + str(round(c.Year1TeamOTLosses, 2)) + " GF: " \
        + str(round(c.Year1TeamGF, 2)) + " GA: " + str(round(c.Year1TeamGA, 2)))
    print("Team Stats (Year-2 Season):         Rank: " + str(round(c.Year2TeamPosition, 2)) + " GP: " + str(round(c.Year2TeamGP, 2)) + " W: " \
        + str(round(c.Year2TeamWins, 2)) + " L: "+ str(round(c.Year2TeamLosses, 2)) + " OT: " + str(round(c.Year2TeamOTLosses, 2)) + " GF: " \
        + str(round(c.Year2TeamGF, 2)) + " GA: " + str(round(c.Year2TeamGA, 2)))
    print("Team Stats (Year-3 Season):         Rank: " + str(round(c.Year3TeamPosition, 2)) + " GP: " + str(round(c.Year3TeamGP, 2)) + " W: " \
        + str(round(c.Year3TeamWins, 2)) + " L: "+ str(round(c.Year3TeamLosses, 2)) + " OT: " + str(round(c.Year3TeamOTLosses, 2)) + " GF: " \
        + str(round(c.Year3TeamGF, 2)) + " GA: " + str(round(c.Year3TeamGA, 2)))

    print("Salary Cap (Year+1 Season): " + str(c.Year1Cap) + "$     Min Salary: " + str(c.Year1MinSalary) + "$")
    print("Salary Cap (Year+2 Season): " + str(c.Year2Cap) + "$     Min Salary: " + str(c.Year2MinSalary) + "$")
    print("Salary Cap (Year+3 Season): " + str(c.Year3Cap) + "$     Min Salary: " + str(c.Year3MinSalary) + "$")
    
    print("\n\n")
    
    return


# Plot a feature vector x against its output y.
# "name" refers to the feature name that will be used for the x-axis
def PlotFeatureVector(x, y, name):
    plt.clf()
    plt.scatter(x, y)
    plt.ylabel("Contract Value (1,000,000 $)")
    plt.xlabel(name)
    plt.title("Feature Plot")
    plt.show()


def PlotCostFunction(Jhistory):
    # First convert to dollars
    Jdollars = Jhistory.copy()
    Jdollars = np.sqrt(Jdollars) * 1000000

    plt.clf()
    plt.plot(Jdollars)
    plt.ylabel("Average Error ($)")
    plt.xlabel("Iteration")
    plt.title("Cost Function")
    plt.show()


# NOTE: Pickle IO is not ideal for safety reasons but since I am just creating my own data file
# and re-using it, this should be ok. 
def DumpToFile(data, fileName):
    with open(fileName, 'wb') as handle:
        pickle.dump(data, handle)

    return


def ReadFromFile(fileName):
    with open(fileName, 'rb') as handle:
        data = pickle.loads(handle.read())

    return data