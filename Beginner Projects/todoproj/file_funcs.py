from datetime import datetime
import json
from pathlib import Path


def main():
    print("""
This file provides helper functions related to I/O operations for files.
Please import this file into your project to utilize all the functions.
""")


def read_data(file):
    with open(f"./todoproj/{file}", "r") as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            create_file(file)
            return json.load(f)


def write_data(file, data):
    with open(f"./todoproj/{file}", "w") as f:
        f.write(json.dumps(data, indent=4))


def write_tasks(file, task):
    try:
        if not read_data(file):
            create_file(file)

        data = read_data(file)

        todo_tasks = data["todo"]
        all_ids = [item["id"] for section in data.values() for item in section]

        if not todo_tasks:
            obj = {
                "id": 1,
                "task": task["task"],
                "date": datetime.today().strftime("%Y-%m-%d"),
                "status": "todo"
            }
        else:
            obj = {
                "id": max(all_ids) + 1,
                "task": task["task"],
                "date": datetime.today().strftime("%Y-%m-%d"),
                "status": "todo"
            }

        data["todo"].append(obj)

        write_data(file, data)
        print(f"Task added! :) (id: {obj["id"]})")

    except Exception as e:
        print(e)


def check_file_exists(file):
    path = Path(f"./todoproj/{file}")
    return path.exists()


def create_file(file):
    with open(f"./todoproj/{file}", "w") as f:
        struct = {
            "todo": [],
            "completed": []
        }
        f.write(json.dumps(struct, indent=4))


if __name__ == "__main__":
    main()
