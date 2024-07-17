# import re

# path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptions.txt"

# with open(path, "r", encoding="utf-8") as file1:
#     data = file1.read()

#     for i in range(124, 141):
#         pattern = f"{i}"

#         data = re.sub(pattern, r"", data)
# with open(path, "w", encoding="utf-8") as file2:
#     file2.write(data)
import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineFinal.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Description" not in item:
            item["Description"] = "TO BE UPDATED"

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)

