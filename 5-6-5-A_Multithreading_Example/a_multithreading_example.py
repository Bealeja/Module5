import threading
from time import sleep
import os
from random import *
from threading import *


# Before Threading
def test_01(msg):
    print("test01: ", msg)


def test_02(msg):
    print("test02: ", msg)


msg = "Something"
test_01(msg)
msg = "Anything"
test_02(msg)


# OUTPUT
# test01: Something
#
# test02: Anything

# Example 2: Threading

def test_01(msg):
    print("test01: ", msg)


def test_02(msg):
    print("test02: ", msg)


msg = "In THREAD Something"
t1 = threading.Thread(target=test_01, args=[msg])
msg = "In THREAD Anything"
t2 = threading.Thread(target=test_02, args=[msg])

t1.start()
t2.start()

t1.join()
t2.join()


# OUTPUT
# test01: In THREAD Something
#
# test02: In THREAD Anything

# Example: Not designating which thread should finish first In this case, you have two functions that each print text
# in a loop. Notice that the output doesn’t follow the calling order. Instead, they are scheduled and keep running
# until they are finished, with no guaranteed order of execution. From an end-user perspective, the output could
# appear to arrive in random order.
#
# Note that join() also doesn’t guarantee any order of execution. You can comment it out and you will see that the
# output will still be mixed. The program alternates between a little bit of t3 and then a little bit of t4 until the
# functions are complete. The more threads you have running in concurrence, the more chaotic the program can become.

def test_03():
    for i in range(50):
        print("Function test_03 ################################")


def test_04():
    for i in range(50):
        print("Function test_04 --------------------------------")


t3 = threading.Thread(target=test_03, args=[])
t4 = threading.Thread(target=test_04, args=[])

t3.start()
t4.start()

t3.join()
t4.join()


# Try for yourself
# For the previous example, add some lines of code to control the threads:
#
# At the beginning of the program, add: from time import sleep Insert a sleep() statement into both for loops. Set
# different timings for each. For example, you could set a one-second pause for test_03() and a two-second pause for
# test_04(). Run the program and see how the output differs from before. Run it again. How similar is the output this
# time? Try altering the timings and the loop values to see what patterns you can create.

def test_03():
    for i in range(50):
        sleep(1)
        print("Function test_03 ################################")


def test_04():
    for i in range(50):
        sleep(2)
        print("Function test_04 --------------------------------")


t3 = threading.Thread(target=test_03, args=[])
t4 = threading.Thread(target=test_04, args=[])

t3.start()
t4.start()

t3.join()
t4.join()


# Example: Thread IDs

# In this example, the join() methods immediately follow their respective start() methods. This is to prevent the
# threads from overlapping and to keep the output consistent. Therefore, this is technically not a multithreading
# example, because the threads execute and complete sequentially.
#
# Note that the threads share the same PID. This is a randomly generated number from your operating system. Try
# running the program again and see how the number changes. You will learn more about processes later in this unit.
#
# You can use the setName() method to change the name of a thread. This helps to make your code more readable when
# your program contains many threads.
def test_05():
    print("PID: ", os.getpid())


t5 = threading.Thread(target=test_05, args=[])
t5.start()
t5.join()
t6 = threading.Thread(target=test_05, args=[])
t6.start()
t6.join()

print("Name: ", t5.name)
print("Name: ", t6.name)
t6.setName("Our Thread")
print(t6.name)


# Final Example
# Here we have another example with three functions:
#
# read_list() prints a list.
# insert_into_list() inserts random integers from 0 to 100 at random indexes of the list.
# delete_from_list() deletes items at random indexes.
# If you run the program a few times, you will get very different results.

def read_list(x_list):
    for i in range(len(x_list)):
        print(i, end=' ')
    print()


def insert_into_list(x_list):
    for i in range(len(x_list)):
        x_list.insert(randint(0, 100), randint(0, len(x_list) - 1))


def delete_from_list(x_list):
    for i in range(len(x_list)):
        n = randint(0, 1)
        if n == 1:
            x_list.pop(randint(0, len(x_list) - 1))


our_list = [1, 2, 5, 7, 1, 9]

t7 = threading.Thread(target=read_list, args=[our_list])
t8 = threading.Thread(target=insert_into_list, args=[our_list])
t9 = threading.Thread(target=delete_from_list, args=[our_list])

t7.start()
t8.start()
t9.start()

for k in range(100):
    threading.Thread(target=read_list, args=[our_list]).start()
    threading.Thread(target=insert_into_list, args=[our_list]).start()
    threading.Thread(target=delete_from_list, args=[our_list]).start()


# Remember, this program is more or less simultaneously reading, inserting, and deleting items from the list.
#
# You do not need to store threads in a variable, such as:
#
# t1 = threading.Thread(target=test_01, args=[msg]) You can also just create and call the thread in one line,
# as you can see at the end of the previous example. However, it’s generally a good idea to be able to access the
# thread with a variable, so you can use it repeatedly without needing to type out the full thread and arguments.


# Try for yourself
# You have now learnt how to run functions in a thread. How about running class methods?
#
# Here is a template to get you started:


class Blue(Thread):
    def run(self):
        for i in range(5):
            print('blue')
            sleep(1)


class Yellow(Thread):
    def run(self):
        for i in range(5):
            print('yellow')
            sleep(1)


t1 = Blue()
t2 = Yellow()

t1.start()
sleep(0.5)
t2.start()
sleep(0.2)

t1.join()
t2.join()

print('green')
