class Stack:
    __name = None
    __stack_key = None
    __stack = None
    __index = None
    __limit = None

    def __init__(self):
        self.__name = None
        self.__stack_key = list()
        self.__stack = dict()
        self.__index = 0
        self.__limit = 0

    def init_marco(self, name):
        self.__name = name
        self.__stack_key.append(f"macro {self.__index}")
        self.__stack[self.__stack_key[-1]] = {self.__name: list()}
        self.__index += 1

    def init_segment(self, name):
        self.__name = name
        self.__stack_key.append(f"segemt {self.__index}")
        self.__stack[self.__stack_key[-1]] = {self.__name: list()}
        self.__index += 1

    def push_line(self, cmd):
        self.__stack[self.__stack_key[-1]][self.__name].append(cmd)

    def __iter__(self):
        self.__limit = self.__index
        self.__index = 0
        return self.__stack

    def __next__(self):
        pass

    def __str__(self):
        string = "<------------------------------------------->\n"
        for i in self.__stack.keys():
            string += "[======================================]\n"
            string += f" -> {i}:\n"
            for j in self.__stack[i].values():
                for k in j:
                    string += f"{k}\n"
            string += "[======================================]\n"
        string += "<------------------------------------------->\n"
        return string







