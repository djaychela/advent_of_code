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
game = 0


def play_game(player_1_cards, player_2_cards):
    global game
    game += 1
    # setup game storage for this game
    game_hands_storage_p1 = []
    game_hands_storage_p2 = []
    round = 1


    while len(player_1_cards) > 0 and len(player_2_cards) > 0:
        # check for hands in previous hands
        if player_1_cards in game_hands_storage_p1:
            idx = game_hands_storage_p1.index(player_1_cards)
            if game_hands_storage_p2[idx] == player_2_cards:
                print(player_1_cards, game_hands_storage_p1)
                # p1 wins!
                print("p1 wins default")
                return 1
        
        game_hands_storage_p1.append(player_1_cards[::1])
        game_hands_storage_p2.append(player_2_cards[::1])
        print(f" -- Round {round} (Game {game}) -- ")
        print(f"Player 1's deck: {player_1_cards}")
        print(f"Player 2's deck: {player_2_cards}")
        print(f"Player 1 plays: {player_1_cards[0]}")
        print(f"Player 2 plays: {player_2_cards[0]}")
        cards = [player_1_cards.pop(0), player_2_cards.pop(0)]

        if len(player_1_cards) >= cards[0] and len(player_2_cards) >= cards[1]:
            print("Playing a sub-game to determine the winner...")
            winner = play_game(player_1_cards[:cards[0]], player_2_cards[:cards[1]])
            game -=1
            print(f'**** returned winner: {winner}')
        elif cards[0] > cards[1]:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            print(f"Player 1 wins round {round} of game {game}")
            player_1_cards.extend(cards)
        elif winner == 2:
            print(f"Player 2 wins round {round} of game {game}")
            player_2_cards.extend(cards[::-1])
        round += 1

    print(f"The winner of game {game} is player {winner}!")
    print(f"Player 1's deck: {player_1}")
    print(f"Player 2's deck: {player_2}")

    return winner
    
winner = play_game(player_1, player_2)

print(winner)
if winner == 1:
    winning_cards = player_1
else:
    winning_cards = player_2

score = 0

winning_cards.reverse()

for mult, card in enumerate(winning_cards, 1):
    
    score += (mult * card)
    print(score, mult, card, mult * card)

print(f"Final Score: {score}")