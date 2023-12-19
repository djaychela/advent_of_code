from data_read import read_file
from operator import attrgetter

sorting_list_raw = read_file("19.txt")

change = sorting_list_raw.index("\n")
workflows = sorting_list_raw[:change]
parts = sorting_list_raw[change + 1:]

class Workflow:
    def __init__(self, info):
        self.info = info

class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __repr__(self):
        return(f"{self.x=}, {self.m=}, {self.a=}, {self.s=}")

    def rating(self):
        return self.x + self.m + self.a + self.s
    
    @classmethod
    def parse(cls, part_list):
        return cls(*(int(attr.split("=")[1]) for attr in part_list))

workflow_dict = dict()

for workflow in workflows:
    workflow_name = workflow.split("{")[0]
    workflow_info = workflow.split("{")[1].strip("}\n").split(",")
    print(f"{workflow_name=}")
    print(f"{workflow_info=}")
    workflow_dict[workflow_name] = Workflow(workflow_info)

part_list = []

# for part in parts:
#     xmas_list = part.strip("{}\n")
#     xmas_list = xmas_list.split(",")
#     part_list.append(Part.parse(xmas_list))

def test_part(part):
    workflow = "in"
    while True:
        for rule in workflow_dict[workflow].info:
            if "<" in rule:
                # process less than
                attribute = rule.split("<")[0]
                rating, new_workflow = rule.split("<")[1].split(":")
                rating = int(rating)
                # print(f"{attribute=}, {rating=}, {new_workflow=}")
                if attrgetter(attribute)(part) < rating:
                    workflow = new_workflow
                    break
            elif ">" in rule:
                # process greater than
                attribute, rating = rule.split(">")
                rating, new_workflow = rule.split(">")[1].split(":")
                rating = int(rating)
                # print(f"{attribute=}, {rating=}, {new_workflow=}")
                if attrgetter(attribute)(part) > rating:
                    workflow = new_workflow
                    break
            else:
                workflow = rule
                break
        if workflow == "A":
            # accepted
            return part.rating()
        elif workflow == "R":
            # reject part... move to next
            return 0

score = 0

# attempt at brute forcing.
for x in range(4000):
    for m in range(4000):
        for a in range(4000):
            for s in range(4000):
                test_part(Part(x=x, m=m, a=a, s=s))
        print(f"{m=}")
# This would take multiple days to run even in PyPy.... so not an option!

print(score)