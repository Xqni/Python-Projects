import requests


def main():
    print("""
This file is supposed to be imported as a module from a package.
Please import "helpers" package and use that instead.
          """)


def convert(api_key, args: list):
    """
    Convert one currency into another.

    :param api_key: Your own API KEY at https://apiplugin.com/ for Currency Converter.
    :type api_key: str

    The API KEY should be kept inside .env file, see helpers/env.py for file/dir structure.

    :param args: A Python list containing the amount, from, and to values.
    :type args: list

    :raise TypeError: If args[0], the very first element of the list, is not a number.

    :return: A response key's value (text) containing the converted value or an error.
    :rtype: str
    """

    url = f"https://v1.apiplugin.io/v1/currency/{api_key}/convert"

    headers = {'Content-Type': 'application/json'}

    try:
        params = {
            "amount": float(args[0]),
            "from": args[1],
            "to": args[2]
        }
    except Exception as e:
        raise e

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return f"Conversion failed! :("
    
    response = response.json()
    return f"Current rate: {response["text"]}"


if __name__ == "__main__":
    main()