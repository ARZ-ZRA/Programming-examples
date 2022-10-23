# Напишите функцию, которая будет принимать число и
# возвращать его дробную часть (если она есть).
from decimal import Decimal
def decimal_part(n):
    n = str(abs(n))
    return float(Decimal(n) % 1)

def fractional_1(num):
    if type(num) == int:
        return 0
    return f"0.{str(num).split('.')[-1]}"

print(fractional_1(4.3333))
print(decimal_part(3))