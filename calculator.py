def sum(x, y):
    assert isinstance(x, (int, float)), 'X need to be int or float'
    assert isinstance(x, (int,float)), 'Y need to be int or float'
    return x + y

def subtract(x, y):
    assert isinstance(x, (int, float)), 'X need to be int or float'
    assert isinstance(y, (int,float)), 'Y need to be int or float'
    return x - y