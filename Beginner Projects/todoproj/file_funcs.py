from datetime import datetime
import json
from pathlib import Path

import helpers.validators as val


def main():
     print("""
This file provides helper functions related to I/O operations for files.
Please import this file into your project to utilize all the functions.
""")


def write_tasks(task):
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            print("loaded the data", data)
            todo_tasks = data["todo"]
            print("loaded the todo tasks", todo_tasks)
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
        print("appended to the todo list", data)
        with open("tasks.json", "w") as f:
            f.write(json.dumps(data, indent=4))
            print(f"Task added! :) (id: {obj["id"]})")

    except Exception as e:
        print(e)


def check_file_exists(file):
    path = Path(f"./todoproj/{file}")
    return path.exists()
     

def create_file(file):
     with open(file, "w") as f:
          struct = {
               "todo": [],
               "completed": []
          }
          f.write(json.dumps(struct, indent=4))


if __name__ == "__main__":
    main()