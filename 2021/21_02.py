from data_read import read_file
from functools import lru_cache

players = read_file("21.txt")

positions = [int(player.strip()[-1]) for player in players][::-1]
scores = [0, 0]
moves = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

@lru_cache(maxsize=None)
def quantum_dice(position_1, position_2, score_1, score_2):
    if score_2 >= 21: return [0, 1]

    wins = [0, 0]
    for move, score in moves.items():
        round_score = position_1 + move
        while round_score >10:
            round_score -=10
        next_win = quantum_dice(position_2, round_score, score_2, score_1 + round_score)
        wins[0] = wins[0] + score * next_win[1]
        wins[1] = wins[1] + score * next_win[0]

    return wins

winning_scores = quantum_dice(positions[1], positions[0], 0, 0)


print(f"Part 2: {max(winning_scores)}")
