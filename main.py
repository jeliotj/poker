#!/usr/bin/python3
##### A Poker Game #####
# By Eliot Smith
# Version 0.0.1
# April 13, 2021

from random import choice as pick

# Constants
SUITS = ["S", "H", "D", "C"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

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

def dealHand(n, deck):
    """ Deal an n card hand with a shuffled deck. """
    hand = []
    for i in range(0,n):
        card = pick(deck)
        deck.remove(card)
        hand.append(card)
    return hand

print("Hello and Welcome to our Poker game!")
while True:
    user = input("""What would you like to do?
            Please type:
            'd' for deal,
            'h' for help or
            'q' for quit.""")
    if user in ("d", "de", "dea", "deal"):
        d = createDeck(52)
        nd = shuffleDeck(d)
        hand = dealHand(5, nd)
        print(hand)
    elif user in ("h", "he", "hel", "help"):
        print("That would be nice, wouldn't it?")
    elif user in ("q", "qu", "qui", "quit"):
        break

# = createDeck(52)
# nd = shuffleDeck(d)
# hand1 = dealHand(5, nd)
# hand2 = dealHand(5, nd)

