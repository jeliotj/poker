#!/usr/bin/python3
##### Poker Hand Simulator #####
# By Eliot Smith
# Version 0.0.1
# April 13, 2021

from operator import itemgetter
from hands import *
from deal import *
from cards import *

# Constants
total_each = {  'royalflush':        0, 
                'strflush':     0, 
                'fourkind':     0, 
                'fullhouse':    0, 
                'flush':        0, 
                'straight':     0,
                'threekind':    0,
                'twopair':      0,
                'onepair':      0,
                'highcard':     0   }

def userMenu():
    """ Present options to the user """
    print("""How many deals to you want to run?
        Please enter a number or 'q' for quit. """)
    user = input()
    return user

def sortCards(hand):
    """ Sort hand according to rank """
    sorted_hand = sorted(hand, key=itemgetter(2))
    return sorted_hand
   
def scoreHand(hand):
    ## Some preliminary necessities
    sorted_hand = sortCards(hand)
    rank_string = rankString(sorted_hand)

    ## Finding all possible hands 
    if findFlush(hand) != 0 and findStraight(sorted_hand) != 0 and sorted_hand[-1][2] == 14:
        score = 'royalflush'
    elif findFlush(hand) != 0 and findStraight(sorted_hand) != 0:
        score = 'strflush'
    elif fourKind(rank_string) != 0:
        score = 'fourkind'
    elif findFlush(hand) != 0:
        score = 'flush'
    elif threeKind(rank_string) != 0 and twoPair(rank_string) != 0:
        score = 'fullhouse'
    elif threeKind(rank_string) != 0:
        score = 'threekind'
    elif twoPair(rank_string) != 0:
        score = 'twopair'
    elif findPair(rank_string) != 0:
        score = 'onepair'
    elif findStraight(sorted_hand) != 0:
        score = 'straight'
    else:
        score = 'highcard'

    return score

def mainLoop():
    while True:
        print("")
        u = userMenu()
        if u != 'q':
            for runs in range(0, int(u)):
                deck = createDeck(52)
                nd = shuffleDeck(deck)
                playerHand = dealHand(5, nd)
                handtype = scoreHand(playerHand)
                total_each[handtype] += 1
            for k in total_each:
                if len(k) <= 5:
                    print(k + ":", end='\t\t')
                else:
                    print(k + ":", end='\t')
                print(total_each[k])
                total_each[k] = 0
        else:
            break

mainLoop()
