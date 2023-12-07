from data_read import read_file
from collections import namedtuple, Counter
from pprint import pprint

from operator import attrgetter

from recordclass import recordclass

hands = read_file("07.txt")

translation = {
    "A": "e", 
    "K": "d", 
    "Q": "c", 
    "J": "b", 
    "T": "a", 
    "9": "9", 
    "8": "8", 
    "7": "7", 
    "6": "6", 
    "5": "5", 
    "4": "4", 
    "3": "3", 
    "2": "2"
}

"""
types:
[5] - five of a kind
[4, 1] - four of a kind
[3, 2] - full house
[3, 1, 1] - three of a kind
[2, 2, 1] - two pair
[2, 1, 1, 1] - one pair
[1, 1, 1, 1, 1] - high card
"""

types = [
[1, 1, 1, 1, 1], [2, 1, 1, 1],  [2, 2, 1], [3, 1, 1], [3, 2],  [4, 1],  [5]
]

CamelCard = recordclass("CamelCard", ["cards", "type", "score", "bet", "rank"])

all_cards_list = []

# get cards into list
for hand in hands:
    # print(hand.strip())
    cards, bet = hand.strip().split(" ")
    cards_score = int("".join([translation[c] for c in cards]), 16)
    # count numbers in each card
    cards_list = list(cards)
    cards_count = Counter(cards_list)
    # turn counts into list, in order high > low
    cards_types_list = sorted(list(cards_count.values()), reverse=True)
    cards_type = types.index(cards_types_list)

    bet = int(bet)
    current_card = CamelCard(cards, cards_type, cards_score, bet, 0)
    print(current_card)
    all_cards_list.append(current_card)

# sort by type, then score
all_cards_list = sorted(all_cards_list, key=attrgetter("type", "score"))

# work out score
scores = [card.bet * rank for rank, card in enumerate(all_cards_list, 1)]

print(sum(scores))



