#######################################################################################################################
# -> Done: Иван Суханюк
# -> Date of creation: 25.05.2020
# -> last change: 25.05.2020
# -> related files: assemble.txt
#######################################################################################################################
from PyCompiler.asm_types import asm_type, reg16, lables, macro_cmd, data
size = 0


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
    return 7


def cbw_processing(ln: str) -> int:
    return 2


def adc_processing(ln: str) -> int:
    return 3


def and_processing(ln: str) -> int:
    if "[" in ln:
        return 6
    return 0


def inc_processing() -> int:
    return 2


def or_processing(ln: str) -> int:
    if "[" in ln:
        return 7
    return 0


def jmp_processing(ln: str) -> int:
    if ":" in ln:
        ln = ln.split()[0]
        lables.append(ln[:-1])
        return 0
    ln = ln.split()
    if ln[1] in lables:
        return 2
    else:
        return 6


def mov_processing(ln: str) -> int:
    if ":" in ln or "[" in ln:
        return 7
    ln = ln.split()
    if ln[1][:-1] in reg16 and ln[2].isdigit():
        return 4
    return 0


def constant_size(tmp: str) -> int:
    tmp = tmp.split()
    buff = 0
    if '"' in tmp[-1]:
        val = tmp[-1]
        buff = len(val[1:-1])
    elif tmp[1] == "DW":
        buff = asm_type["DW"]
    elif tmp[1] == "DD":
        buff = asm_type["DD"]
    elif tmp[1] == "DB":
        buff = asm_type["DB"]
    data["constants"].append([tmp[0], tmp[1], size, data["segments"][-1]])
    return buff


with open("Files/assembly.txt", "rt") as assembly:
    with open("Files/first.txt", "w") as listing:
        
        def first_tab(asm_file, lst_file):
            active_seg = 0
            active_macro = 0
            macro = ""
            global size
            for line in asm_file:
                if line is "\n":
                    continue
                lst_file.write(f"\t{(hex(size)[2:].upper())}\t{line}")
                if "ENDM" in line:
                    lst_file.write("\n")
                    active_macro -= 1
                if "SEGMENT" in line:
                    active_seg += 1
                    data["segments"].append(line.split()[0])
                if active_macro > 0:
                    macro_cmd.append(line)
                if macro in line:
                    for i in macro_cmd:
                        lst_file.write(f"\t{(hex(size)[2:].upper())}\t\t\t\t{i}")
                        size += cmd_manager(i)
                    macro_cmd.clear()
                if active_seg > 0:
                    size += cmd_manager(line)
                if "MACRO" in line:
                    active_macro += 1
                    macro = (line.split())[0]
                if "ENDS" in line:
                    lst_file.write("\n")
                    active_seg -= 1
                    size = 0
        
        
        def second_tab(asm_file, lst_file) -> None:
            lst_file.write("\n\nName\t\tType\tValue\n\n")
            for var in data["constants"]:
                lst_file.write(f"{var[0]}\t\t{var[1]}\t\t{var[3]}:{var[2]}\n")
            
        
        first_tab(assembly, listing)
        second_tab(assembly, listing)















