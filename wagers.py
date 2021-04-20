def buyChips():
    """ Buy up to $100 worth of chips """
    cash = int(input("You may buy up to $100 worth of chips. How much do you want to spend?"))
    if cash <= 100:
        v = cash
    else:
        print("You can only buy up to $100 in chips.")
    return v

def makeWager(stack):
    wager = input("You have $" + str(stack) + " to wager.  How much will you wager?")
    return wager
