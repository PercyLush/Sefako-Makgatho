import json
import re

def prerequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFinal.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            prerequisite = {}

            if "Prerequisite" in item:
                prerequisite_text = item["Prerequisite"]
                code_pattern = r"([A-Z]+\s*\d+)"
                match = re.search(code_pattern, prerequisite_text)

                if "and" in prerequisite_text or "&" in prerequisite_text or "," in prerequisite_text or ";" in prerequisite_text:
                    if match:
                        new_data = re.split(r"\s*and\s*|\s*&\s*|\s*,\s*", prerequisite_text)
                        codes = []
                        if len(new_data) > 0:
                            for code in new_data:
                                module = {"Code": code.strip()}
                                codes.append(module)
                            prerequisite = {"$and": codes}

                elif "or" in prerequisite_text or "/" in prerequisite_text:
                    if match:
                        new_data = re.split(r"\s*or\s*|\s*/\s*", prerequisite_text)
                        codes = []
                        if len(new_data) > 0:
                            for code in new_data:
                                module = {"Code": code.strip()}
                                codes.append(module)
                            prerequisite = {"$or": codes}

                else:
                    if match:     
                        prerequisite = {"Code": prerequisite_text}
                    else:
                        prerequisite = {"Comment": prerequisite_text}
            item["Prerequisite"] = prerequisite
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFINAL.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

def corequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFINAL.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            corequisite = {}

            if "Corequisite" in item:
                corequisite_text = item["Corequisite"]
                code_pattern = r"([A-Z]+\s*\d+)"
                match = re.search(code_pattern, corequisite_text)

                if "and" in corequisite_text or "&" in corequisite_text or "," in corequisite_text or "." in corequisite_text:
                    if match:
                        new_data = re.split(r"\s*and\s*|\s*&\s*|\s*,\s*", corequisite_text)
                        codes = []
                        if len(new_data) > 0:
                            for code in new_data:
                                module = {"Code": code.strip()}
                                codes.append(module)
                            corequisite = {"$and": codes}

                elif "or" in corequisite_text or "/" in corequisite_text:
                    if match:
                        new_data = re.split(r"\s*or\s*|\s*/\s*", corequisite_text)
                        codes = []
                        if len(new_data) > 0:
                            for code in new_data:
                                module = {"Code": code.strip()}
                                codes.append(module)
                            corequisite = {"$or": codes}

                else:
                    if match:     
                        corequisite = {"Code": corequisite_text}
                    else:
                        corequisite = {"Comment": corequisite_text}
            item["Corequisite"] = corequisite
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFINAL.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

prerequisite()
corequisite()