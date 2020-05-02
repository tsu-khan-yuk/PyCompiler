###########################################################################################################
# -> Выполнил: Иван Суханюк
# -> Дата создания: 16.04.2020
# -> Последние изменения: 02.05.2020
# -> Связанеые файлы: assembly.txt
###########################################################################################################
assembly = open("assembly.txt", "rt")
listing = open("main.txt", "w")
line_count = 0
for line in assembly:
    assume = False
    line_count += 1
    listing.write(f"Рядок номер [{str(line_count)}]:  {line}")
    lst1 = line.split()
    for word in lst1:
        listing.write(f"\t{word}" + " "*(15 - len(word)) + f"{len(word)} \t")
        if word == "MACRO":
            listing.write("Ідентифікатор директиви макровизначення\n")
        elif word == "SEGMENT":
            listing.write("Ідентифікатор директиви початку сегменту\n")
        elif word == "DB":
            listing.write("Ідентрифікатор директиви 1 байтового типу данних\n")
        elif word == "DW":
            listing.write("Ідентрифікатор директиви 2-х байтового типу данних\n")
        elif word == "DD":
            listing.write("Ідентрифікатор директиви 4-х байтового типу данних\n")
        elif word == "ENDS":
            listing.write("Ідентрифікатор директиви закінчення сегменту\n")
        elif word == "ENDM":
            listing.write("Ідентрифікатор директиви закінчення макровизначення\n")
        elif word == "END":
            listing.write("Ідентифікатор директиви закінчення програми\n")
        elif word == "AX":
            listing.write("Ідентифікатор регістра аккумулятора\n")
        elif word == "BX":
            listing.write("Ідентифікатор регістра бази\n")
        elif word == "DI":
            listing.write("Ідертифікатор регітсра DI\n")
        elif word == "SI":
            listing.write("Ідентифікатор регістра SI\n")
        elif word == "BP":
            listing.write("Ідентифікатор регітсра BP\n")
        elif word == "Inc" or word == "Mov" or word == "Or" or word == "Cmp" or word == "Adc" or word == "Cbw" or \
                word == "And" or word == "Jbe":
            listing.write("Ідентифікатор мнемонічного коду машинної інструкції\n")
        elif word.startswith("CS") or word.startswith("ES") or word.startswith("DS"):

            # listing.write("Ідетифікатор сегментного регістра")
            # lst2 = word.split(":")
            # for k in lst2:
            #     if k == "CS":
            #         listing.write(" кодів\n")
            #     elif k == "ES":
            #         listing.write(" додаткових данних\n")
            #     elif k == "DS":
            #         listing.write(" данних\n")
        else:
            listing.write("Ідентифікатор невизнаечений, або мітка\n")
    listing.write("\n")


assembly.close()
listing.close()
