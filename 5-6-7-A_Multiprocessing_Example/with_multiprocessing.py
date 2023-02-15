import multiprocessing


# Example: With Multiprocessing

def change_list(x_list):
    return x_list.append(10)


if __name__ == '__main__':
    print('With Multiprocessing')
    our_list = [1, 2, 3, 4, 5]
    print("The list before processing:", our_list)
    p1 = multiprocessing.Process(target=change_list, args=[our_list])

    p1.start()

    print("The list after processing:", our_list)
    print(" ")

# As you can see, the change only happens in the memory space of the process, but outside it the list remains the
# same, as this is a different memory space. Note that even using the join()  method does not transfer the data to
# the main process. Try removing the p1.join() line and see if it makes a difference.
# LOOK AT INSIDE VS OUTSIDE TO SEE THE APPENDED LIST

