import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceAssessments.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        for key in ["Assessments"]:
            if key in item:
                if "DP" in item[key]:
                    num_pattern = r"(\d+)"
                    num = re.search(num_pattern, item[key])
                    if num:
                        item["DP"] = int(num.group(0))

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)