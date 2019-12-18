from utils import Utils
from typing import List


def get_input_data():
    input_data = task_helper.read_input_file(split=",")
    return convert_string_list_to_int_list(input_data)


def int_op_sum(intcode, int_list):
    """
    Sum the numbers in the first two positions and store the result in the third
    :param intcode: Four long integer list of the opcodes needed information
    :param int_list: The entire intcode_program
    """
    int_list[intcode[3]] = int_list[intcode[1]] + int_list[intcode[2]]


def int_op_multiply(intcode, int_list):
    """
    Multiply the numbers in the first two positions and store the result in the third
    :param intcode: Four long integer list of the opcodes needed information
    :param int_list: The entire intcode_program
    """
    int_list[intcode[3]] = int_list[intcode[1]] * int_list[intcode[2]]


def convert_string_list_to_int_list(string_list: List[str]) -> List[int]:
    """
    Converts the given list of strings into a list of integers, no error handling.
    :param string_list: A list of numbers that are strings
    :return: The same list where the items in the list are now integers
    """
    return list(map(int, string_list))


def perform_operation(intcode_section, intcode_program):
    """
    Finds the correct operation to perform and performs that action
    :param intcode_section: Four long integer list of the opcodes needed information
    :param intcode_program: The entire intcode_program
    """
    opcode = intcode_section[0]
    if opcode == 1:
        int_op_sum(intcode_section, intcode_program)
    elif opcode == 2:
        int_op_multiply(intcode_section, intcode_program)
    elif opcode == 99:
        return True
    else:
        raise Exception(f"This opcode: {opcode} is not valid.")


def intcode_computer(intcode_program):
    for position, integer in enumerate(intcode_program):
        if position == 0 or position % 4 == 0:
            intcode_section = intcode_program[position:position + 4]
            if perform_operation(intcode_section, intcode_program):
                break

    return intcode_program[0]


if __name__ == '__main__':
    task_helper = Utils()
    intcode_program = get_input_data()

    goal = 19690720
    index_0 = intcode_program[0]

    for noun in range(1, 100):
        for verb in range(1, 100):
            intcode_program[1] = noun
            intcode_program[2] = verb

            if goal == intcode_computer(intcode_program):
                print(f"Found combination | noun: {noun} - verb: {verb}")
                print(f"{100 * noun + verb}")
                exit()
            else:
                intcode_program = get_input_data()

