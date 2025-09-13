from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

length = 10 * ureg.meter
my_speed = Q_(20, 'm/s')
print(length)
print(my_speed)