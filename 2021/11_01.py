from colorama import init, Style, Fore
from data_read import read_file

navigation = read_file("11.txt")

navigation = [[int(number) for number in nav.strip()] for nav in navigation]

class Octopuses:

    def __init__(self, grid):
        self.grid = grid
        self.grid_size = len(self.grid[0])
        self.triggered_grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.step = 0
        self.flashes = 0
        self.deltas = [(idx, jdx) for jdx in range(-1, 2) for idx in range(-1, 2)]

    def reset_trigger_grid(self):
        self.triggered_grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def count_trigger_grid(self):
        return sum(x.count("*") for x in self.triggered_grid)

    def display(self):
        print(f"**** Step:{self.step} ****")
        for idx in range(self.grid_size):
            for jdx in range(self.grid_size):
                if self.grid[idx][jdx] <= 9:
                    print(self.grid[idx][jdx], end="")
                else:
                    print(Fore.RED + Style.BRIGHT + str(self.grid[idx][jdx]-10) + Style.NORMAL + Fore.WHITE, end="")
            print()
        print(f"Flashes: {self.flashes}")
    
    def display_trigger_grid(self):
        print(f"**** Step:{self.step} ****")
        for idx in range(self.grid_size):
            for jdx in range(self.grid_size):
                print(self.triggered_grid[idx][jdx], end="")
            print()

    def update(self):
        for idx in range(self.grid_size):
            for jdx in range(self.grid_size):
                self.grid[idx][jdx] +=1

        self.go_again = True
        while self.go_again:
            self.go_again = False
            for idx in range(self.grid_size):
                for jdx in range(self.grid_size):
                    if self.grid[idx][jdx] > 9 and self.triggered_grid[idx][jdx] == ".":
                        self.go_again = True
                        self.flashes += 1
                        self.triggered_grid[idx][jdx] = "*"
                        for delta in self.deltas:
                            idx_d = idx + delta[0]
                            jdx_d = jdx + delta[1]
                            if 0 <= idx_d < self.grid_size:
                                if 0 <= jdx_d < self.grid_size:
                                    self.grid[idx_d][jdx_d] += 1

        for idx in range(self.grid_size):
            for jdx in range(self.grid_size):
                if self.grid[idx][jdx] > 9:
                    self.grid[idx][jdx] = 0

        self.step += 1

init()

octo = Octopuses(navigation)
octo.display()

while True:
    octo.update()
    # octo.display()
    # octo.display_trigger_grid()
    if octo.step == 100:
        print(f"P1: Flashes at Step 100: {octo.flashes}")
    if octo.count_trigger_grid() == 100:
        print(f"P2: All Octopuses Flashing at Step: {octo.step}")
        break
    octo.reset_trigger_grid()