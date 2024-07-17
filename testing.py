import re
import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\OralHealthFINALs.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Institution" not in item:
            
            item["Institution"] = "Sefako Makgatho Health Sciences University"

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)

