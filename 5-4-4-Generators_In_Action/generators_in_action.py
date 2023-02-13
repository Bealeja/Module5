# for loop example

def topten():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()

for i in values:
    print(i)

# OUTPUT
# 1
#
# 4
#
# 9
#
# 16
#
# 25
#
# 36
#
# 49
#
# 64
#
# 81
#
# 100

# You Try!
print(" ")
print("You Try!")


# Look at the even number iterator that you created previously. Now try to make an even number generator that returns
# the first ten even values after 4 (6, 8, 10, 12, 14, 16, 18, 20, 22, 24). Try adding some user input that sets the
# start and stop values for the generator. Add these values as arguments when calling the generator.

def Positive_Generator(start_num, end_num):
    n = start_num
    while n < end_num + 1:
        yield n
        n += 2


values = Positive_Generator(0, 24)

for i in values:
    print(i)
