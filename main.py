#!/usr/bin/python3
##### A Poker Game #####
# By Eliot Smith
# Version 0.0.1
# April 13, 2021

from time import sleep
from operator import itemgetter, attrgetter
from hands import *
from wagers import *
from deal import *
from cards import *

# Constants

def userMenu():
    """ Present menu options to the user """
    print("""What would you like to do?
        Please type:
        'd' for deal,
        'h' for help or
        'q' for quit.""")
    user = input()
    return user

def sortCards(hand):
    """ Sort hand according to rank """
    sorted_hand = sorted(hand, key=itemgetter(2))
    return sorted_hand
   
def inspectHand(hand):

    sorted_hand = sortCards(hand)
    rank_string = rankString(sorted_hand)

    ## Find the possible hands of value
    findFlush(sorted_hand)
    findPair(rank_string)
    twoPair(rank_string)
    threeKind(rank_string)
    fourKind(rank_string)
    
def mainLoop():
    while True:
        print("")
        u = userMenu()
        stack = 0
        if u in ("d", "de", "dea", "deal"):
            #if stack == 0:
            #    print("You need to buy some chips.")
            #    stack = buyChips()
            #    sleep(1)
            #    print("You now have $" + str(stack) + " in chips.")
            deck = createDeck(52)
            nd = shuffleDeck(deck)
            playerHand, dealerHand = dealHand(5, nd)
            print("Here is your hand:")
            for card in playerHand:
                print((playerHand.index(card)+1) * '\t', end='')
                print(ranks_full.get(card[0]) + " of " + suits_full.get(card[1]))
            #makeWager(stack)
            inspectHand(playerHand)

        elif u in ("h", "he", "hel", "help"):
            print("That would be nice, wouldn't it?")
            sleep(2)
        elif u in ("q", "qu", "qui", "quit"):
            break

mainLoop()