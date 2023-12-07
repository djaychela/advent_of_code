from data_read import read_file
from collections import namedtuple, Counter
from pprint import pprint

from operator import attrgetter, itemgetter

from recordclass import recordclass

hands = read_file("07.txt")

translation = {
    "A": "e", 
    "K": "d", 
    "Q": "c", 
    "T": "a", 
    "9": "9", 
    "8": "8", 
    "7": "7", 
    "6": "6", 
    "5": "5", 
    "4": "4", 
    "3": "3", 
    "2": "2",
    "J": "0"
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

def pick_best_card(card_tuples):
    replacement_number = 0
    replacement_rank = 15
    replacement = None
    for card in card_tuples:
        for idx, rank in enumerate(translation.keys()):
            if card[0] == rank:
                if idx < replacement_rank:
                    if card[1] >= replacement_number:
                        replacement_rank = idx
                        replacement = rank
                        replacement_number = card[1]
    return replacement

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

    # Joker logic:
    # if joker present, count the most of any type, and highest of those
    # turn joker into the best present for purposes of type classification
    if cards == "JJJJJ":
        print("All Jokers!!!")
        pass
    elif "J" in cards_list:
        print(f"{cards=}: JOKER!!!")
        # find highest counts
        # pick best from that list
        card_to_replace = sorted(cards_count.items(), key=itemgetter(1), reverse=True)
        if card_to_replace[0][0] == "J":
            del(card_to_replace[0])
        # sort from list
        card_to_replace = pick_best_card(card_to_replace)
        # sort via not just presence, but numbers as well?
        print(f"{card_to_replace=}")
        print(f"Before: {cards_list=}")
        cards_list = [c if c !="J" else card_to_replace for c in cards_list ]
        print(f"After:  {cards_list=}")
        cards_count = Counter(cards_list)

    # turn counts into list, in order high > low
    cards_types_list = sorted(list(cards_count.values()), reverse=True)
    cards_type = types.index(cards_types_list)

    bet = int(bet)
    current_card = CamelCard(cards, cards_type, cards_score, bet, 0)
    all_cards_list.append(current_card)

# sort by type, then score
all_cards_list = sorted(all_cards_list, key=attrgetter("type", "score"))

# work out score
scores = [card.bet * rank for rank, card in enumerate(all_cards_list, 1)]

for rank, card in enumerate(all_cards_list, 1):
    print(card.cards, card.bet * rank)

print(sum(scores))

# 246954468 - too high 
# 246829920 - too high
# 246534246 - too high
# 246260353 - not right either.
# 246074324 - wait 5 minutes.
# All due to incorrect card substitutions
# 245864585 - not right.
# Due to missing on JJJJJ hand as 'pass' was a 'continue', so "JJJJJ" (top scoring hand) never scored.
# 246436046 - correct answer!!!