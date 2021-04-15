#!/usr/bin/python3
##### A Poker Game #####
# By Eliot Smith
# Version 0.0.1
# April 13, 2021

from time import sleep
from random import choice as pick
import re

# Constants
SUITS = ["S", "H", "D", "C"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def createDeck(n):
    """ Create an unshuffled deck of n cards """
    deck = []
    for i in SUITS:
        for j in RANKS:
            deck.append(j+i)
    return deck

def shuffleDeck(deck):
    """ Shuffle an unshuffled deck """
    newdeck = []
    for i in range(0, len(deck)):
        card = pick(deck)
        newdeck.append(card)
        deck.remove(card)
        
    return newdeck

def drawCard(deck, hand):
    card = pick(deck)
    deck.remove(card)
    hand.append(card)

def dealHand(n, deck):
    """ Deal an n card hand with a shuffled deck. """
    player = []
    dealer = []
    for i in range(0,n):
        drawCard(deck, player)
        drawCard(deck, dealer)
    return player, dealer

def userMenu():
    """ Present menu options to the user """
    print("""What would you like to do?
        Please type:
        'd' for deal,
        'h' for help or
        'q' for quit.""")
    user = input()
    return user

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

def inspectHand(playerHand):
    h = ''.join(playerHand)
    pair = re.compile(r".*([^SHDC]).*\1")
    try:
        m = pair.match(h).groups()
        for i in m:
            print("You got a pair of " + i + "'s!")
    except:
        print("You got no pairs")
    sleep(3)
    #if pair.match(h):
    #    print("You got a pair of" + c + "s!")

def mainLoop():
    print("POKER!")
    while True:
        u = userMenu()
        stack = 0
        if u in ("d", "de", "dea", "deal"):
            if stack == 0:
                print("You need to buy some chips.")
                stack = buyChips()
                sleep(1)
                print("You now have $" + str(stack) + " in chips.")
            deck = createDeck(52)
            nd = shuffleDeck(deck)
            playerHand, dealerHand = dealHand(5, nd)
            sleep(1)
            print(playerHand)
            sleep(1)
            makeWager(stack)
            sleep(1)
            inspectHand(playerHand)

        elif u in ("h", "he", "hel", "help"):
            print("That would be nice, wouldn't it?")
            sleep(2)
        elif u in ("q", "qu", "qui", "quit"):
            break

mainLoop()