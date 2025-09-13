import pint
import sys

ureg = pint.UnitRegistry(cache_folder=":auto:")
Q_ = ureg.Quantity

def main():
    ...


def convert_units(args: list):
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