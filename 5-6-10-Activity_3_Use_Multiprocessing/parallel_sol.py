# We will use the ‘time’ module to get the current time that we will need to measure the execution time of our program:
import time
# We will need the ‘multiprocessing’ module to be able to spawn multiple processes:
import multiprocessing
# We’ll use the ‘sys’ module to acquire operating-system-specific information:
import sys
# The os module will be used to learn how many threads are available in a given machine:
import os

# We will record the starting time straight away:
start_time = time.time()


# We will use the function prime_test to determine if a number is prime or not. It takes three parameters,
# namely the number that we wish to check to see if it is prime, start, and end index of the check:
def prime_test(num, start_index, end_index):
    # To check if a number is prime or not, we need to check if that number is divisible by any other number without the
    # remainder, other than one and itself. If it is, then it is not a prime and we return ‘False’. Otherwise,
    # the number is prime and we return ‘True’:
    for i in range(start_index, end_index):
        if num % i == 0:
            return False

    return True


# Next, we need to determine the number of available threads on our computer. To do this, we will make use of the
# get_the_number_of_available_threads function, which will first check the platform with sys.platform and,
# depending on the platform, the os module will be used to extract information about the CPU in terms of how many
# threads are available:
def get_the_number_of_available_threads():
    if sys.platform == 'win32':
        return int((os.environ['NUMBER_OF_PROCESSORS']))
    else:
        return int((os.popen('grep -c cores /proc/cpuinfo').read()))


# Great! We are done gathering the needed information. Now, we can proceed to split up the tasks and send them off to
# multiple processes for processing:
def split_tasks(num):
    # Here we will store the number of available threads into a variable threads:
    threads = get_the_number_of_available_threads()

    # Each process will check a given range of numbers, so we need to split the number of checks into chunks that we
    # will assign to multiple processes:
    remainder = int(num % threads)
    task_chunks = int(num // threads)

    # Inside the variable processes, we will store references to all the scheduled processes that we will start and
    # join:
    processes = []

    # Depending on the number of available threads, we will determine how many processes to start. If it is not the
    # first iteration, we create a process consisting of the function that we wish to call and the arguments we wish
    # to pass, as the argument form is different for the first and last process. We need to create edge cases for
    # them. But, in order to create a process, we need to use a multiprocessing module and then call the process from
    # it. Then, we will pass the name of the function and the arguments of the function to it. In our case,
    # the function is called prime_test and the arguments are the numbers that are being checked and the task chunks
    # we have created.
    #
    # Past this point, we will store the process into the variable ‘t’, which is overwritten in each iteration of the
    # loop. But, we do end up storing the process into our processes list, where we will hold the reference to a
    # process.
    for i in range(threads):
        if i != 0:
            t = multiprocessing.Process(target=prime_test,
                                        args=(num, (task_chunks * i), (task_chunks * (i + i))))
            processes.append(t)
            t.start()
        elif i == threads - 1:
            t = multiprocessing.Process(target=prime_test,
                                        args=(num, (task_chunks * i), (task_chunks * (i + i + remainder))))
            processes.append(t)
            t.start()
        else:
            t = multiprocessing.Process(target=prime_test, args=(num, 2, task_chunks))
            processes.append(t)
            t.start()

    # Once we have created all the processes and stored them, we will proceed to join them:
    for th in processes:
        th.join()


# The ‘num’ variable will hold the number that we wish to test.
#
# Now, with the calculation 2**31-1, you will see that the multiprocess approach will be faster while the processing
# time will be about the same if not slower with a smaller number.

if __name__ == '__main__':
    num = 2**31-1
    # num = 2 ** 19 - 1
    # We got to the point where we wish to start the whole procedure and so we will split_tasks with the function to
    # which 'num' will be passed as a parameter:
    split_tasks(num)
    # In the end, we will print out the results of our findings and the total time it took to complete the task:
    print("All Threads Have finished!")
    print("It took: ", time.time() - start_time, "seconds to run the script")
