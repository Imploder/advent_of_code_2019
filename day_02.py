from utils import Utils
from typing import List


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
        print(f"Index 0 Value: {intcode_program[0]}")
        print("Found 99, exiting")
        exit()
    else:
        raise Exception(f"This opcode: {opcode} is not valid.")


if __name__ == '__main__':
    task_helper = Utils()
    input_data = task_helper.read_input_file(split=",")
    intcode_program = convert_string_list_to_int_list(input_data)

    # Emergency Fire Repairs:
    intcode_program[1] = 12
    intcode_program[2] = 2

    for position, integer in enumerate(intcode_program):
        if position == 0 or position % 4 == 0:
            intcode_section = intcode_program[position:position + 4]
            perform_operation(intcode_section, intcode_program)
