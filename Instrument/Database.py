from PyCompiler.Instrument.Opcode import Opcode


segment_tab = {
    "CS": None,
    "DS": None,
    "SS": None,
    "ES": None,
    "GS": None,
    "FS": None
}

constant_type = {
    "DW": 2,
    "DD": 4,
    "DB": 1
}

registers = {"AX", "AH", "AL", "BX", "BH", "BL", "CX", "CL", "CH", "DI", "SI"}

command = {
    # todo: изменить структуру с учетом mod r/m
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