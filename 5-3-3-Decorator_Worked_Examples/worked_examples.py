def validation_decorator(func):
    def validation_wrapper(*args):
        if not args[0].isdigit() or not args[1].isdigit():
            raise Exception("Both number have to be either integers")
        else:
            num_01 = int(args[0])
            num_02 = int(args[1])
        if isinstance(num_01, int) and isinstance(num_02, int):
            return func(num_01, num_02)
        else:
            raise Exception("Both number have to be either integers")

    return validation_wrapper


@validation_decorator
def add(num_01, num_02):
    return num_01 + num_02


@validation_decorator
def subtract(num_01, num_02):
    return num_01 - num_02


@validation_decorator
def multiply(num_01, num_02):
    return num_01 * num_02


@validation_decorator
def divide(num_01, num_02):
    if num_02 != 0:
        return num_01 / num_02
    else:
        return "Cannot divide by zero!"


while True:
    first_num = input("Enter first number or q to quit: ")
    if first_num == 'q':
        break
    second_num = input("Enter the second number or q to quit: ")
    if second_num == 'q':
        break
    operation = input(
        "Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter q to "
        "quit: ")
    if operation == 'q':
        break
    elif operation == '1':
        print(add(first_num, second_num))
    elif operation == '2':
        print(subtract(first_num, second_num))
    elif operation == '3':
        print(multiply(first_num, second_num))
    elif operation == '4':
        print(divide(first_num, second_num))
    else:
        print("Invalid operation. Try again!")
