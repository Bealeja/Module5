# Example: Without Multiprocessing

def change_list(x_list):
    x_list.append(10)


if __name__ == '__main__':
    our_list = [1, 2, 3, 4, 5]
    change_list(our_list)
    print(our_list)
