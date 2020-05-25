#######################################################################################################################
# -> Done: Иван Суханюк
# -> Date of creation: 25.05.2020
# -> last change: 25.05.2020
# -> related files: assemble.txt
#######################################################################################################################

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
    first_operand = None


class Cmd_database:
    comand = {
        "Cbw": {
            "opcode": "98"
        },
        "Inc": {
            "opcode": "FF"
        },
        "Adc": {
            "opcode": {
                ("r/m8", "r8"): "10",
                ("r/m16", "r16"): "11",
                "r8,r/m8": "12",
                "r16,r/m16": "13"
            }
        },
        "Cmp": {
            "opcode": {
                "r8,r/m8": "3a",
                "r16,r/m16": "3b"
            }
        },
        "And": {
            "opcode": {
                "r/m8,r8": "20",
                "r/m16,r16": "21",
            }
        },
        "Mov": {
            "opcode": {
                "r8,imm8": "b0",
                "r16,imm16": "b8",
                "r/m8,imm8": "c6",
                "r/m16,imm16": "c7"
            }
        },
        "Or": {
            "opcode": {
                "r/m8,imm8": "80",
                "r/m16,imm16": "81",
                "r/m16,imm8": "83"
            }
        },
        "Jbe": {
            "opcode": {
                "rel8": "76",
                "rel16/32": "86"
            }
        }
    }
