from data_read import read_file

blueprints_raw = read_file("19_test.txt")

class Blueprint:
    def __init__(self, bp_no, ore, clay, obsidian, geode):
        self.blueprint_number = int(bp_no)
        self.ore_robot_cost = int(ore)
        self.clay_robot_cost = int(clay)
        self.obsidian_robot_cost = list(map(int, obsidian))
        self.geode_robot_cost = list(map (int, geode))
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        self.minute = 1
        self.strategy = "geode"

    def __repr__(self):
        return f"Blueprint {self.blueprint_number}: Ore:{self.ore_robot_cost}, Clay:{self.clay_robot_cost}, Obsi:{self.obsidian_robot_cost}, Geode:{self.geode_robot_cost}\n"

    def run_minute(self):
        # do any possible mining
        self.ore += self.ore_robots
        self.clay += self.clay_robots
        self.obsidian += self.obsidian_robots
        self.geode += self.geode_robots
        # build any possible robots
        if self.ore >= self.clay_robot_cost:
            self.clay_robots += 1
            self.ore -= self.clay_robot_cost
        if self.
        # increment the minute
        self.minute += 1

        print(f"""Minute {self.minute} ended:
        Ore:{self.ore}    \tClay:{self.clay} \tObsi: {self.obsidian} \tGeode: {self.geode}
        Ore:{self.ore_robots}    \tClay:{self.clay_robots}   \tObsi: {self.obsidian_robots} \tGeode: {self.geode_robots}
        """)

blueprint_list = []

for blueprint in blueprints_raw:
    elements = blueprint.split("robot costs ")
    blueprint_number = blueprint.split(":")[0].split(" ")[-1]
    ore_robot_cost = elements[1].split(" ore.")[0]
    clay_robot_cost = elements[2].split(" ore.")[0]
    obsi_robot_cost = [elements[3].split(" ore")[0], elements[3].split(" clay.")[0].split(" ")[-1]]
    geode_robot_cost = [elements[4].split(" ore")[0], elements[4].split(" obsidian.")[0].split(" ")[-1]]
    blueprint_list.append(Blueprint(blueprint_number, ore_robot_cost, clay_robot_cost, obsi_robot_cost, geode_robot_cost))

print(blueprint_list)

blueprint_scores = []

for blueprint in blueprint_list:
    # run simulation for 24 minutes
    for minutes in range(1, 25):
        blueprint.run_minute()