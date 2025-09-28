import questionary

from .file_funcs import write_tasks, check_file_exists, create_file
from .tasks_funcs import show_tasks, mark_task


def main():
    try:
        questions = [
            {
                "type": "select",
                "message": "What would you like to add to the list? :)",
                "choices": ["Add task", "Change status", "View a task"],
                "name": "choice"
            },
        ]

        results = questionary.prompt(questions)

        if results["choice"] == "Add task":
            task_question = {
                "type": "text",
                "message": "What would you like to add today? :)\n",
                "name": "task"
            }
            if not check_file_exists("tasks.json"):
                create_file("tasks.json")
            write_tasks("tasks.json", questionary.prompt(task_question))

        elif results["choice"] == "View a task":
            show_tasks("tasks.json")
        else:
            mark_task("tasks.json")

    except KeyError as e:
        print(e)
    except Exception as e:
        raise (e)


if __name__ == "__main__":
    main()
