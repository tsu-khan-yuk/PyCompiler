def search_ident(line: str, tmp_ch: str) -> dict:
	check = {
		"assume": False,
		"coma": False,
		"lable": False,
		"macro": None
	}

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
				check["macro"] = True
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
				if not check["macro"]:
					tmp = word
	return check
