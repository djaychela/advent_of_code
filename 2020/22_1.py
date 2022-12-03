import pathlib

file_name = "22.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    hands = [hand.strip() for hand in file.readlines()]

def parse_hand(cards):
    player_hand = []
    for card in cards:
        try:
            player_hand.append(int(card))
        except ValueError:
            pass
    return player_hand

splitpoint = hands.index('')
player_1 = parse_hand(hands[:splitpoint])
player_2 = parse_hand(hands[splitpoint:])
round = 1

while len(player_1) > 0 and len(player_2) > 0:
    print(f" -- Round {round} --")
    print(f"Player 1's deck: {player_1}")
    print(f"Player 2's deck: {player_2}")
    print(f"Player 1 plays: {player_1[0]}")
    print(f"Player 2 plays: {player_2[0]}")
    cards = [player_1.pop(0), player_2.pop(0)]
    if cards[0] > cards[1]:
        print("Player 1 wins!")
        player_1.extend(sorted(cards, reverse=True))
    else:
        print("Player 2 wins!")
        player_2.extend(sorted(cards, reverse=True))
    round += 1

print(" -- Post-Game Results --")
print(f"Player 1's deck: {player_1}")
print(f"Player 2's deck: {player_2}")

if len(player_1) == 0:
    winner = player_2
else:
    winner = player_1

winner.reverse()

score = 0
for mult, card in enumerate(winner, 1):
    score += (mult * card)

print(f"Final Score: {score}")