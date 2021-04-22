SUITS = ["S", "H", "D", "C"]
NRANKS = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

suits_full = {'S': 'Spades', 'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs'}
ranks_full = {'2': 'Two', '3': 'Three','4': 'Four','5': 'Five','6': 'Six','7': 'Seven','8': 'Eight',\
    '9': 'Nine','T': 'Ten','J': 'Jack','Q': 'Queen','K': 'King','A': 'Ace'}

total_each = {  'royalflush':        0, 
                'strflush':     0, 
                'fourkind':     0, 
                'fullhouse':    0, 
                'flush':        0, 
                'straight':     0,
                'threekind':    0,
                'twopair':      0,
                'onepair':      0,
                'highcard':     0   }
