# In a 2019 article introducing meta-programming (which includes decorators and meta -classes), Saurabh Kukade,
# a lead software engineer at Nitor Infotech, used the following example to demonstrate how decorators can make
# programmers’ lives a lot easier.
#
# Take a look at the following code from Kukade. Each function performs an arithmetic operation on two variables. Now
# you would like the program to:
#
# display which function was called display what parameters were given for the function. But you also want to keep
# your code clean and simple. Open up a new PyCharm project and see if you can add the new feature using decorators
# to avoid having to modify each function with repeated code, like you saw done in the video.

# Initial

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


# Final

def my_decorator(func):
    def wrapper_function(*args):
        print("{0} is called with parameters {1}".format(func.__name__, args))
        return func(*args)

    return wrapper_function


@my_decorator
def add(x, y):
    return x + y


@my_decorator
def sub(x, y):
    return x - y


@my_decorator
def mul(x, y):
    return x * y


# OUTPUTS
my_decorator(add(5, 1))
my_decorator(sub(6, 2))
my_decorator(mul(7, 3))
