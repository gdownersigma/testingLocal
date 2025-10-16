def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1-num2


def multiply_numbers(num1, num2):
    return num1*num2


def divide_numbers(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        return 0


print(add_numbers(7, 5))
print(subtract_numbers(10, 2))
print(multiply_numbers(4, 8))
print(divide_numbers(9/3))
