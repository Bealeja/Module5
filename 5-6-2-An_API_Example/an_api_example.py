import asyncio
import time


async def test_01():
    print("Something")
    await asyncio.sleep(1)
    print("Anything")


async def test_02():
    print("Hi")
    await asyncio.sleep(1)
    print("Goodbye")


async def main():
    await asyncio.gather(test_01(), test_02(), test_01())


start = time.perf_counter()
asyncio.run(main())
execution_time = time.perf_counter() - start
print("Execution Time: " + str(round(execution_time, 2)) + " seconds")


# OUTPUT
# Something
#
# Hi
#
# Something
#
# Anything
#
# Goodbye
#
# Anything
#
# Execution Time: 1.0 seconds


# Try this sequential version, notice the time difference
def test_01():
    print("Something")
    time.sleep(1)
    print("Anything")


def test_02():
    print("Hi")
    time.sleep(1)
    print("Goodbye")


time_start = time.time()
test_01()
test_02()
test_01()
time_end = time.time()
print("Execution Time: " + str(round(time_end - time_start, 2)) + " seconds")


# OUTPUT
# Something
#
# Hi
#
# Something
#
# Anything
#
# Goodbye
#
# Anything
#
# Execution Time: 3.0 seconds

# Another Example

async def test_03():
    print("Something")
    return await test_04()


async def test_04():
    print("Hi")
    return await test_05()


async def test_05():
    print("Walk")
    return await test_end()


async def test_end():
    print("Finished!")


async def main():
    await asyncio.gather(test_03(), test_05(), test_04(), test_05(), test_end())


time_start = time.time()
asyncio.run(main())
time_end = time.time()
print("Execution Time: " + str(round(time_end - time_start, 2)) + " seconds")


# OUTPUT
# Something
#
# Hi
#
# Walk
#
# Finished!
#
# Walk
#
# Finished!
#
# Hi
#
# Walk
#
# Finished!
#
# Walk
#
# Finished!
#
# Finished!
#
# Execution Time: 0.0 seconds

# Try for yourself Use one of the examples given here as a template and see if you can adapt an HTTP request program
# you wrote in Week 3 to execute asynchronously. Can you write the program so that it can do something else while
# waiting for the API to respond?
#
# For example, you could add a ‘loading’ progress bar to the program. You could use a loop and the  sleep() method to
# print a row of ‘*’ until the response has been downloaded.
#
# Also, try to make the API request as time-consuming as possible, so that you can see the difference that
# asynchronous programming makes.