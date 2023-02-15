from multiprocessing import Process, Manager


def change_a_list(x_list):
    x_list.append(100)
    print("Inside the process:", x_list)
    return x_list


num_list = [1, 2, 3, 6]
print("Before the process:", num_list)

if __name__ == '__main__':
    with Manager() as manager:
        print("this is the start")
        pass_list = manager.list(num_list)
        print("this is the pass_list")
        our_process = Process(target=change_a_list, args=[pass_list])
        print("this is just before the start of the multi processing")
        our_process.start()
        our_process.join()
        num_list = list(pass_list)

    print("Outside the process:", list(num_list))

# Is it really necessary to pass the list data from one variable to another? Try commenting out num_list = list(
# pass_list)  and change the final line to:
#
# print("Outside the process:", list(pass_list))
# What happens when you run the program now?
#
# Remember, a variable is assigned a memory address. After the program passes the list to the function in the sub
# process, pass_list() now points to contents that sit in the memory space in our_process. Manager allows you to pass
# data from a variable in the subprocess to a variable outside, but you still cannot reuse the subprocess variable in
# your program’s main process.
#
# There are other ways of transferring data between processes that are probably better, but the goal now is not to
# write the most optimal code that is humanly possible. Rather, it’s important to write the program in a simple way
# so that it’s easier for you to understand the fundamental concepts. Optimisation will come in time. Just keep on
# coding and you will get there!


