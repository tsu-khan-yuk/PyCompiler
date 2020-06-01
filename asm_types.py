# Ідентифікатори
# Містять великі букви латинского алфавіту та цифри. Починаються з букви.
# Константи
# Шістнадцятерічні, десяткові, двійкові та текстові константи
# Директиви
# END,
# SEGMENT - без операндів, ENDS, ASSUME,
# MACRO (без параметрів або з одним параметром) ENDM
# DB,DW,DD з одним операндом - константою (строкові константи тільки для DB)
# Розрядність даних та адрес
# 16- розрядні дані та зміщення в сегменті, 32 -розрядні дані та зміщення не
# використовуються
# Адресація операндів пам'яті
# Базова індексна адресація із зміщенням по ідентифікатору (Val1[bp+si],Val1[bx+di]
# Заміна сегментів
# Префікси заміни сегментів можуть задаватись явно, а при необхідності автоматично
# генеруються транслятором

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
from re import *

def parser(string: str):
    global cmd_stack
    const = findall(r"\s+\w{2}\s{2}\d+\w$", string)
    cmd = findall(r"\s{8}\w+(\s{5}|\s{6})\w{2}", string)
    if cmd:
        exmpl = Command(string)
        print(exmpl)
    elif const:
        pass
        # print("constant", const)


cmd_stack = []


class Command:
    __string = None
    __name = None
    __operands = None

    def __init__(self, string: str):
        self.__string = string
        self.__pars_processing()

    def __pars_processing(self):
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
        else:
            tokens = self.__string.split()
            self.__name = tokens[0]
            self.__operands = tokens[1]

    def __parse_operands(self):
        # todo: make ability to parse operands
        if isinstance(self.__operands, str):
            pass

    def __str__(self):
        s = "+-------------------+\n"
        s += f"| string:' {self.__string}'\n"
        s += f"| name: {self.__name}\n"
        s += f"| operands: {self.__operands}\n"
        s += "+--------------------+"
        return s


class Operand:
    # todo: will receive operand and calculate its` size
    pass


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


command = {
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
