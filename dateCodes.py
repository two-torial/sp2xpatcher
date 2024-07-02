import re
import json

# Matches SUPPORTED.md lines with game information on them, splitting the needed data into groups
regex = re.compile(r"\| ([^|]*) \| ([^|]*) \| ([^|]*) \| \[.*?\]\((.*?)\) \|")

# Updates every entry in a json file with the dateCode
def update_json_file(json_path, dateCode):
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        entries = 0
        if isinstance(data, list):
            for entry in data:
                if "gameCode" in entry:
                    new_entry = {}
                    for key, value in entry.items():
                        new_entry[key] = value
                        if key == "gameCode":
                            new_entry["dateCode"] = dateCode
                    entry.clear()
                    entry.update(new_entry)
                    entries += 1
        
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"'{json_path}' -> \"dateCode\": \"{dateCode}\"")
        return entries
    except Exception as e:
        print(e)

# Main function iterating through SUPPORTED.md, finding relevant lines, processing json files for each game version
def iterate(file_path):
    try:
        entries = 0
        count = 0
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                match = regex.search(line)
                if match:
                    variant = match.group(1).strip()
                    dateCode = match.group(3).strip()
                    if "-" in variant:
                        dateCode_with_variant = f"{dateCode} ({variant.split("-")[1]})"
                    else:
                        dateCode_with_variant = dateCode
                    json_path = match.group(4).strip()
                    entries += update_json_file(json_path, dateCode_with_variant)
                    count += 1
        return [ entries, count ]
    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")


entries, count = iterate("SUPPORTED.md")
print(f"\nUpdated {entries} entries over {count} files.")