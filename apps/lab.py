from time import sleep
# from math import factorial
# from functools import reduce

memory = {}

def my_factorial(n):
    """..."""
    if n in memory:
        return memory[n]
    memory[n] = 1 if n == 1 else n * my_factorial(n-1)
    return memory[n]

# def infinite():
#     n = 0
#     while True:
#         yield n ** 2
#         n += 1

def infinite_fib():
    a,b = 1,1
    while True:
        yield a+b
        a,b = b,a+b

# from typing import Any, Callable, Union

# TFunc = Callable[..., Any]

# def my_validator(message: str = None) -> Callable[[TFunc], TFunc]:
#     """..."""
#     def wrapper(func: TFunc) -> TFunc:
#         nonlocal message
#         message = f"an error has occurred in the method: {func.__name__} check it." \
#                     if not message else message
#         def inner(*args: Any, **kwargs: Any) -> Union[TFunc, Exception]:
#             if not func(*args, **kwargs):
#                 raise Exception(message)
#             return func(*args, **kwargs)
#         return inner
#     return wrapper

# @my_validator("un error el numero no puede ser negativo.")
# def is_not_negative(n):
#     print("dentro de la función del número no negativo")
#     return n > 0

# @my_validator("the ")
# def max_len(s, ml):
#     print("dentro de la función del maxima longitud")
#     return len(s) < ml

if __name__ == '__main__':

    # is_not_negative(-10)

    # max_len("hola", 2)

    # print(my_factorial(10))
    # print(memory)

    # a = 1
    # l = [a := a*i for i in range(1, 11)]
    # print(l)

    # print(reduce(lambda x,y: x*y, range(1,10)))
    it = infinite_fib()
    while True:
        sleep(1)
        print(next(it))
    