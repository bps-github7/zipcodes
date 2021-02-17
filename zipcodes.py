"""
Zipcode memorizer
A simple memory game for delivery drivers
Ben Sehnert
"""


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
    print("Help: welcome to gopuff delivery range zipcode training.")
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
    print("option handler recieved: ", opt)
    return 0

def main():
    zipcodes_help()
    while True:
        response = input("first, tell us if you want to play free style or self directed (type h for help)\n")
        if response in ("h","help"):
            zipcodes_help(extended=True)
        else:
            print("cones")
            

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

main()
