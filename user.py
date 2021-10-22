## User Interface Functions
import sys

def userMenu():
    """ Get user input"""

    numRuns = input("""How many deals to you want to run?
Please enter a positive whole number or 'q' for quit.\n""")

    while True:
        if numRuns == 'q':
            sys.exit()
        else:
            try:
                numRuns = int(numRuns)
                return numRuns
            except ValueError:
                print("That doesn't look like a valid number! Try again...")
