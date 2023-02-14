import multiprocessing


# Example: With Multiprocessing

def change_list(x_list):
    return x_list.append(10)


print('With Multiprocessing')
our_list = [1, 2, 3, 4, 5]
print("The list before processing:", our_list)
p1 = multiprocessing.Process(target=change_list, args=[our_list])

p1.start()

print("The list after processing:", our_list)
print(" ")
