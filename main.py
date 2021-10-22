#!/usr/bin/python3
##### Poker Hand Simulator #####
# By Eliot Smith
# Version 0.0.1
# April 13, 2021

from hands import *
from deal import *
from constants import *
from user import *

def mainLoop():
    while True:
        print("")
        u = userMenu()
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

mainLoop()
