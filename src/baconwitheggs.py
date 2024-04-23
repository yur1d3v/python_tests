"""
1 - receive an integer
2 - know if the number is a multiple of 3 and 5:
    bacon with eggs
3 - know if the number is a multiple of only 3:
    bacon
4 - know if the number is a multiple of only 5:
    eggs
5 - know if the number is NOT a multiple of 3 and 5:
    go hungry
"""

def bacon_with_eggs(n):
    assert isinstance(n, int), 'n should be int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon with eggs'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Eggs'

    return 'Be Hungry'