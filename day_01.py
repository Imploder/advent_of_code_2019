raw_data = "input_01.txt"


def read_input_file(input_file):
    with open(input_file, 'r') as file:
        return [word.strip() for word in file.read().split()]


def calculate_module_fuel_total(modules):
    total = 0
    for module in modules:
        fuel_required = (int(module) // 3) - 2
        total += fuel_required

    return total


if __name__ == '__main__':
    module_mass = read_input_file(raw_data)
    print(calculate_module_fuel_total(module_mass))
