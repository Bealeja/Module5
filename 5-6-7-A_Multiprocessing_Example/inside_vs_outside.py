import multiprocessing


# Example: Inside vs outside a process

def change_list(x_list):
    x_list.append(10)
    print(x_list, "inside the process")
    return x_list


if __name__ == '__main__':
    print("Inside vs outside a process")
    our_list = [1, 2, 3, 4, 5]
    print("The list before processing:", our_list)
    p1 = multiprocessing.Process(target=change_list, args=[our_list])

    p1.start()
    p1.join()

    print(our_list, "outside the process")
    print(" ")
