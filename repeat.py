'''модуль с декоратором повторов позволяет выполнить функцию Н-ое количество раз'''
import functools

def repeat_decorator(times=2):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result=None
            for i in range(times):
                result=func(*args, **kwargs)
            return result
        return wrapper
    return decorator
