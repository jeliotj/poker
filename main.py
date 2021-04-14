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

def inspectHand(hand):
    # if all cards contain S,H,D, or C : Flush
    # if all cards are in a sequence: Straight
    # if 2 or more have the same first element
    # if 2 have the same first element and 3 have same first element but different from the other 2
    
    
def mainLoop():
    print("POKER!")
    while True:
        u = userMenu()
        if u in ("d", "de", "dea", "deal"):
            stack = buyChips()
            deck = createDeck(52)
            nd = shuffleDeck(deck)
            playerHand, dealerHand = dealHand(5, nd)
            print(playerHand)
            wager = input("You have $" + str(stack) + " to wager.  How much will you wager?")
            playerBest = inspectHand(playerHand)
            dealerBest = inspectHand(dealerHand)
            outcome = compareHands(playerHand, dealerHand)
            if outcome == 1:
                print("You won the hand!")
                stack = 2*wager

        elif u in ("h", "he", "hel", "help"):
            print("That would be nice, wouldn't it?")
            sleep(2)
        elif u in ("q", "qu", "qui", "quit"):
            break

mainLoop()