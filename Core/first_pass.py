from PyCompiler.Instrument.Command import Command
from PyCompiler.Instrument.Line_stack import Stack
from PyCompiler.Instrument.Constant import Constant
from PyCompiler.Instrument.Database import regular_base

stack = Stack()


def parser(file):
    for string in file:
        if "SEGMENT" in string:
            buff = string.split()
            stack.init_seg(buff[0], "S")
        elif "MACRO" in string:
            buff = string.split()
            stack.init_seg(buff[0], "M")
        elif "ENDM" in string or "ENDS" in string:
            pass
        else:
            constant = regular_base[0].search(string)
            constant_string = regular_base[1].search(string)
            cmd = regular_base[2].search(string)
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
            i = iter(stack)
            for line in assembly:
                if "END" in line:
                    size = 0
                if not ("SEGMENT" in line or "MACRO" in line or "END" in line or line == "\n" or "ASSUME" in line
                        or ":\n" in line):
                    print(next(i))
                listing.write(f"{counter}\t\t{size}\t\t\t{line}")  # 0x0
                counter += 1
