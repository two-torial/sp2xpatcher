import os
import re
import json
import subprocess
import sys
from datetime import datetime, timezone
from copy import deepcopy

# Regular expression pattern to match the lines in SUPPORTED.md
regex = re.compile(r"\| ([^|]*) \| ([^|]*) \| ([^|]*) \| \[.*?\]\((.*?)\) \|")

# Get a list of files for a given git command
def git_files(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    files = result.stdout.decode('utf-8').splitlines()
    return [file for file in files if file.endswith('.json')]

# Get a list of changes json files using git
def get_changed_jsons():
    commands = [
        ['git', 'diff', '--name-only'], # changed files
        ['git', 'diff', '--cached', '--name-only'], # staged files
        ['git', 'log', 'origin/main..HEAD', '--name-only', '--pretty=format:'] # comitted files
    ]
    changed_files = set()
    for command in commands:
        changed_files.update(git_files(command))
    return list(changed_files)

# Update header for a given json file
def update_header(json_path, date_code):
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        if isinstance(data, list) and data:
            if "name" not in data[0]:
                data.pop(0)

            if data:
                first_entry = data[0]
                game_code = first_entry.get("gameCode", "")
                last_updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                new_entry = {
                    "gameCode": game_code,
                    "version": date_code,
                    "lastUpdated": last_updated,
                    "source": 'https://sp2x.two-torial.xyz/',
                }
                data.insert(0, new_entry)

                for entry in data[1:]:
                    entry.pop("dateCode", None)

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"'{os.path.relpath(json_path, 'patches/')}' - Updated header")
    except Exception as e:
        exit(e)

# Cleanup all json files by batch-running jobs 
def clean_json_files():
    json_files = []
    for filename in os.listdir("patches/"):
        if filename.endswith('.json'):
            filepath = os.path.join("patches/", filename)
            with open(filepath, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)

            # Remove redundance union entries
            new_json_data = deepcopy(json_data)
            for item in new_json_data:
                if "type" in item:
                    if item["type"] == "union":
                        for patch in item["patches"]:
                            if "type" in patch:
                                del patch["type"]

            if json_data != new_json_data:
                # Only save changes and print if something was done
                with open(filepath, "w", encoding="utf-8") as json_file:
                    json.dump(new_json_data, json_file, indent=4)
                print(f"'{filename}' - Cleaned up")
                json_files.append(filepath)
    return json_files

# Run checks for json_files if specified, otherwise all changes files
def check(json_files=None):
    # if json_files is none: run clean_json_files and set json_files to its return value
    json_files = json_files or clean_json_files()
    # if there are still no json files, get changed jsons instead
    if not json_files:
        json_files = get_changed_jsons()
        # exit if there's no changed files
        if not json_files:
            exit("Nothing to do")

    count = 0
    try:
        # Open SUPPORTED.md
        with open("SUPPORTED.md", "r", encoding="utf-8") as file:
            # For each line
            for line in file:
                match = regex.search(line)
                # If it matches a game info line 
                if match:
                    # Get the last group of the regex (json path) 
                    json_path = match.group(4).strip()
                    # For each path in json_files check if it matches the current line's json path
                    if any(j_path in json_path for j_path in json_files):
                        # if that's the case update its header and add 1 to count
                        variant = match.group(1).strip()
                        date_code = match.group(3).strip()
                        # Add variant (ex 010) to datecode if present, otherwise keep datecode as is
                        if "-" in variant:
                            date_code = f"{date_code} ({variant.split('-')[1]})" 
                        update_header(json_path, date_code)
                        count += 1

        # If nothing was done, exit early
        if count == 0:
            exit("Nothing to do")
        return count
    except Exception as e:
        exit(f"Error processing files: {e}")

if __name__ == "__main__":
    if not os.path.exists('./SUPPORTED.md'):
        exit("File 'SUPPORTED.md' not found")

    if not os.path.exists('patches/'):
        exit("Folder 'patches' not found")

    len_args = len(sys.argv)
    if len_args == 1:
        count = check()
    elif len_args == 2:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            exit(f"Invalid path '{filepath}'")
        count = check([filepath])
    else:
        exit("Usage: python checks.py <(optional)json_name>")

    print(f"\nUpdated {count} file(s)")