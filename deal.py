from random import randint as pick

def createDeck(n):
    """ Create an unshuffled deck of n cards """
    deck = []
    for i in SUITS:
        for j in NRANKS:
            deck.append((j, i, NRANKS.get(j)))
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

