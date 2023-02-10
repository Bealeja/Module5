# Example 1
our_list = ["First item", "Second item", "Third item"]

for i in our_list:
    print(i, end=' | ')
print()

# OUTPUT
# First item | Second item | Third item |

# Example 2
our_list = ["First item", "Second item", "Third item"]
list_length = len(our_list)
i = 0

while i != list_length:
    print(our_list[i], end=' | ')
    i += 1
print()

# OUTPUT
# First item | Second item | Third item |

# Try for yourself
# Let’s refresh your memory about iterable variables and data structures.
#
# Use the previous for loop list example.
# Change the contents of our_list to another data type. Try all of these data types:
# String
# Set
# Integer
# Tuple
# Take note of which versions give a result and which versions return errors.

print('\n YOU TRY!')

String_Input = "First item"
Set_Input = {"First item", "Second item", "Third item"}
Interger_Input = [1, 2, 3]
Tuple_Input = (1, 2, "hello", 4)

print('\n This is a string input')
for i in String_Input:
    print(i, end=' | ')
print()

# Output
# F | i | r | s | t |   | i | t | e | m |

print('\n This is a set input')
for j in Set_Input:
    print(j, end=' | ')
print()

# Output
# First item | Third item | Second item |

print('\n This is a interger input')
for k in Interger_Input:
    print(k, end=' | ')
print()

# Output
# 1 | 2 | 3 |

print('\n This is a Tuple input')
for l in Tuple_Input:
    print(l, end=' | ')
print()

# Output
# 1 | 2 | hello | 4 |