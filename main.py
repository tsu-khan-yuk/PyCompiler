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
        if ":" in word or ("[" in word and "]" in word) or "," in word:
            if word.endswith(":"):
                listing.write(f"\t{word[:-1]}" + " " * (15 - len(word[:-1])) + f"{len(word[:-1])} \t")
                listing.write("Ідентифікатор невизначений, або мітка\n")

            if word.startswith("CS"):
                listing.write("\tCS" + " "*13 + "2\tІдентифікатор кодового сегменту\n")
            elif word.startswith("ES"):
                listing.write("\tES" + " "*13 + "2\tІдентифікатор додаткового кодового сегменту\n")
            elif word.startswith("DS"):
                listing.write("\tDS" + " "*13 + "2\tІдентифікатор сегменту дати\n")
            listing.write("\t:" + " "*14 + "1\tОдносимвольна\n")

            if assume:
                listing.write(f"\t{word[3:-1]}" + " " * (15 - len(word[3:-1])) + f"{len(word[3:-1])} \t")
                listing.write("Ідентифікатор невизнаечений, або мітка\n")
                if word[-1] == ",":
                    listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
            else:


        else:
            listing.write(f"\t{word}" + " "*(15 - len(word)) + f"{len(word)} \t")
            if word == "MACRO":
                listing.write("Ідентифікатор директиви макровизначення\n")
            elif word == "SEGMENT":
                listing.write("Ідентифікатор директиви початку сегменту\n")
            elif word == "ASSUME":
                listing.write("Ідентифікатор директиви ASSUME\n")
                assume = True
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
            else:
                listing.write("Ідентифікатор невизнаечений, або мітка\n")
    listing.write("\n")


assembly.close()
listing.close()
