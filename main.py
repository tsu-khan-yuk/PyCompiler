###########################################################################################################
# -> Выполнил: Иван Суханюк
# -> Дата создания: 16.04.2020
# -> Последние изменения: 02.05.2020
# -> Связанеые файлы: assembly.txt
###########################################################################################################


def counter(wrd: str) -> int:
	if "[" not in wrd:
		wrd = wrd.split()
		cnt = len(wrd)
	else:
		cnt = 1
	for i in wrd:
		if ":" in i:
			cnt += 1
		if "[" in i or "]" in i:
			cnt += 2
		if "+" in i:
			cnt += 1
	return cnt


def token_counter(Line: str) -> dict:
	dct = dict()
	if Line.endswith(":"):
		dct[0] = 1
		return dct
	if "," in Line:
		lst = Line.split(",")
		lst = lst[0].split() + lst
		lst.pop(2)
	else:
		lst = Line.split()
	token = 0
	count = 0
	for i in lst:
		token += counter(i)
		count += 1
		dct[count] = token
		token = 0
	return dct


assembly = open("assembly.txt", "rt")
listing = open("main.txt", "w")
line_count = 0
for line in assembly:
	if line is "\n":
		continue
	assume = False
	coma = False
	line_count += 1
	listing.write(f"Рядок номер [{str(line_count)}]:  {line[:-1]}" + "\t\t" + str(token_counter(line)) + "\n")
	lst1 = line.split()
	for word in lst1:
		if ":" in word or "[" in word or "]" in word:
			if word.endswith(":"):
				listing.write(f"\t{word[:-1]}" + " " * (15 - len(word[:-1])) + f"{len(word[:-1])} \t")
				listing.write("Ідентифікатор невизначений, або мітка\n")

			if word.startswith("CS"):
				listing.write("\tCS" + " " * 13 + "2\tІдентифікатор кодового сегменту\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")
			elif word.startswith("ES"):
				listing.write("\tES" + " " * 13 + "2\tІдентифікатор додаткового кодового сегменту\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")
			elif word.startswith("DS"):
				listing.write("\tDS" + " " * 13 + "2\tІдентифікатор сегменту дати\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")

			if assume:
				listing.write(f"\t{word[3:-1]}" + " " * (15 - len(word[3:-1])) + f"{len(word[3:-1])} \t")
				listing.write("Ідентифікатор невизнаечений, або мітка\n")
				if word[-1] == ",":
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
			else:
				if "[" in word:
					left = word.find(":")
					left = 0 if left < 0 else left + 1
					right = word.find("[")
					str1 = f"\t{word[left:right]}"
					str2 = " " * (15 - len(word[left:right]))
					str3 = f"{len(word[left:right])} \t"
					listing.write(str1 + str2 + str3)
					listing.write("Ідентифікатор невизнаечений, або мітка\n")
					listing.write("\t[" + " " * 14 + "1\tОдносимвольна\n")
					listing.write(f"\t{word[-2:]}" + " " * (15 - len(word[-2:])) + f"{len(word[-2:])} \t")
					listing.write("Ідентіфікатор регістра " + "BX\n" if word[-2:] == "BX" else "BP\n")
				elif "]" in word:
					right = -2 if coma else -1
					listing.write(f"\t{word[:right]}" + " " * (15 - len(word[:right])) + f"{len(word[:right])} \t")
					listing.write("Ідентіфікатор регістра " + "DI\n" if word[:-2] == "DI" else "SI\n")
					listing.write("\t]" + " " * 14 + "1\tОдносимвольна\n")
					if coma:
						listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
						coma = False
		else:
			tmp = word[:-1] if coma and not (word == "+") else word
			str1 = f"\t{tmp}"
			str2 = " " * (15 - len(tmp))
			str3 = f"{len(tmp)} \t"
			listing.write(str1 + str2 + str3)
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
			elif word[:-1].isdigit():
				if word[-1] is "H":
					listing.write("Ідентифікатор шістнадцяткової константи\n")
				elif word[-1] is "D":
					listing.write("Ідентифікатор десяткової константи\n")
				elif word[-1] is "B":
					listing.write("Ідентифікатор двійкової константи\n")
			elif word.isdigit():
				listing.write("Ідентифікатор десяткової констансти\n")
			elif word.startswith('"') and word.endswith('"'):
				listing.write("Ідентифікатор текстової константи\n")
			elif word == "AX" or "AX," in word:
				listing.write("Ідентифікатор регістра аккумулятора\n")
				if coma:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					coma = False
			elif word == "BX" or "BX," in word:
				listing.write("Ідентифікатор регістра бази\n")
				if coma:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					coma = False
			elif word == "DI" or "DI," in word:
				listing.write("Ідертифікатор регітсра DI\n")
				if coma:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					coma = False
			elif word == "SI" or "SI," in word:
				listing.write("Ідентифікатор регістра SI\n")
				if coma:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					coma = False
			elif word == "BP" or "BP," in word:
				listing.write("Ідентифікатор регітсра BP\n")
				if coma:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					coma = False
			elif word == "Inc" or word == "Mov" or word == "Or" or word == "Cmp" or word == "Adc" or \
					word == "Cbw" or word == "And" or word == "Jbe":
				listing.write("Ідентифікатор мнемонічного коду машинної інструкції\n")
				if not (word == "Jbe" or word == "Cbw" or word == "Inc"):
					coma = True
			else:
				listing.write("Ідентифікатор невизнаечений, або мітка\n")
	listing.write("\n")

assembly.close()
listing.close()
