import helpers.validators as val
import json
from pathlib import Path
import questionary

def main():
    questions = [
        {
            "type": "select",
            "message": "What would you like to track today? :)",
            "choices": ["Income", "Expense", "Summary"],
            "name": "name"
        },
    ]
    results = questionary.prompt(questions)
    tracker(results)


def tracker(results):
    print(results)
    if results["name"] == "Income":
        tracker_income()

def tracker_income():
    questions = [
        {
            "type": "text",
            "message": "Which income would you like to report?",
            "name": "income",
            "validate": val.valueValidator,
        },
        {
            "type": "text",
            "message": "What amount did you earn?",
            "name": "amount",
            "validate": val.valueValidator,
        },
        {
            "type": "text",
            "message": "What month is this for?",
            "name": "month",
            "validate": val.valueValidator,
        },
    ]
    income = questionary.prompt(questions)
    try:
        amount = float(income["amount"])
    except Exception as e:
        print(e)

    write_file(income, amount)


def write_file(data, amount):
    obj = {
        data["month"]: {
            data["income"]: amount
        }
    }

    if check_file_exists("data.json"):
        with open("./exproj/data.json") as f:
            file_data = json.load(f)
            
            if data["month"] in file_data.keys():
                if data["income"] in file_data[data["month"]].keys():
                    print(json.dumps(file_data[data["month"]][data["income"]], indent=4))


def check_file_exists(file):
    path = Path(f"./exproj/{file}")
    return path.exists()


if __name__ == "__main__":
    main()