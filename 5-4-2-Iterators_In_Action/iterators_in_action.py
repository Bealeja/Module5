# Example 1
our_string = 'A long piece of text.'
our_iterator_object = iter(our_string)

while True:
    try:
        i = next(our_iterator_object)
        print(i, end=' ')
    except StopIteration:
        print()
        break

# Output
# A  l o n g  p i e c e  o f  t e x t .

