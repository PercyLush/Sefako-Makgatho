import re

def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealthCourseData.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(M\s*o\s*d\s*u\s*l\s*e\s*C\s*o\s*d\s*e\s*:\s*)"
        file_new = re.sub(pattern, r"Code: ", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def name():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(M\s*o\s*d\s*u\s*l\s*e\s*N\s*a\s*m\s*e\s*:\s*)"
        file_new = re.sub(pattern, r"Name: ", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def description():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(M\s*o\s*d\s*u\s*l\s*e\s*C\s*o\s*n\s*t\s*e\s*n\s*t\s*:\s*|C\s*o\s*n\s*t\s*e\s*n\s*t\s*:\s*)"
        file_new = re.sub(pattern, r"Description: ", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def prerequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(P\s*r\s*e\s*-\s*r\s*e\s*q\s*u\s*i\s*s\s*i\s*t\s*e\s*m\s*o\s*d\s*u\s*l\s*e\s*s\s*:\s*|Pre-requisite module/s\s*:\s*|Pre-requisites module/s\s*:\s*|Pre-requisite module/s\s*|Pre-requisite\s*\n\s*module/s\s*:\s*|Pre-requisite modules\s*\n\s*for this module:\s*|Pre-requisite\s*modules\s*for\s*this\s*module\s*:\s*)"
        file_new = re.sub(pattern, r"Prerequisite: ", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def corequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(C\s*o\s*-\s*r\s*e\s*q\s*u\s*i\s*s\s*i\s*t\s*e\s*m\s*o\s*d\s*u\s*l\s*e\s*s\s*:\s*|Co-requisite module/s\s*:\s*|Co-requisites module/s\s*:\s*|Co-requisite module/s\s*|Co-requisite\s*\n\s*module/s\s*:\s*|Co-requisites modules\s*\n\s*for module:\s*|Co-requisites\s*modules\s*for\s*module:\s*)"
        file_new = re.sub(pattern, r"Corequisite: ", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def assessments():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(A\s*s\s*s\s*e\s*s\s*s\s*m\s*e\s*n\s*t\s*W\s*e\s*i\s*g\s*h\s*t\s*i\s*n\s*g\s*:\s*|S\s*t\s*r\s*u\s*c\s*t\s*u\s*r\s*e\s*:\s*)"
        file_new = re.sub(pattern, r"\nAssessments: ", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def empty_space():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Code:(.+))"
        file_new = re.sub(pattern, r"\n\n\1", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealth.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

code()
name()
description()
prerequisite()
corequisite()
assessments()
empty_space()
