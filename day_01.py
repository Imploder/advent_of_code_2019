import os
from utils import Utils


def read_input_file(input_file):
    with open(input_file, 'r') as file:
        return [word.strip() for word in file.read().split()]


def calculate_fuel_needed_for_mass(mass):
    return (int(mass) // 3) - 2


def calculate_total_fuel_needed_for_mass(mass):
    total_fuel = 0
    incremental_fuel = calculate_fuel_needed_for_mass(mass)
    while incremental_fuel >= 0:
        total_fuel += incremental_fuel
        incremental_fuel = calculate_fuel_needed_for_mass(incremental_fuel)

    return total_fuel


if __name__ == '__main__':
    task_helper = Utils()
    mass_of_modules = read_input_file(task_helper.input)
    print(sum(calculate_total_fuel_needed_for_mass(int(module)) for module in mass_of_modules))
