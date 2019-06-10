
import functools


def my_decorator(func):
    # decorator without args
    @functools.wraps(func)
    def function_that_runs_func():
        print("in the decor")
        func()
        print("after the decor")
    return function_that_runs_func


@my_decorator
def my_func():
    print("i am the func")


def decor_with_args(num):
    # decor with args
    def my_decor(func):
        @functools.wraps(func)
        def function_runs_func(*args, **kwargs):
            print("in the decor")
            func()
            print("after the decor")
        return function_runs_func
    return my_decor


@decor_with_args(65)
def my_function():
    print("hello")

my_function()





