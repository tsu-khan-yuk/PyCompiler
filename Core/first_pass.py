from Core.Tools.Command import Command
from Core.Tools.Line_stack import Stack
from Core.Tools.Constant import Constant
from Core.Tools.Database import regularBase, labels
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
        elif "END" in string or string == "\n":
            pass
        else:

            # TODO: check 're' for 0 or more elements in string
            constant = regularBase['constants']['number'].search(string)
            constantString = regularBase['constants']['string'].search(string)
            basicCommand = regularBase['commands']['two word cmd'].search(string)
            jumpCommand = regularBase['commands']['Jbe cmd'].search(string)
            cbwCommand = regularBase['commands']['Cbw cmd'].search(string)
            lableLine = regularBase['lables'].search(string)

            if basicCommand or jumpCommand or cbwCommand:
                stack.push_line(Command(string))
            elif constant or constantString:
                stack.push_line(Constant(string))
            elif lableLine is not None:
                labels['jump'].append(lableLine.string.split())
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


if __name__ == '__main__':
    main_first_pass_function()