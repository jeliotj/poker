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

# Dictionary to expand names

suits_full = {'S': 'Spades', 'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs'}
ranks_full = {'2': 'Two', '3': 'Three','4': 'Four','5': 'Five','6': 'Six','7': 'Seven','8': 'Eight',\
    '9': 'Nine','T': 'Ten','J': 'Jack','Q': 'Queen','K': 'King','A': 'Ace'}

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
    """ Random selection of a single card from a deck,
    inserting it into a hand. """
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
    value = 0

    hand = ''.join(playerHand)
    spade = re.findall("S", hand)
    heart = re.findall("H", hand)
    diamond = re.findall("D", hand)
    club = re.findall("C", hand)

    print("You got " + str(len(spade)) + " spades.")
    print("You got " + str(len(heart)) + " hearts.")
    print("You got " + str(len(diamond)) + " diamonds.")
    print("You got " + str(len(club)) + " clubs.")

    if len(spade) == 5 or len(heart) == 5 or len(diamond) == 5 or len(club) == 5:
        print("You got a flush!")
        value = value + 64
    else:
        pass

    findranks = re.findall("[^SDHC]+", hand)
    list.sort(findranks)
    rankhand = ''.join(findranks)
    ## Find a pair
    pair = re.compile(r".*(.).*\1")
    try:
        m = pair.match(rankhand).groups()
        print("You got a pair of " + str(m[0]) + "'s")
    except:
        print("You did not get a pair.")
    ## Two Pairs
    twopair = re.compile(r".*(.).*\1.*(.).*\2")
    try:
        m = twopair.match(rankhand).groups()
        print("You got a pair of " + str(m[0]) + "'s and a pair of " + str(m[1]) + "'s.")
    except:
        print("You did not get two pairs.")
    ## Three of a Kind
    threeof = re.compile(r".*(.).*\1.*\1")
    try:
        m = threeof.match(rankhand).groups()
        print("You got three " + str(m[0]) + "'s")
    except:
        print("You did not get three of a kind.")
    ## Four of a Kind
    fourof = re.compile(r".*(.).*\1.*\1.*\1")
    try:
        m = fourof.match(rankhand).groups()
        print("You got four " + str(m[0]) + "'s")
    except:
        print("You did not get four of a kind.")
        
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
            print(playerHand)
            #makeWager(stack)
            inspectHand(playerHand)

        elif u in ("h", "he", "hel", "help"):
            print("That would be nice, wouldn't it?")
            sleep(2)
        elif u in ("q", "qu", "qui", "quit"):
            break

mainLoop()