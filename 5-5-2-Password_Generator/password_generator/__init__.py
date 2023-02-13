# Example Password Generator
import inspect
import random
from random import randint


def password_generator_01(max_length, allowed_chars, seed=None):
    if max_length < 10:
        raise Exception("Password cannot be shorter then 10")
    if seed:
        random.seed(seed)
    length = int(randint(int(max_length - (max_length * 0.1)), max_length))
    passwd = ''
    for i in range(length):
        passwd += allowed_chars[randint(0, len(allowed_chars) - 1)]
    return passwd


max_characters = 15
character_selection = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+{}|>?<[];'\,./~`><"
password = password_generator_01(max_characters, character_selection)
print("Password: ", password)
print(" ")

# Using Annotations
print("Using Annotations:")


def password_generator_01(max_length: 'int', allowed_chars: 'str', seed=None) -> 'str':
    if max_length < 10:
        raise Exception("Password cannot be shorter then 10")
    if seed:
        random.seed(seed)
    length = int(randint(int(max_length - (max_length * 0.1)), max_length))
    passwd = ''
    for i in range(length):
        passwd += allowed_chars[randint(0, len(allowed_chars) - 1)]
    return passwd


print(password_generator_01.__annotations__)

# Get more information about the program
print(inspect.getfullargspec(password_generator_01))
