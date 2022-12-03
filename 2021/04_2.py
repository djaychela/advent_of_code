from dataclasses import dataclass
from typing import ClassVar

from data_read import read_file

board_list = []

bingo = read_file("04.txt")

calls = list(map(int, bingo.pop(0).split(",")))


@dataclass
class Board:
    numbers: list
    called: ClassVar[list] = []
    winning_call: int = 0
    won: bool = False

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
        if self.won:
            return True
        for idx in range(len(self.numbers)):
            line_true = True
            for jdx in range(len(self.numbers[0])):
                current = self.numbers[idx][jdx]
                if current not in self.called:
                    line_true = False
            if line_true:
                self.winning_call = self.called[-1]
                self.won = True
                return True
        # check columns
        for idx in range(len(self.numbers)):
            col_true = True
            for jdx in range(len(self.numbers[0])):
                current = self.numbers[jdx][idx]
                if current not in self.called:
                    col_true = False
            if col_true:
                self.winning_call = self.called[-1]
                self.won = True
                return True

        return False

    def score_board(self):
        score = 0
        relevant_calls = self.called[: self.called.index(self.winning_call) + 1]
        for idx in range(len(self.numbers)):
            for jdx in range(len(self.numbers[0])):
                current = self.numbers[idx][jdx]
                if current not in relevant_calls:
                    score += current

        return score

    def call(self, called_number):
        self.called.append(called_number)


# parse boards
for idx in range(1, len(bingo), 6):
    board = bingo[idx : idx + 5]
    board_list.append(Board(board))

# call numbers
for call in calls:
    board_list[0].called.append(call)
    print(f"Called: {call}")
    for idx, board in enumerate(board_list):
        win = board.check_win()
        print(f"{idx + 1} : {win}")
        if win:
            winning_call = call
            best_board = idx + 1


winning_locations = [
    (idx, calls.index(board.winning_call)) for idx, board in enumerate(board_list)
]

winning_locations.sort(key=lambda y: y[1], reverse=True)

last_winning_board = winning_locations[0][0]

board_score = board_list[last_winning_board].score_board()
winning_call = board_list[last_winning_board].winning_call
print(f"{board_score = }")
print(f"{winning_call = }")
print(f"Answer: {board_score * winning_call}")
