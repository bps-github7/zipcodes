"""
Zipcode memorizer
A simple memory game for delivery drivers
Ben Sehnert
"""


import sys

germantown = [144, 119,140]
manayaunk = [127]
roxboro = [128]
east_falls = [129]
narberth=['072']
bala_cynwd = ['004',131]


def zipcodes_help(extended=False):
    """
Help fn, explains how to use the program
    """
    print("Help: welcome to Manayaunk site delivery range zipcode training.")
    print("you can type q/quit any time to leave or h/help to review this info.\n\n")
    if extended:
        print("type in a number corresponding to one of the following terms to learn more")
        print("ie. to learn more about 'freestyle mode' type 1 and hit enter\n")
        terms = ["operating mode: freestyle", "operating mode: self-directed",
                 "option: list all", "option: list one", "option : reverse list all",
                 "option : reverse list one", "option : rapid fire list one",
                 "option : rapid fire list all", "option : rapid fire reverse list all",
                 "option: rapid fire reverse list one"]
        for x,y in enumerate(terms):
            print(f"{x+1}\t\t\t{y}")
        while True:
            response = input()
            if response in ("q","quit"):
                print("exiting help menu - enter q/ quit again to close the app")
                break
            elif response in ("h", "help"):
                zipcodes_help()
            else:
                try:
                    response = int(response)
                    if response < 11 and response > 0:
                        option_handler(response)
                    else:
                        print("try again- you must enter a value in range 0 to 10 to learn about a term")
                except ValueError:
                    print("try again- you must enter a numeric value to learn about a term")


def option_handler(opt):
    """
Takes a number between 0 and 10 as sole arg.
informs user about the choice associated with that number.
see terms (list) in zipcodes_help to learn about the available choices.
    """
    if opt == 1:
        print("operating mode: freestyle")
        print("you will be tested with a random assortment of excersizes")
    elif opt == 2:
        print("operating mode: self directed")
        print("choose the excersise you want to do and number of rounds per each")
    # these names arent really accurate now that you defined them.
    elif opt == 3:
        print("option: list all")
        print("Given an area, provide all zip codes associated with it.")
        # if prompt():
            # list_all()
    elif opt == 4:
        print("option: list one")
        print("Match the correct zip code with a given area")
    elif opt == 5:
        print("option: reverse list all")
        print("Given a zip code, provide the name of the area associated with it.")
    elif opt == 6:
        print("option: reverse list one")
        print("Match the correct area with the given zip code.")
    elif opt == 7:
        print("option: rapid fire list all.")
        print("Complete the challenge within alloted time to win the maximum possible points")
    elif opt == 8:
        print("option: rapid fire list one.")
        print("Complete the challenge within alloted time to win the maximum possible points")
    elif opt == 9:
        print("option: rapid fire reverse list all")
        print("Complete the challenge within alloted time to win the maximum possible points")
    elif opt == 10:
        print("option: rapid fire reverse list one")
        print("Complete the challenge within alloted time to win the maximum possible points")
        
    return 0

def main():
    zipcodes_help()
    while True:
        response = input("enter 1 for free style mode or 2 for self directed mode (type h for help)\n")
        try:
            int(response)
            if int(response) == 1:
                freestyle()
            elif int(response) == 2:
                self_directed()
        except ValueError:
            print("numeric value expected")
            continue
        if response in ("h","help"):
            zipcodes_help(extended=True)
        if response in ("q", "quit"):
            sys.exit(1)
                
def freestyle():
    """[summary]
    """
    print("freestyle mode")
    print()

def self_directed():
    """[summary]
    """
    print("self-directed mode")
    print()


        
            

def list_all_zipcodes(area_name, area_list):
    """
asks the user for zipcodes until they listed all
    """
    while True:
        provided = input(f"enter a 3 digit zipcode ending for {area_name}:\n")
        if provided in ("q","quit"):
            return 0
        if int(provided) in area_list:
            area_list.remove(int(provided))
            print("correct")
            if len(area_list):
                print("there are still more to list")
                return list_all_zipcodes(area_name, area_list)
            else:
                return 1
        else:
            print("not correct. try again")

def reverse_list_all(area_name, area_list):
    while True:
        print("what area has the followng zip codes?")
        for item in area_list:
            print(item)
        provided = input()
        if provided in ("q","quit"):
            return 0
        if provided == area_name:
            print("correct")
            return 1
        else:
            print("incorrect. try again")
  
list_all_zipcodes("manayaunk", manayaunk)


# main()
