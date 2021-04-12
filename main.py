#!/usr/bin/python3

from random import choice as pick

# Constants
suits = ["S", "H", "D", "C"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Initializing needed arrays
unshufDeck1 = []
shufDeck1 = []
hand1 = []
hand2 = []

# Create unshuffled, 52-card, standard American deck
for i in suits:
    for j in ranks:
        unshufDeck1.append(j+i)

# Shuffle the deck
for k in range(0, len(unshufDeck1)):
    card = pick(unshufDeck1)
    shufDeck1.append(card)
    unshufDeck1.remove(card)
    
# Deal the hands



