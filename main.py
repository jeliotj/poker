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
   
def scoreHand(hand):
    score = 0
    ## Some preliminary necessities
    sorted_hand = sortCards(hand)
    rank_string = rankString(sorted_hand)

    ## Finding all possible hands 

    if findFlush(hand) != 0 and findStraight(hand) != 0 and sorted_hand[-1][2] == 14:
        score = score + 100
    elif findFlush(hand) != 0 and findStraight(hand) != 0:
        score = score + 90
    elif fourKind(rank_string) != 0:
        score = score + 80
    elif findFlush(hand) != 0:
        score = score + 60
    elif threeKind(rank_string) != 0:
        score = score + 40
    elif twoPair(rank_string) != 0:
        score = score + 30
    elif findPair(rank_string) != 0:
        score = score + 20
    elif findStraight(hand) != 0:
        score = score + 50
    else:
        score = score + sorted_hand[-1][2]

    return score
    
def mainLoop():
    while True:
        print("")
        u = userMenu()
        if u in ("d", "de", "dea", "deal"):
            final = 0
            i = 0
            while final < 50:
                deck = createDeck(52)
                nd = shuffleDeck(deck)
                playerHand, dealerHand = dealHand(5, nd)
                #print("Here is your hand:")
                #for card in playerHand:
                #    print((playerHand.index(card)+1) * '\t', end='')
                #    print(ranks_full.get(card[0]) + " of " + suits_full.get(card[1]))
                score = scoreHand(playerHand)
                if score >= 50:
                    final = final + score
                else:
                    i += 1
            print(playerHand)
            print(final)
            print("It took " + str(i) + " deals to get a straight or better.")

        elif u in ("h", "he", "hel", "help"):
            print("That would be nice, wouldn't it?")
            sleep(2)
        elif u in ("q", "qu", "qui", "quit"):
            break

mainLoop()