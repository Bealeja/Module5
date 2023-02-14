import multiprocessing
import os

def test_01():
    print("Function:", test_01.__name__, " PID:", os.getpid(), end=' ')


def test_02():
    print("Function:", test_02.__name__, " PID:", os.getpid(), end=' ')


def test_03():
    print("Function:", test_03.__name__, " PID:", os.getpid(), end=' ')


if __name__ == '__main__':
    processes = [multiprocessing.Process(target=test_01, args=[]),
                 multiprocessing.Process(target=test_02, args=[]),
                 multiprocessing.Process(target=test_03, args=[])]

    for p in processes:
        p.start()
        p.join()
        print(p.name)
print(" ")


# OUTPUT
# Function: test_01 PID: 13248 Process-1
#
# Function: test_02 PID: 13249 Process-2
#
# Function: test_03 PID: 13250 Process-3

# As you can see, the basic program structure is similar to how threading works:
#
# Import the relevant library.
# Define functions.
# Create processes/threads and define which functions they call.
# Start the processes/threads.
# The key thing to remember about processes is that they have their own memory space. Any
# changes to data that happen in a process won’t transfer automatically to that same data outside of the process.
# Let’s look at some examples that illustrate this feature.





