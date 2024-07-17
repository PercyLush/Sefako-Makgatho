import re

def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptions.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(.+)\s*\(\s*([A-Z]+\s*\d{3})\s*\)"
        new_file = re.sub(pattern, r"\nName: \1\nCode: \2", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptionsFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(new_file)

def description():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptionsFinal.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"Code:(.+)\n(.+)"
        new_file = re.sub(pattern, r"Code: \1\nDescription: \2", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptionsFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(new_file)

code()
description()