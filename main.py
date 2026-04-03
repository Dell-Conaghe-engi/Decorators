'''модуль для декоратора'''
import numbers


def add_numbers(numbers):
    return sum(numbers)

a=add_numbers(range(1,11))
print(a)

import time


def check_time(func):
    def wrapper(*args, **kwargs):
        """наш декоратор - подсчет выполнения скорости работы"""
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"функция {func} отработала за {end - start:.4f} секунд")

        return

    return wrapper

@check_time
def lazy_func():
    print("я ленивый , капец")
    time.sleep(1)
    print("наконец-то я поднялся с кровати")


lazy_func()






























