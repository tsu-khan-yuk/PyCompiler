###########################################################################################################
# -> Выполнил: Иван Суханюк
# -> Дата создания: 16.04.2020
# -> Последние изменения: 16.04.2020
# -> Связанеые файлы: assembly.txt
###########################################################################################################
assembly = open("assembly.txt", "rt")
listing = open("main.txt", "w")
count = 0
for i in assembly:
    assume = False
    count += 1
    listing.write("Рядок номер [" + str(count) + "]:\t" + i)
    lst1 = i.split()
    for j in lst1:
        if j == "MACRO":
            listing.write(">>> Ідентифікатор директиви макровизначення\n\n")
        elif j == "SEGMENT":
            listing.write(">>> Ідентифікатор директиви початку сегменту\n\n")
        elif j == "DB":
            listing.write(">>> Ідентрифікатор директиви 1 байтового типу данних\n\n")
        elif j == "DW":
            listing.write(">>> Ідентрифікатор директиви 2-х байтового типу данних\n\n")
        elif j == "DD":
            listing.write(">>> Ідентрифікатор директиви 4-х байтового типу данних\n\n")
        elif j == "ENDS":
            listing.write(">>> Ідентрифікатор директиви закінчення сегменту\n\n")
        elif j == "ENDM":
            listing.write(">>> Ідентрифікатор директиви закінчення макровизначення\n\n")
        elif j == "END":
            listing.write(">>> Ідентифікатор директиви закінчення програми\n\n")
        elif j == "AX":
            listing.write(">>> Ідентифікатор регістора аккумулятора")
        elif j == "BX":
            listing.write(">>> Ідентифікатор ")
        elif j == "DI":
            listing.write(">>> ")
        elif j == "SI":
            listing.write(">>> ")
        elif j == "BP":
            listing.write(">>> ")
        elif j == "Inc" or j == "Mov" or j == "Or" or j == "Cmp" or j == "Adc" or j == "Cbw" or \
                j == "And" or j == "Jbe":
            listing.write(">>> Ідентифікатор мнемонічного коду машинної інструкції\n\n")
        elif j.startswith("CS") or j.startswith("ES") or j.startswith("DS"):
            listing.write(">>> Ідетифікатор сегментного регістра")
            lst2 = j.split(":")
            for k in lst2:
                if k == "CS":
                    listing.write(" кодів\n")
                elif k == "ES":
                    listing.write(" додаткових данних\n")
                elif k == "DS":
                    listing.write(" данних\n")
        else:
            listing.write(">>> Ідентифікатор невизнаечений, або мітка\n")


assembly.close()
listing.close()
