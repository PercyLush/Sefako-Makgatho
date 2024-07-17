import re
import json

def extract_key_value_pairs(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    keys_of_interest = ["Name", "Code", "Description", "Assessment"]

    extracted_data_list = []

    pattern = re.compile(r'(\w+):\s*((?:.*(?:\n(?!\w+:).*)*))\n')

    matches = pattern.findall(content)

    current_course_data = {}

    for match in matches:
        key, value = match
        if key in keys_of_interest:
            if key == "Name":
                current_course_data[key] = value.strip()

            if key == "Code":
                current_course_data[key] = value.strip()

            if key == "Description":
                current_course_data[key] = value.strip()

            if key == "Assessment":
                current_course_data[key] = value.strip()

        if key == "Assessment":
            extracted_data_list.append(current_course_data)
            current_course_data = {}  # Reset for the next course

    return extracted_data_list

file_path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptionsFinal.txt"

result_list = extract_key_value_pairs(file_path)

json_file_path = "C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptions.json"

with open(json_file_path, 'w') as json_file:
    json.dump(result_list, json_file, indent=2)

print(f"Data has been successfully stored in {json_file_path}")
