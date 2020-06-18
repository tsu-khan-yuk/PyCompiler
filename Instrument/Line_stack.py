class Stack:
    __type = None
    __stack = None
    __cmd_index = None
    __cmd_limit = None
    __stack_index = None
    __stack_limit = None

    def __init__(self):
        self.__type = None
        self.__stack = list()
        self.__stack_index = self.__cmd_index = -1
        self.__stack_limit = self.__cmd_limit = 0

    def init_seg(self, name, cast):
        cast = "macro" if cast == "M" else "segment"
        self.__type = cast
        self.__stack.append({"type": cast, "name": name, "cmds": list()})

    def push_line(self, line):
        self.__stack[-1]["cmds"].append(line)

    def __iter__(self):
        self.__cmd_index = -1
        self.__stack_index = 0
        self.__stack_limit = len(self.__stack)
        self.__cmd_limit = len(self.__stack[0]["cmds"])
        return self

    def __next__(self):
        self.__cmd_index += 1
        if self.__cmd_index >= self.__cmd_limit:
            self.__cmd_index = 0
            self.__stack_index += 1
            try:
                self.__cmd_limit = len(self.__stack[self.__stack_index]["cmds"])
            except IndexError:
                pass
        if self.__stack_index == self.__stack_limit:
            # raise StopIteration
            pass
        return self.__stack[self.__stack_index]["cmds"][self.__cmd_index]

    def __str__(self):
        string = "<------------------------------------------->\n"
        for i in self.__stack:
            string += f"\n -> {i['type']}: {i['name']}\n"
            for j in i["cmds"]:
                string += f"{j}\n"
        string += "<------------------------------------------->\n"
        return string







