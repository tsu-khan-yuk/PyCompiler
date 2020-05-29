# Cbw
# Inc reg
# Adc reg,reg
# Cmp reg,mem
# And mem,reg
# Mov reg,imm
# Or mem,imm
# Jbe
# Де reg – 8 або 16-розрядні РЗП
# mem – адреса операнда в пам’яті
# imm - 8 або 16 розрядні безпосередні дані (константи)


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


comand = {
    #todo: изменить структуру с учетом mod r/m
    "Cbw": Opcode(False, None, None, "0x98"),
    "Inc": Opcode(False, None, None, "0xff"),
    "Adc": Opcode(False, ["r/m8", "r/m16", "r8", "r16"], ["r8", "r16", "r/m8", "r/m16"],
                  ["0x10", "0x11", "0x12", "0x13"]),
    "Cmp": Opcode(False, ["r8", "r16"], ["r16", "r/m16"], ["0x3a", "0x3b"]),
    "And": Opcode(False, ["r/m8", "r/m16"], ["r8", "r16"], ["0x20", "0x21"]),
    "Mov": Opcode(False, ["r8", "r16", "r/m8", "r/m16"], ["imm8", "imm16", "imm8", "imm16"],
                  ["0xb0", "0xb8", "0xc6", "0xc7"]),
    "Or": Opcode(False, ["r/m8", "r/m16", "r/m16"], ["imm8", "imm16", "imm8"], ["0x80", "0x81", "0x83"]),
    "Jbe": Opcode(False, ["rel8", "rel16/32"], None, ["0x76", "0x86"])
}

# todo: добавить структуру для записи комнад и строчек сегментов

segment_tab = {
    "CS": None,
    "DS": None,
    "SS": None,
    "ES": None,
    "GS": None,
    "FS": None
}

asm_type = {
    "DW": 2,
    "DD": 4,
    "DB": 1
}

reg16 = {"BX", "DI", "AX", "SI"}

lables = []

Macro = dict()

data = {
    "segments": [],
    "constants": [],
    "lables": []
}
