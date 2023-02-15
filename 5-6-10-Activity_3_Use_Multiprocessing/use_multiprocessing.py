# install time
import time

start_time = time.time()


def prime_test(number):
    for i in range(2, number):
        if num % i == 0:
            return False

    return True


#num = 2 ** 31 - 1
num = 2**19-1


print("Is Prime: ", prime_test(num))
print("It took: ", time.time()-start_time, "seconds to run the script")

# OUTPUT
# # num = 2**31-1
#
# Is Prime: True
#
# It took: 155.3124589920044 seconds to run the script
#
#
#
# # num = 2**19-1
#
# Is Prime: True
#
# It took: 0.015623092651367188 seconds to run the script