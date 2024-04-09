# https://docs.python.org/3/library/doctest.html
# https://docs.python.org/3/library/unittest.html
from calculator import soma

# print(soma(10,20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))

try:
    print(soma('15', 15))
except AssertionError as e:
    print(f"Conta Inválida: {e}")

print('Conta:', soma(25,25))