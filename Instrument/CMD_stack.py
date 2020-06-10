class Stack:
    __name = None
    __stack_key = None
    __stack = None
    __index = None

    def __init__(self):
        self.__name = None
        self.__stack_key = None
        self.__stack = dict()
        self.__index = 0

    def init_marco(self, name):
        self.__name = name
        self.__stack_key = f"macro {self.__index}"
        self.__stack[self.__stack_key] = {self.__name: list()}
        self.__index += 1

    def init_segment(self, name):
        self.__name = name
        self.__stack_key = f"segemt {self.__index}"
        self.__stack[self.__stack_key] = {self.__name: list()}
        self.__index += 1

    def push_line(self, cmd):
        self.__stack[self.__stack_key][self.__name].append(cmd)

    def __str__(self):
        string = "<-------------------------------------->\n"
        for i in self.__stack.keys():
            string += "[======================================]\n"
            string += f" -> {i}:\n"
            for j in self.__stack[i].values():
                for k in j:
                    string += f"{k}\n"
            string += "[======================================]\n"
        string += "<-------------------------------------->\n"
        return string







