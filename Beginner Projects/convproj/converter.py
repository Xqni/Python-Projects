import argparse
import helpers
import helpers.env as env
import re
import sys


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
    main(args)