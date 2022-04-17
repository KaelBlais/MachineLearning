# This file will contain minor utility function to clean up rest of code

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

    # Magic special case - These players have different URLs for some reason
    if(name == "Marc-Andre-Fleury"):
        name = "marc-andre-fleury1"

    return name