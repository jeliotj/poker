import re
from cards import *

def rankString(hand):
    """ Creates a string so that RE can be used to find pairs, three and four of a kind. """
    rankhand = []
    for card in hand:
        rankhand.append(card[0])
    rank_string = ''.join(rankhand)
    return rank_string

def findPair(string):
    """ Find a pair """
    pair = re.compile(r".*(.).*\1")
    try:
        m = pair.match(string).groups()
    except:
        return 0

def twoPair(string):
    twopair = re.compile(r".*(.).*\1.*(.).*\2")
    try:
        m = twopair.match(string).groups()
    except:
        return 0

def threeKind(string):
    threeof = re.compile(r".*(.).*\1.*\1")
    try:
        m = threeof.match(string).groups()
    except:
        return 0

def fourKind(string):
    fourof = re.compile(r".*(.).*\1.*\1.*\1")
    try:
        m = fourof.match(string).groups()
    except:
        return 0

def findStraight(hand):
    if hand[4][2] == (hand[3][2] + 1) and hand[3][2] == (hand[2][2] + 1) and hand[2][2] == (hand[1][2] + 1) and hand[1][2] == (hand[0][2] + 1):
        return 1
    else:
        return 0

def findFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return 1
    else:
        return 0