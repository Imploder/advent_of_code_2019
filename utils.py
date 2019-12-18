import sys


class Utils:
    def __init__(self):
        self.task = sys.argv[0].split("/")[-1]
        self.input = self.task.replace("day", "input").replace(".py", ".txt")

    def read_input_file(self) -> list:
        with open(self.input, 'r') as file:
            return [word.strip() for word in file.read().split()]
