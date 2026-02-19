import math
from collections import OrderedDict


def calculate_area(length, width):
    area = length * width
    return area


def is_even(number):
    return number % 2 == 0


def greet_user(name):
    age = 25
    message = "Hello " + name + " you are " + str(age) + " years old"
    return message


def is_positive(number):
    if number > 0:
        return True
    return False


def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total


def get_square_roots(numbers):
    return [math.sqrt(n) for n in numbers]


def count_above_threshold(numbers, threshold):
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def classify_number(n):
    if n > 0:
        label = "positive"
    elif n < 0:
        label = "negative"
    else:
        label = "zero"
    return label


def multiply(a, b):
    return a * b
