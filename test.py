import questionary


questions = [
  {
    "type": "select",
    "name": "type",
    "message": "What would you like to convert today? :)",
    "choices": ["Currency", "Units"],
  }
]

results = questionary.prompt(questions)

if results["type"] == "Currency":
    c_prompt = [
        {
            "type": "text",
            "name": "amount",
            "message": "Amount:",
        },
        {
            "type": "text",
            "name": "from",
            "message": "From:",
        },
        {
            "type": "text",
            "name": "to",
            "message": "To:",
        },
    ]

elif results["type"] == "Units":
    u_prompt = [
        {
            "type": "text",
            "name": "value",
            "message": "value:",
        },
        {
            "type": "text",
            "name": "from",
            "message": "From:",
        },
        {
            "type": "text",
            "name": "to",
            "message": "To:",
        },
    ]

    results = questionary.prompt(u_prompt)
    print(results)