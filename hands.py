import re
from cards import *

def findPair(string):
    """ Find a pair """
    pair = re.compile(r".*(.).*\1")
    try:
        m = pair.match(string).groups()
        print("You got a pair of " + str(m[0]) + "'s")
    except:
        pass

def twoPair(string):
    twopair = re.compile(r".*(.).*\1.*(.).*\2")
    try:
        m = twopair.match(string).groups()
        print("You got a pair of " + str(m[0]) + "'s and a pair of " + str(m[1]) + "'s.")
    except:
        pass

def threeKind(string):
    threeof = re.compile(r".*(.).*\1.*\1")
    try:
        m = threeof.match(string).groups()
        print("You got three " + str(m[0]) + "'s")
    except:
        pass

def fourKind(string):
    fourof = re.compile(r".*(.).*\1.*\1.*\1")
    try:
        m = fourof.match(string).groups()
        print("You got four " + str(m[0]) + "'s")
    except:
        pass

def findFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        print("You got a flush in " + suits_full.get(hand[0][1]) + "!")

def rankString(hand):
    """ Creates a string so that RE can be used to find pairs, three and four of a kind. """
    rankhand = []
    for card in hand:
        rankhand.append(card[0])
    rank_string = ''.join(rankhand)
    return rank_string
