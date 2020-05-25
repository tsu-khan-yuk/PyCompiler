#######################################################################################################################
# -> Done: Иван Суханюк
# -> Date of creation: 25.05.2020
# -> last change: 25.05.2020
# -> related files: assemble.txt
#######################################################################################################################
from PyCompiler.asm_types import asm_type, reg16, lables, macro_cmd


def cmd_manager(ln: str) -> int:
    sz = 0
    if "DW" in ln or "DD" in ln or "DB" in ln:
        sz = constant_size(ln)
    elif "Mov" in ln:
        sz = mov_processing(ln)
    elif "Jbe" in ln or ln.endswith(":"):
        sz = jmp_processing(ln)
    elif "Or" in ln:
        sz = or_processing(ln)
    elif "Inc" in ln:
        sz = inc_processing()
    return sz


def inc_processing() -> int:
    return 1


def or_processing(ln: str) -> int:
    if "[" in ln:
        return 5
    return 0


def jmp_processing(ln: str) -> int:
    if ":" in ln:
        lables.append(ln[:-1])
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
    if ln[1][:-1] in reg16 and ln[2].isdigit():
        return 3
    return 0


def constant_size(tmp: str) -> int:
    tmp = tmp.split()
    if '"' in tmp[-1]:
        val = tmp[-1]
        return len(val[1:-1])
    elif tmp[1] == "DW":
        return asm_type["DW"]
    elif tmp[1] == "DD":
        return asm_type["DD"]
    elif tmp[1] == "DB":
        return asm_type["DB"]


with open("Files/assembly.txt", "rt") as assembly:
    with open("Files/first.txt", "w") as listing:
        active_seg = 0
        active_macro = 0
        size = 0
        macro = ""
        for line in assembly:
            if line is "\n":
                continue
            listing.write(f"\t{(hex(size)[2:].upper())}\t{line}")
            if "ENDM" in line:
                listing.write("\n")
                active_macro -= 1
            if "SEGMENT" in line:
                active_seg += 1
            if active_macro > 0:
                macro_cmd.append(line)
            if macro in line:
                for i in macro_cmd:
                    listing.write(f"\t{(hex(size)[2:].upper())}\t\t\t\t{i}")
                    size += cmd_manager(i)
                macro_cmd.clear()
            if active_seg > 0:
                size += cmd_manager(line)
            if "MACRO" in line:
                active_macro += 1
                macro = (line.split())[0]
            if "ENDS" in line:
                listing.write("\n")
                active_seg -= 1
                size = 0
