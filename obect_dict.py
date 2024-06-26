import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFinal.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        for key in ["Prerequisite", "Corequisite"]:
            if key in item:
                if "$and" in item[key]:
                    for separate in item[key]["$and"]:
                        if "Code" in separate:
                            separate["Code"] = separate["Code"].replace(" ","")

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)