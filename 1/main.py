import math

modules = open("input.txt", "r")

def calc_fuel(module):
    return int(module) // 3-2

def get_fuel():
    total_fuel = 0
    for module in modules.readlines():
        module = calc_fuel(int(module))
        total_fuel += module
    print(total_fuel)

def get_total_fuel():
    total_fuel = 0
    for module in modules:
        while int(module) > 5:
            module = calc_fuel(module)
            total_fuel += int(module)
    print(total_fuel)
