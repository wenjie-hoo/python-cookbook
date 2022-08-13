def add(x:int, y:int)->int:
    return x + y

'''
>>> help(add)
Help on function add in module __main__:
add(x: int, y: int) -> int
>>>

>>> add.__annotations__
{'y': <class 'int'>, 'return': <class 'int'>, 'x': <class 'int'>}
'''
