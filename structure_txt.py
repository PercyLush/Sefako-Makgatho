import re

def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOH.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"([A-Z]+\s*\d{3})\s*(.+)\s*"
        new_file = re.sub(pattern, r"\nCode: \1\nName: \2", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(new_file)

def duration():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(\sY\s(.+)|\sS2\s(.+)|\sS2\s(.+))"
        new_file = re.sub(pattern, r"\nDuration: \1", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(new_file)

def credit():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(\d+\s*Credits)"
        new_file = re.sub(pattern, r"\nCredit: \1\n", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(new_file)

def nqf():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(\d{1}\s*NQF)"
        new_file = re.sub(pattern, r"\nNQF: \1\n\n", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\BDSandBOHFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(new_file)

code()
duration()
credit()
#nqf()