import multiprocessing
import time

start_time = time.time()


def PrimeNumber(number):
    for i in number:
        if i in range(2, number):
            return False

    return True


num = 2 ** 31 - 1

process = multiprocessing.Process(target=PrimeNumber, args=num)
process.start()
process.join()
print('process time: ', time.time() - start_time)
