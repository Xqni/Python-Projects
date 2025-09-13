import pint
import sys

ureg = pint.UnitRegistry(cache_folder=":auto:")
Q_ = ureg.Quantity

def main():
    ...


def convert_units():
    args = sys.argv

    unit1 = Q_(float(args[1]), args[2])
    unit2 = args[3]
    result = unit1.to(unit2)
    print(f"{result:.2f~P}")


if __name__ == "__main__":
    convert_units()