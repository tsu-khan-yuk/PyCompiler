#######################################################################################################################
# -> Done: Иван Суханюк
# -> Date of creation: 25.05.2020
# -> last change: 25.05.2020
# -> related files: assemble.txt
#######################################################################################################################
from PyCompiler.asm_types import lables, Macro, data
from PyCompiler.Instrument.Database import *
from PyCompiler.asm_types import parser

size = 0


# todo: переделать lexer.py с использование ООП


def cmd_manager(ln: str) -> int:
    sz = 0
    if "DW" in ln or "DD" in ln or "DB" in ln:
        sz = constant_size(ln)
    elif "Mov" in ln:
        sz = mov_processing(ln)
    elif "Jbe" in ln or ln.endswith(":\n"):
        sz = jmp_processing(ln)
    elif "Or" in ln:
        sz = or_processing(ln)
    elif "Inc" in ln:
        sz = inc_processing()
    elif "And" in ln:
        sz = and_processing(ln)
    elif "Adc" in ln:
        sz = adc_processing(ln)
    elif "Cbw" in ln:
        sz = cbw_processing(ln)
    elif "Cmp" in ln:
        sz = cmp_processing(ln)
    return sz


def cmp_processing(ln: str) -> int:
    if ":" in ln:
        return 5
    if "[" in ln:
        return 0


def cbw_processing(ln: str) -> int:
    return 1


def adc_processing(ln: str) -> int:
    return 2


def and_processing(ln: str) -> int:
    if "[" in ln:
        return 5
    return 0


def inc_processing() -> int:
    return 1


def or_processing(ln: str) -> int:
    if "[" in ln:
        return 5
    return 2


def jmp_processing(ln: str) -> int:
    if ":" in ln:
        ln = ln.split()[0]
        lables.append(ln[:-1])
        data["lables"].append([ln[:-1], data["segments"][-1], size])
        return 0
    ln = ln.split()
    if ln[1] in lables:
        return 2
    else:
        return 4


def mov_processing(ln: str) -> int:
    if ":" in ln or "[" in ln:
        return 5
    ln = ln.split()
    if ln[1][:-1] in registers and ln[2].isdigit():
        return 3
    return 0


def constant_size(tmp: str) -> int:
    tmp = tmp.split()
    buff = 0
    if '"' in tmp[-1]:
        val = tmp[-1]
        buff = len(val[1:-1])
    elif tmp[1] == "DW":
        buff = constant_type["DW"]
    elif tmp[1] == "DD":
        buff = constant_type["DD"]
    elif tmp[1] == "DB":
        buff = constant_type["DB"]
    data["constants"].append([tmp[0], tmp[1], size, data["segments"][-1]])
    return buff


def main_first_pass_function():
    with open("Product Files/assembly.txt", "rt") as assembly:
        with open("Product Files/first_pass_res.txt", "w") as listing:

            def first_tab(asm_file, lst_file):
                active_seg = 0
                active_macro = 0
                macro = ""
                global size
                for line in asm_file:
                    if line is "\n":
                        continue
                    parser(line)
                    lst_file.write(f"\t{(hex(size)[2:].upper())}\t{line}")
                    if "ENDM" in line:
                        lst_file.write("\n")
                        active_macro -= 1
                    if "SEGMENT" in line:
                        active_seg += 1
                        data["segments"].append([line.split()[0]])
                    if active_macro > 0:
                        Macro[macro].append(line)
                    if "MACRO" in line:
                        active_macro += 1
                        macro = (line.split())[0]
                        Macro[macro] = []
                    elif macro in line:
                        for i in Macro[macro]:
                            lst_file.write(f"\t{(hex(size)[2:].upper())}\t\t\t{i}")
                            size += cmd_manager(i)
                    if active_seg > 0:
                        size += cmd_manager(line)
                    if "ENDS" in line:
                        data["segments"][-1].append(size)
                        lst_file.write("\n")
                        active_seg -= 1
                        size = 0

            def second_tab(lst_file) -> None:
                lst_file.write("\n\nSYMBOL TABLE\nSymbol Names\nName\t\tType\tValue\n")
                for var in data["constants"]:
                    lst_file.write(f"{var[0]}\t\t{var[1]}\t\t{var[3][0]}:{(hex(var[2]))[2:]}\n")
                for lab in data["lables"]:
                    lst_file.write(f"{lab[0]}\t\tnear\t{lab[1][0]}:{(hex(lab[2]))[2:]}\n")

            def third_tab(lst_file) -> None:
                lst_file.write("\nMacro Name\n")
                if len(Macro) is 0:
                    lst_file.write("None")
                else:
                    for m in Macro.keys():
                        lst_file.write(m)

            def fourth_tab(lst_file) -> None:
                lst_file.write("\n\nGroups and Segments\n")
                lst_file.write("Name\t\tBit\t\tSize\tAlign\tClass\n")
                for seg in data["segments"]:
                    lst_file.write(f"{seg[0]}\t\t16\t\t{hex(seg[1])[2:].upper()}\t\tpara\tnone\n")

            first_tab(assembly, listing)
            second_tab(listing)
            third_tab(listing)
            fourth_tab(listing)
