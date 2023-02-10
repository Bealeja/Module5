# Wrapper Layout
def my_decorator_function(func):
    def my_wrapper_function(*args):
        print('This is the name of the function: ', func.__name__)
        print('This is the output of the function: ')
        func()
        print('This is the end of the wrapper function \n')

    return my_wrapper_function


@my_decorator_function
def greetings():
    print('my name is Jack')


@my_decorator_function
def age():
    print('my age is 25')


@my_decorator_function
def funfact():
    print('I like BJJ and hope to compete soon when I get my blue belt')


@my_decorator_function
def randomnoise():
    print('rraaaaawr xD')


greetings()
age()
funfact()
randomnoise()
