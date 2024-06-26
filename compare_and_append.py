import json

path1 = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFinal.json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\SCI_Credits_Duration.json"

with open(path1, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

    for item1 in data1:
        if "Code" in item1:
            for item2 in data2:
                if "Code" in item2:
                    if item1["Code"] == item2["Code"]:
                        for key in ["Credit", "Duration","Period"]:
                            if key in item2:
                                item1[key] = item2.get(key)

                    else:
                        pass

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFinal.json", "w", encoding="utf-8") as file:
    json.dump(data1, file, indent=2)