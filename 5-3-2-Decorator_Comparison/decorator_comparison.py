# Try for yourself
# Try to reverse engineer this program so that it results in the same output, but without decorators.
# Compare the two versions. Is the decorated version significantly shorter and simpler?
# Do you think the effort to plan and write a decorator is worthwhile for the end result?
# This program logs the time taken to execute a function:

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Johnny', 20)


# Example
def scream(text):
    return text.upper()


print(scream('Hello!'))

yell = scream

print(yell('Hello'))


def scream(text):
    return text.upper()


def mutter(text):
    return text.lower()


def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(scream)
greet(mutter)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


# Example Function as an argument
def check_upper_case_decorator(func):
    def check_upper_wrapper(*args, **kwargs):
        for c in args[0]:
            if not c.isupper() and not c.isdigit():
                return False
        return func(args[0])

    return check_upper_wrapper


# With Decorator
@check_upper_case_decorator
def reverse_string_01(my_string):
    return "".join(reversed(my_string))


msg_01 = "aa01567ffba3097cc"
print(reverse_string_01(msg_01))
msg_02 = "AA001344CCDFBBFFF"

print(reverse_string_01(msg_02))


# Without Decorator
def reverse_string_02(my_string):
    for c in my_string:
        if not c.isupper() and not c.isdigit():
            return False
        return "".join(reversed(my_string))


print(reverse_string_02(msg_01))
print(reverse_string_02(msg_02))
