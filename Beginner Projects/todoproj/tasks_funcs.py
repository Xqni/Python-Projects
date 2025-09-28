import questionary
from inspect import stack

from .file_funcs import read_data, write_data, create_file


def main():
    print("""
This file provides helper functions related to tasks.
Please import this file into your project to utilize all the functions.
""")


def show_tasks(file):
    data = read_data(file)

    if not data:
        create_file(file)

    data = read_data(file)
    questions = {
        "type": "select",
        "message": "which category please?",
        "choices": [key.capitalize() for key in data.keys()],
        "name": "category"
    }

    results = questionary.prompt(questions)

    try:
        task_id = get_task_id(data, results["category"].lower())

        task = get_task_by_id(int(task_id["task_id"]), data)

        if stack()[1].function == "main":
            show_task(task)
        elif stack()[1].function == "mark_task":
            task = change_status(task)
            if results["category"].lower() == "todo":
                data["completed"].append(task)
            else:
                data["todo"].append(task)
            try:
                n_data = remove_task(data, task)
                write_data(file, n_data)
                print(f"Changed task!")
            except Exception as e:
                print(e)
    except (ValueError, UnboundLocalError):
        print("\nNo tasks to show, please see the other category!\n")


def remove_task(data, task):
    for key, value in data.items():
        for index, item in enumerate(value):
            if item["id"] == task["id"] and item["status"] != task["status"]:
                value.pop(index)
                return data


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


def change_status(task):
    match task["status"]:
        case "todo":
            task["status"] = "completed"
        case "completed":
            task["status"] = "todo"
        case _:
            return task
    return task


def mark_task(file):
    show_tasks(file)


def get_task_id(data, category):
    return questionary.prompt({
        "type": "select",
                "message": "which task please? :)",
                "choices": [str(item["id"]) for item in data[category]],
                "name": "task_id"
    })


if __name__ == "__main__":
    main()
