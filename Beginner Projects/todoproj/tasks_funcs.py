import questionary
import json


def main():
     print("""
This file provides helper functions related to tasks.
Please import this file into your project to utilize all the functions.
""")

def show_tasks(file):
     with open(file, "r") as f:
            data = json.load(f)
            
            questions = {
                 "type": "select",
                 "message": "which category please?",
                 "choices": [key.capitalize() for key in data.keys()],
                 "name": "category"
            }
            results = questionary.prompt(questions)

            if results["category"].lower() == "todo":
                 task_id = questionary.prompt({
                      "type": "select",
                      "message": "which task please? :)",
                      "choices": [str(item["id"]) for item in data["todo"]],
                      "name": "task_id"
                 })
                 task = get_task_by_id(int(task_id["task_id"]), data)
                 show_task(task)

            elif results["category"].lower() == "completed":
                 task_id = questionary.prompt({
                      "type": "select",
                      "message": "which task please? :)",
                      "choices": [item["id"] for item in data["completed"]]
                 })


def get_task_by_id(id: int, data: dict):
    for section in data.values():
        for task in section:
            if task["id"] == id:
                return task
    return None


def show_task(task):
     print("--------------------------")
     for key, value in task.items():
          print(f"{key}: {value}")
     print("--------------------------")


if __name__ == "__main__":
    main()