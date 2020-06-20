from PyCompiler.Instrument.Command import Command
from PyCompiler.Instrument.Line_stack import Stack
from PyCompiler.Instrument.Constant import Constant
from PyCompiler.Instrument.Database import regular_base, labels
stack = Stack()
undef = []


def undef_line_proc(line):
    undef.append(line)


def parser(file):
    for string in file:
        if "SEGMENT" in string:
            buff = string.split()
            stack.init_seg(buff[0], "S")
        elif "MACRO" in string:
            buff = string.split()
            stack.init_seg(buff[0], "M")
        elif "END" in string:
            pass
        else:
            # todo: check 're' for 0 or more elements in string
            constant = regular_base[0].search(string)
            constant_string = regular_base[1].search(string)
            cmd = regular_base[2].search(string)
            jump = regular_base[3].search(string)
            cbw = regular_base[4].search(string)
            lab = regular_base[5].search(string)
            if cmd or jump or cbw:
                stack.push_line(Command(string))
            elif constant or constant_string:
                stack.push_line(Constant(string))
            elif lab is not None:
                labels['jump'].append(lab.string.split())
            else:

                undef_line_proc(string)


def main_first_pass_function():
    with open("Product Files/assembly.txt", "rt") as assembly:
        with open("Product Files/first_pass_res.txt", "wt") as listing:
            counter = 1
            parser(assembly)
            assembly.seek(0)
            size = 0
            i = iter(stack)
            for line in assembly:
                if "END" in line:
                    size = 0
                # if not ("SEGMENT" in line or "MACRO" in line or "END" in line or line == "\n" or "ASSUME" in line
                #         or ":\n" in line):
                #     print(next(i))
                # else:
                #     listing.write("[passed] ")
                listing.write(f"{counter}\t\t{size}\t\t\t{line}")  # 0x0
                counter += 1
    print(undef)