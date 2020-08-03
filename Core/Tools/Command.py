# from PyCompiler.Instrument.Database import labels


class Command:
    __string = None
    __name = None
    __operands = None
    __size = None

    def __init__(self, string: str):
        self.__string = string
        self.__size = 0
        self.__parse_processing()
        if self.__operands is not None:
            pass
            # self.__parse_operands()

    def __parse_processing(self):
        self.__string = self.__string.split("\n")[0]
        tokens = self.__string.split(", ")
        if len(tokens) == 2:
            right = [tokens[1]]
            if "[" in tokens[0]:
                left = tokens[0].split("    ")
                left = [left[2], left[3][(1 if "Or" not in self.__string else 2):]]
            else:
                left = tokens[0].split()
            tokens = left + right
            self.__name = tokens[0]
            self.__operands = [tokens[1], tokens[2]]
        elif len(tokens) == 1 and "Cbw" in self.__string:
            self.__operands = None
        else:
            tokens = self.__string.split()
            self.__name = tokens[0]
            self.__operands = tokens[1]

    def __parse_operands(self):
        if isinstance(self.__operands, str):
            # TODO: lables
            pass
        elif isinstance(self.__operands, list):
            # TODO: operands
            buff = self.__operands[:]
            # self.__operands[0] = Operand(buff[0])
            # self.__operands[1] = Operand(buff[1])

    @property
    def size(self):
        return self.__size

    def __str__(self):
        s = "+--------------------+\n"
        s += f"| string:' {self.__string}'\n"
        s += f"| name: {self.__name}\n"
        s += f"| operands: {self.__operands}\n"
        s += "+--------------------+"
        return s
