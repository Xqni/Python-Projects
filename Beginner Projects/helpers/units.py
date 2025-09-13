import pint

"""Standard initialization"""
ureg = pint.UnitRegistry(cache_folder=":auto:")
Q_ = ureg.Quantity

def main():
    print("""
This file is supposed to be imported as a module from a package.
Please import "helpers" package and use that instead.
          """)


def convert_units(args: list):
    """
    Converts one unit of measurement to another.

    :param args: A Python list contaning quantity, from, and to untis.
    :type args: list

    Since this function is implemented using pint package, it can handle pretty complex converions inluding but not limited to angles/angluar frequencies, logarithmic untis, and different quanitity measurements such as m**2/s to cm**2/s, etc.

    This package is pretty good and powerful, I would suggest checking out the official documentation for more exmaples and things you can do it at the following URL: https://pint.readthedocs.io/en/stable/index.html

    :return: The converted value or an error.
    :rtype: str

    """

    try:
        unit1 = Q_(float(args[0]), args[1])
        unit2 = args[2]
        result = unit1.to(unit2)
        return f"{result:.6f~P}"
    except IndexError:
        return f"usage: value unit1 unit2"
    except pint.errors.DimensionalityError as e:
        return f"{e}"


if __name__ == "__main__":
    main()