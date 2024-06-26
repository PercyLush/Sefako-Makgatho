import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceFinal.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        Assessments = []
        for key in ["Assessments"]:
            if key in item:
                assessments = item[key].split("\n")
                name_pattern = r"([A-z]+)"
                weight_pattern = r"(\d+)"

                for assessment in assessments:
                    new_assessment = {}
                    match_name = re.findall(name_pattern, assessment)
                    match_weight = re.search(weight_pattern, assessment)
                    Text = ""
                    for name in match_name:
                        Text += name
                    if match_weight:
                        new_assessment = {"Name": Text.strip(), "Type": "Coursework", "Weight": int(match_weight.group(0))}
                        Assessments.append(new_assessment)
                    else: 
                        new_assessment = {"Name": Text.strip(), "Type": "Coursework", "Weight": 0}
                        Assessments.append(new_assessment)
        item[key] = Assessments
with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)