###########################################################################################################
# -> Выполнил: Иван Суханюк
# -> Дата создания: 16.04.2020
# -> Последние изменения: 05.05.2020
# -> Связанеые файлы: assembly.txt
###########################################################################################################


def search_ident(line: str, listing) -> dict:
	check = {
		"assume": False,
		"coma": False,
		"lable": False,
		"macro": None
	}

	tmp_var = None
	lst1 = line.split()
	for word in lst1:
		if ":" in word or "[" in word or "]" in word:
			if word.endswith(":"):
				listing.write(f"\t{word[:-1]}" + " " * (15 - len(word[:-1])) + f"{len(word[:-1])} \t")
				listing.write("Ідентифікатор невизначений, або мітка\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")

			if word.startswith("CS"):
				listing.write("\tCS" + " " * 13 + "2\tІдентифікатор кодового сегменту\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")
			elif word.startswith("ES"):
				listing.write("\tES" + " " * 13 + "2\tІдентифікатор додаткового кодового сегменту\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")
			elif word.startswith("DS"):
				listing.write("\tDS" + " " * 13 + "2\tІдентифікатор сегменту дати\n")
				listing.write("\t:" + " " * 14 + "1\tОдносимвольна\n")

			if check["assume"]:
				listing.write(f"\t{word[3:-1]}" + " " * (15 - len(word[3:-1])) + f"{len(word[3:-1])} \t")
				listing.write("Ідентифікатор невизнаечений, або мітка\n")
				if word[-1] == ",":
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
			else:
				if "[" in word:
					left = word.find(":")
					left = 0 if left < 0 else left + 1
					right = word.find("[")
					f_str[0] = f"\t{word[left:right]}"
					f_str[1] = " " * (15 - len(word[left:right]))
					f_str[2] = f"{len(word[left:right])} \t"
					listing.write(f_str[0] + f_str[1] + f_str[2])
					listing.write("Ідентифікатор невизнаечений, або мітка\n")
					listing.write("\t[" + " " * 14 + "1\tОдносимвольна\n")
					listing.write(f"\t{word[-2:]}" + " " * (15 - len(word[-2:])) + f"{len(word[-2:])} \t")
					listing.write("Ідентіфікатор регістра " + ("BX\n" if word[-2:] == "BX" else "BP\n"))
				elif "]" in word:
					right = -2 if check["coma"] else -1
					listing.write(f"\t{word[:right]}" + " " * (15 - len(word[:right])) + f"{len(word[:right])} \t")
					listing.write("Ідентіфікатор регістра " + ("DI\n" if word[:-2] == "DI" else "SI\n"))
					listing.write("\t]" + " " * 14 + "1\tОдносимвольна\n")
					if check["coma"]:
						listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
						check["coma"] = False
		else:
			tmp = word[:-1] if check["coma"] and not (word == "+") else word
			f_str[0] = f"\t{tmp}"
			f_str[1] = " " * (15 - len(tmp))
			f_str[2] = f"{len(tmp)} \t"
			listing.write(f_str[0] + f_str[1] + f_str[2])
			if word == "MACRO":
				listing.write("Ідентифікатор директиви макровизначення\n")
				check["macro"] = tmp_var
				check["lable"] = True
			elif word == "SEGMENT":
				listing.write("Ідентифікатор директиви початку сегменту\n")
				check["lable"] = True
			elif word == "ASSUME":
				listing.write("Ідентифікатор директиви ASSUME\n")
				check["assume"] = True
			elif word == "DB":
				listing.write("Ідентрифікатор директиви 1 байтового типу данних\n")
				check["lable"] = True
			elif word == "DW":
				listing.write("Ідентрифікатор директиви 2-х байтового типу данних\n")
				check["lable"] = True
			elif word == "DD":
				listing.write("Ідентрифікатор директиви 4-х байтового типу данних\n")
				check["lable"] = True
			elif word == "ENDS":
				listing.write("Ідентрифікатор директиви закінчення сегменту\n")
				check["lable"] = True
			elif word == "ENDM":
				listing.write("Ідентрифікатор директиви закінчення макровизначення\n")
			elif word == "END":
				listing.write("Ідентифікатор директиви закінчення програми\n")
			elif word == "+":
				listing.write("Ідентифікатор знака суми\n")
			elif word.isdigit():
				listing.write("Ідентифікатор десяткової констансти\n")
			elif word[:-1].isdigit():
				if word[-1] is "H":
					listing.write("Ідентифікатор шістнадцяткової константи\n")
				elif word[-1] is "D":
					listing.write("Ідентифікатор десяткової константи\n")
				elif word[-1] is "B":
					listing.write("Ідентифікатор двійкової константи\n")
			elif word.startswith('"') and word.endswith('"'):
				listing.write("Ідентифікатор текстової константи\n")
			elif word == "AX" or "AX," in word:
				listing.write("Ідентифікатор регістра аккумулятора\n")
				if check["coma"]:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					check["coma"] = False
			elif word == "BX" or "BX," in word:
				listing.write("Ідентифікатор регістра бази\n")
				if check["coma"]:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					check["coma"] = False
			elif word == "DI" or "DI," in word:
				listing.write("Ідертифікатор регітсра DI\n")
				if check["coma"]:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					check["coma"] = False
			elif word == "SI" or "SI," in word:
				listing.write("Ідентифікатор регістра SI\n")
				if check["coma"]:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					check["coma"] = False
			elif word == "BP" or "BP," in word:
				listing.write("Ідентифікатор регітсра BP\n")
				if check["coma"]:
					listing.write("\t," + " " * 14 + "1\tОдносимвольна\n")
					check["coma"] = False
			elif word == "Inc" or word == "Mov" or word == "Or" or word == "Cmp" or word == "Adc" or \
				word == "Cbw" or word == "And" or word == "Jbe":
				listing.write("Ідентифікатор мнемонічного коду машинної інструкції\n")
				if not (word == "Jbe" or word == "Cbw" or word == "Inc"):
					check["coma"] = True
			else:
				listing.write("Ідентифікатор невизнаечений, або мітка\n")
				tmp_var = word
	return check


def tkn_counter(wrd: str) -> int:
	if "[" not in wrd:
		wrd = wrd.split()
		cnt = len(wrd)
	else:
		cnt = 1
	for i in wrd:
		if ":" in i:
			cnt += 2
		if "[" in i or "]" in i:
			cnt += 2
		if "+" in i:
			cnt += 1
	return cnt


def token_counter(Line: str, lables: dict, val) -> "dict, str":
	dct = dict()
	count = 0
	if Line.endswith(":\n") or lables["lable"] or val in Line:
		dct[1] = 0
		count = 1
	if "," in Line and not lables["assume"]:
		lst = Line.split(",")
		lst = lst[0].split("    ") + lst
		lst.remove("")
		lst.remove("")
		lst.pop(2)
	else:
		lst = Line.split()
	token = 1
	wait = 2

	if "Mov" in Line or "Or" in Line or "Cmp" in Line or "Adc" in Line or "And" in Line:
		lables["coma"] = True

	for i in lst:
		if wait == 0:
			count += 1
			wait = 2
		count += token
		token = tkn_counter(i)
		dct[count] = token
		if "," in i:
			wait -= 2
		if lables["coma"]:
			wait -= 1
	lables["coma"] = False
	return dct


def sh_up(dc: dict) -> dict:
	"""Функция делает сдвиг вверх по ключам в словаре"""
	dc[0] = 0
	for i in dc.keys():
		dc[i] = dc.get(i + 1)
	dc.pop(0)
	dc.pop(max(dc.keys()))
	return dc


def convert_str(buff_str: dict) -> str:
	"""Функция """
	if buff_str.get(1) == 0:
		buff_str = sh_up(buff_str)
		buff_str = str(buff_str)
		buff_str = "{1" + buff_str[5:]
	else:
		buff_str = str(buff_str)
		buff_str = "{0|" + buff_str[1:]
	buff_str = buff_str.replace(", ", "|")
	buff_str = buff_str.replace(":", "")
	return buff_str


with open("Files/assembly.txt", "rt") as assembly:
	with open("Files/lex.txt", "w") as lsting:
		line_count = 0
		f_str = ["", "", ""]
		mcro = None

		for ln in assembly:
			if ln is "\n":
				continue
			line_count += 1
			lsting.write(f"Рядок номер [{str(line_count)}]:  {ln}")
			ch = search_ident(ln, lsting)
			if ch["macro"]:
				mcro = ch["macro"]
			lsting.write("Таблиця: " + convert_str(token_counter(ln, ch, mcro)) + "\n\n")


