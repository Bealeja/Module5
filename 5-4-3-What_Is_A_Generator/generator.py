# Using __next__()

def our_generator():
    yield "I "
    yield "exist"
    yield "!"


sentence = our_generator()

print(sentence.__next__(), end='')
print(sentence.__next__(), end='')
print(sentence.__next__(), end='')


# OUTPUT
# I exist!

# Using iter() and next()
def our_generator():
    yield "I "
    yield "exist"
    yield "!"


sentence = our_generator()
a_word = iter(sentence)

print(next(a_word), end='')
print(next(a_word), end='')
print(next(a_word), end='')

# OUTPUT
# I exist!


# Using a for loop
def our_generator():
    yield "I "
    yield "exist"
    yield "!"


for a_word in our_generator():
    print(a_word, end='')
print()

