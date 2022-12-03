from dataclasses import dataclass
from typing import ClassVar

from data_read import read_file

board_list = []

bingo = read_file("04.txt")

calls = list(map(int,bingo.pop(0).split(",")))

@dataclass
class Board:
    numbers: list
    called: ClassVar[list] = []

    def __post_init__(self):
        int_numbers = []
        for numbers in self.numbers:
            line = []
            for number in numbers.split():
                line.append(int(number))
            int_numbers.append(line)
        self.numbers = int_numbers

    def check_win(self):
        # check rows
        for idx in range(len(self.numbers)):
            line_true = True
            for jdx in range(len(self.numbers[0])):
                current = self.numbers[idx][jdx]
                if current not in self.called:
                    line_true = False
            if line_true:
                return True
        # check columns
        for idx in range(len(self.numbers)):
            col_true = True
            for jdx in range(len(self.numbers[0])):
                current = self.numbers[jdx][idx]
                if current not in self.called:
                    col_true = False
            if col_true:
                return True

        return False
    
    def score_board(self):
        score = 0
        for idx in range(len(self.numbers)):
            for jdx in range(len(self.numbers[0])):
                current = self.numbers[idx][jdx]
                if current not in self.called:
                    score += current

        return score
    
    def call(self, called_number):
        self.called.append(called_number)


# parse boards
for idx in range(1, len(bingo), 6):
    board = bingo[idx:idx + 5]
    board_list.append(Board(board))

# call numbers
board_found = False
for call in calls:
    if board_found:
        print()
        break
    board_list[0].called.append(call)
    print(f"Called: {call}")
    for idx, board in enumerate(board_list):
        win = board.check_win()
        print(f"{idx + 1} : {win}")
        if win:
            board_found = True
            winning_call = call
            best_board = idx + 1
            break

print(best_board, winning_call)
board_score = board_list[best_board - 1].score_board()
print(f"Answer: {board_score * winning_call}")

