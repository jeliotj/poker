#!/usr/bin/python3

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

d = createDeck(52)
nd = shuffleDeck(d)
hand1 = dealHand(5, nd)
hand2 = dealHand(5, nd)

print(hand1)
print(hand2)