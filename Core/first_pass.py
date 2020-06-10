from PyCompiler.Instrument.Command import Command
from PyCompiler.Instrument.CMD_stack import Stack
from PyCompiler.Instrument.Constant import Constant
from re import search
stack = Stack()


def parser(file):
    for string in file:
        if "SEGMENT" in string:
            buff = string.split()
            stack.init_segment(buff[0])
        elif "MACRO" in string:
            buff = string.split()
            stack.init_marco(buff[0])
        elif "ENDM" in string or "ENDS" in string:
            pass
        else:
            constant = search(r"[A-Z]\w+\s+(DW|DD|DB)\s+\d+\w\n$", string)
            constant_string = search(r'[A-Z]\w+\s+DB\s+"\w+"\n$', string)
            cmd = search(r"\w{2,3}\s+"
                         r"(((AX|AH|AL|BX|BH|BL|CX|CL|CH|DI|SI)|"
                         r"(CS:\w{3}\[(BP|BX) \+ (SI|DI)\])|(\w+\[(BP|BX) \+ (SI|DI)\])),\s"
                         r"((AX|AH|AL|BX|BH|BL|CX|CL|CH|DI|SI)|"
                         r"(CS:\w{3}\[(BP|BX) \+ (SI|DI)\])|(\w+\[(BP|BX) \+ (SI|DI)\])|"
                         r"(\d+))|(AX|AH|AL|BX|BH|BL|CX|CL|CH|DI|SI))\n$", string)
            if cmd:
                stack.push_line(Command(string))
            elif constant or constant_string:
                stack.push_line(Constant(string))


def main_first_pass_function():
    with open("Product Files/assembly.txt", "rt") as assembly:
        with open("Product Files/first_pass_res.txt", "w") as listing:
            counter = 1
            parser(assembly)
            assembly.seek(0)
            size = 0
            for line in assembly:
                listing.write(f"{counter}\t\t{size}\t\t\t{line}")
                counter += 1
