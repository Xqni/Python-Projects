import argparse
import helpers
import helpers.env as env
import helpers.validators as val
import re
import sys
import questionary


def main(args):
    if args.currency:
        p = r"^\d+.?(\d+)?(?:\s[a-zA-Z]{3}){2}$"
        s = " ".join(args.currency)
        if not re.match(p, s):
            sys.exit("usage: 1 currency1 currency2")
        handle_currency(args.currency)
    
    elif args.unit:
        handle_units(args.unit)


def handle_currency(money):
    response = helpers.currency.convert(env.get("API_KEY"), args=money)
    print(response)


def handle_units(values):
    result = helpers.units.convert_units(values)
    print(result)


if __name__ == "__main__":
    # initialize parser
    parser = argparse.ArgumentParser()

    # Add different flags
    parser.add_argument("-c", "--currency", 
                        nargs="*", 
                        help="usage: 1 USD CAD")
    parser.add_argument("-u", "--unit", 
                        nargs="*", 
                        help="usage: 1 cm ft")

    # get the list of arguments passed
    args = parser.parse_args()

    if len(sys.argv) > 1:
        main(args)
    elif len(sys.argv) == 1:
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
                    "validate": val.valueValidator,
                },
                {
                    "type": "text",
                    "name": "from",
                    "message": "From:",
                    "validate": val.valueValidator,
                },
                {
                    "type": "text",
                    "name": "to",
                    "message": "To:",
                    "validate": val.valueValidator,
                },
            ]

            results = questionary.prompt(c_prompt)
            handle_currency(list(results.values()))

        elif results["type"] == "Units":
            u_prompt = [
                {
                    "type": "text",
                    "name": "value",
                    "message": "value:",
                    "validate": val.valueValidator,
                },
                {
                    "type": "text",
                    "name": "from",
                    "message": "From:",
                    "validate": val.valueValidator,
                },
                {
                    "type": "text",
                    "name": "to",
                    "message": "To:",
                    "validate": val.valueValidator,
                },
            ]
            results = questionary.prompt(u_prompt)
            handle_units(list(results.values()))