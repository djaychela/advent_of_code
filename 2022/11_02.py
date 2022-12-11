from data_read import read_file

from copy import copy
from numpy import prod

instructions = read_file("11.txt")

class Monkey:
    def __init__(self, number, items, operation, test, true_throw, false_throw):
        self.number = number
        self.items = items
        self.op_action = operation.split(" ")[0]
        self.op_value = operation.split(" ")[1]
        self.test = int(test)
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspections = 0
        mod_value = 1

    def get_item(self, item):
        self.items.append(item)

    def inspect_items(self):
        for item in copy(self.items):
            self.inspections += 1
            original_value = item
            if self.op_value == 'old':
                item = item ** 2
            elif self.op_action == "*":
                item = item * int(self.op_value)
            else:
                item = item + int(self.op_value)

            item = item % self.mod_value

            if item % self.test == 0:
                monkeys[self.true_throw].get_item(item)
                self.items.remove(original_value)
            else:
                monkeys[self.false_throw].get_item(item)
                self.items.remove(original_value)

    def show_holding(self):
        print(f"Monkey {self.number}: {', '.join(map(str, self.items))}")

    def __repr__(self):
        return f"Monkey {self.number}: {self.items=}, {self.op_action=}, {self.op_value=}, {self.test=}, {self.true_throw=}, {self.false_throw=}"

monkeys = []
test_list = []

for idx in range(0, len(instructions), 7):
    m_number = int(instructions[idx][7])
    m_items = list(map(int, instructions[idx+1].split(":")[1].strip().split(",")))
    m_operation = instructions[idx+2].split("new = old ")[1].strip()
    m_test = instructions[idx+3].split("divisible by ")[1].strip()
    m_true = int(instructions[idx+4].split("monkey")[1].strip())
    m_false = int(instructions[idx+5].split("monkey")[1].strip())

    test_list.append(int(m_test))

    new_monkey = Monkey(m_number, m_items, m_operation, m_test, m_true, m_false)

    monkeys.append(new_monkey)

mod_value = prod(test_list)

for monkey in monkeys:
    monkey.mod_value = mod_value

for round in range(1, 10001):
    
    for monkey in monkeys:
        monkey.inspect_items()
    
    if round % 1000 == 0:
        print(f"Round: {round}")
        print([m.inspections for m in monkeys])


inspections = [m.inspections for m in monkeys]
print(f"{sorted(inspections)[-2] * sorted(inspections)[-1]}")