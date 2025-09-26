import questionary

from .file_funcs import write_tasks, check_file_exists, create_file
from .tasks_funcs import show_task, get_task_by_id, show_tasks

def main():
    questions = [
        {
            "type": "select",
            "message": "What would you like to add to the list? :)",
            "choices": ["Add task", "Complete a task", "View a task"],
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
        print(check_file_exists("tasks.json"))
        if not check_file_exists("tasks.json"):
             create_file("tasks.json")
        write_tasks(questionary.prompt(task_question))
    
    elif results["choice"] == "View a task":
         show_tasks("tasks.json")


if __name__ == "__main__":
    main()