class Opcode:
    __first_operand = None
    __second_operand = None
    __mod = None
    __value = None
    __index = None

    def __init__(self, mod=False, f=None, s=None, val=None):
        self.__mod = mod
        self.__first_operand = f
        self.__second_operand = s
        self.__value = val

    def __getitem__(self, item):
        if 0 <= item <= len(self.__value):
            return [self.__first_operand[item], self.__second_operand[item], self.__value[item]]