from .Database import labels


class Stack:
    __stack = None
    __cmd_index = None
    __cmd_limit = None
    __stack_index = None
    __stack_limit = None

    def __init__(self):
        self.__stack = list()
        self.__stack_index = self.__cmd_index = -1
        self.__stack_limit = self.__cmd_limit = 0

    def init_seg(self, name, cast):
        if cast == "M":
            cast = "macro"
            labels['macro'].append(name)
        elif cast == "S":
            cast = "segment"
        self.__stack.append({"type": cast, "name": name, "cmds": list()})

    def push_line(self, line):
        self.__stack[-1]["cmds"].append(line)

    def __iter__(self):
        self.__cmd_index = -1
        self.__stack_index = 0
        self.__stack_limit = len(self.__stack)
        self.__cmd_limit = len(self.__stack[0]["cmds"])
        return self

    @property
    def ret(self):
        return self.__stack

    def __next__(self):
        self.__cmd_index += 1
        if self.__cmd_index >= self.__cmd_limit:
            self.__cmd_index = 0
            self.__stack_index += 1
            try:
                self.__cmd_limit = len(self.__stack[self.__stack_index]["cmds"])
            except IndexError:
                pass
        if not self.__stack_index == self.__stack_limit:
            return self.__stack[self.__stack_index]["cmds"][self.__cmd_index]

    def __str__(self):
        string = "<------------------------------------------->\n"
        for i in self.__stack:
            string += f"\n -> {i['type']}: {i['name']}\n"
            for j in i["cmds"]:
                string += f"{j}\n"
        string += "<------------------------------------------->\n"
        return string







