"""
Zipcode memorizer
A simple memory game for delivery drivers
Ben Sehnert
"""



import sys
import random

all_zipcodes = {"germantown"  : '144', "mt airy" :'119',
"nicetown" : '140', "east germantown" : '118',
"manayunk" : '127', "roxborough" : '128', "east falls" : '129',
"narberth" : '072', "bala cynwd" : '004',  "wynnefield" : '131' }

all_area_names = [i for i in list(all_zipcodes.keys())]
all_area_zipcodes = [i for i in list(all_zipcodes.values())]



def test():
    # for i in all_zipcodes:
    #     print(all_zipcodes[i])
    # for i in area_zipcodes:
    #     print(i)
    # multiple_choice(hard=True)
    list_one()


def zipcodes_help(extended=False):
    """
Help fn, explains how to use the program
    """
    print("Help: welcome to Manayaunk site delivery range zipcode training.")
    print("you can type q/quit any time to leave or h/help to review this info.\n\n")
    if extended:
        print("type in a number corresponding to one of the following terms to learn more")
        print("ie. to learn more about 'freestyle mode' type 1 and hit enter\n")
        terms = ["operating mode : freestyle", "operating mode: self-directed",
                 "excersise: list all", "excersise: list one", "excersise : reverse list all",
                 "excersise : reverse list one", "excersise : rapid fire list one",
                 "excersise : rapid fire list all", "excersise : rapid fire reverse list all",
                 "excersise: rapid fire reverse list one"]
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
                        excersise_handler(response)
                    else:
                        print("try again- you must enter a value in range 0 to 10 to learn about a term")
                except ValueError:
                    print("try again- you must enter a numeric value to learn about a term")


def excersise_handler(opt):
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
    elif opt == 3:
        print("Excersise: list all")
        print("Cycle through the list of all area names and answer with the correct zipcodes to pass.")
        print("possible points: 10")
        # if prompt():
            # list_all()
    elif opt == 4:
        print("Excersise: list one")
        print("Match the correct zip code with a given area")
        print("Possbile Points: 1")
    elif opt == 5:
        print("Excersise: reverse list all")
        print("Cycle through the list of all zip codes and match with the correct zipcodes to pass")
        print("Possible points: 10")
    elif opt == 6:
        print("Excersise: reverse list one")
        print("Match the correct area name with a given zip code.")
        print("Possible points: 1")
    elif opt == 7:
        print("Excersise: rapid fire list all.")
        print("Complete the challenge within alloted time to win the maximum possible points")
        print("Possible points: 15")
    elif opt == 8:
        print("Excersise: rapid fire list one.")
        print("Complete the challenge within alloted time to win the maximum possible points")
        print("Possible points: 15")
    elif opt == 9:
        print("Excersise: rapid fire reverse list all")
        print("Complete the challenge within alloted time to win the maximum possible points")
        print("possible points: 15")
    elif opt == 10:
        print("Excersise: rapid fire reverse list one")
        print("Complete the challenge within alloted time to win the maximum possible points")
        print("possible points: 15")
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
    possible_excersises = ['list_one', 'list_all', 'reverse_list_one', 'reverse_list_all', 'rapid fire']
    while True:
        for x,y in enumerate(possible_excersises):
            print(f'[{x}] {y}')

def self_directed():
    """[summary]
    """
    print("self-directed mode")
    print("choose which excersise to do and how many of each")


def multiple_choice(hard=False):
    options = ['a','b','c','d']
    correct_zipcode = random.choice(all_area_zipcodes) 
    correct_area = all_area_names[all_area_zipcodes.index(correct_zipcode)]
    copy = all_area_names[:]
    copy.remove(correct_area)
    
    areas = random.sample(copy, 3)
    areas.append(correct_area)
    random.shuffle(areas)
    # # Testing:
    # print(f"the zipcode for {correct_area} is {correct_zipcode}")
    print("what is the area ")
    print(correct_zipcode)
    for x,y in zip(options, areas):
        print(f"[{x}] {y}")
    while True:
        response = input()
        if response in options:
            if response in ("q","quit"):
                return 0
            elif areas[options.index(response)] == correct_area:
                print("correct")
                return 1
            else:
                print("incorrect")
                if hard:
                    return 0
                print("try again")



def list_one(area_name, area_list):
    """
asks the user for zipcodes until they listed all
    """
    correct_zipcode = 
    while True:
        provided = input(f"enter a 3 digit zipcode ending for {area_name}:\n")
        if provided in ("q","quit"):
            return 0
        
        
        if all_area_names[int(provided)] in area_list:
            print("correct")
            return 1
        else:
            print("not correct. try again")

# def reverse_list_one(area_name, area_list):
#     while True:
#         print("what area has the followng zip codes?")
#         for item in area_list:
#             print(item)
#         provided = input()
#         if provided in ("q","quit"):
#             return 0
#         if provided == area_name:
#             print("correct")
#             return 1
#         else:
#             print("incorrect. try again")
  
# list_all_zipcodes("manayaunk", manayaunk)
# for i in area_names:
#     print(i)

# multiple_choice()



test()
# main()
