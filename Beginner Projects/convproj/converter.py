import argparse
import helpers
import helpers.env as env
import helpers.validators as val
import re
import sys
import questionary

"""Main Converter program."""


def main(args):
    """
    If the user opts for flag based functionality then direct the user input into correct handler functions.

    :param args: An argparse namespace.
    :type args: argparse.Namespace object.

    There is a regex pattern defined to ensure that the user input is of correct format before proceeding, should the user choose argparse route.

    REGEX PATTERN EXPLAINED: ^\\d+.?(\\d+)?(?:\\s[a-zA-Z]{3}){2}$
    ^\\d+ - checks for atleast one digit at the start, but accepts more.
    .? - checks for zero or one space
    (?:\\d+)? - non-recording group, checks for one or more digits. ? at the end indicates the whole group is opitional
    (?:\\s[a-zA-Z]{3}){2}$ - non-recording group, checks for following patterns.
    \\s - checks for only one space character
    [a-zA-Z] - checks for letters in both cases.
    {3} - checks the previous pattern exactly three times in a row.
    {2} - checks the whole previous pattern exactly two times in a row.
    $ - marks the end of the string.

    The argparse route is for users who are comfortable using CLI, flags, and typing long commands.
    Use can run argparse mode by running "python -m convproj.converter -c 1 usd cad".
    1, usd, and cad can be replaced by values/currencies of your choice.

    I have also taken less comfortable users into account by implementing an interactice questions-answer based version.

    The implementation of interactive version is done using questionary package which is available at https://pypi.org/project/questionary/
    Although the tool is pretty simple yet powerful, my implementation only makes use of select and text type questions.
    I have, however, inserted a validation class which ensures, should the user use this route, users must enter values for each question before proceeding.

    Use can run interactive mode by simply running "python -m convproj.converter".
    """
    if args.currency:
        p = r"^\d+.?(?:\d+)?(?:\s[a-zA-Z]{3}){2}$"
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
