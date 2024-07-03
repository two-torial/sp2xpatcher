from datetime import datetime, timezone
import sys
import re
import json

regex = re.compile(r"\| ([^|]*) \| ([^|]*) \| ([^|]*) \| \[.*?\]\((.*?)\) \|")

def update_json_file(json_path, dateCode):
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        if isinstance(data, list) and data:
            if "name" not in data[0]:
                data.pop(0)
            
            if data:
                first_entry = data[0]
                gameCode = first_entry.get("gameCode", "")

                lastUpdated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                new_entry = {
                    "gameCode": gameCode,
                    "version": dateCode,
                    "lastUpdated": lastUpdated,
                    "source": 'https://sp2x.two-torial.xyz/',
                }
                data.insert(0, new_entry)

                for entry in data[1:]:
                    if "dateCode" in entry:
                        del entry["dateCode"]

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        
        print(f"'{json_path}' -> \"dateCode\": \"{dateCode}\"")
        return 1
    except Exception as e:
        print(e)
        return 0

def process(file_path, json=''):
    try:
        entries = 0
        count = 0
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                match = regex.search(line)
                if match:
                    json_path = match.group(4).strip()
                    if json == '' or json.replace('\\', '/').replace("./", '') in json_path:
                        variant = match.group(1).strip()
                        dateCode = match.group(3).strip()
                        if "-" in variant:
                            dateCode_with_variant = f"{dateCode} ({variant.split('-')[1]})"
                        else:
                            dateCode_with_variant = dateCode
                        entries += update_json_file(json_path, dateCode_with_variant)
                        count += 1
        return [ entries, count ]
    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")
        return [0, 0] 

if __name__ == "__main__":
    json_path = ''
    len_args = len(sys.argv)
    if len_args in range(2, 3):
        json_path = sys.argv[1]
    else:
        exit("Usage: python makeHeader.py <(optional)json_path>")
        
    entries, count = process("SUPPORTED.md", json_path)
    print(f"\nUpdated {entries} entrie(s) over {count} file(s)")
