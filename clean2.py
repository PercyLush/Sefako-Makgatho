import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineFinal.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        item["Institution"] = "Sefako Makgatho Health Sciences University"
        

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)