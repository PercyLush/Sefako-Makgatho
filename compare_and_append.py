import json

path1 = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceDescriptions.json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceAssessments.json"

with open(path1, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

    for item1 in data1:
        if "Code" in item1:
            for item2 in data2:
                if "Code" in item2:
                    if item1["Code"] == item2["Code"]:
                        if "Prerequisite" in item2:
                            item1["Prerequisite"] = item2.get("Prerequisite")

                        if "Corequisite" in item2:
                            item1["Corequisite"] = item2.get("Corequisite")

                        if "Assessments" in item2:
                            item1["Assessments"] = item2.get("Assessments")
                    else:
                        pass

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\Testing.json", "w", encoding="utf-8") as file:
    json.dump(data1, file, indent=2)