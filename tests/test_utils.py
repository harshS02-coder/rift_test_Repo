import os
import sys
import json
import math
import random

# ─── Bug 1: LINTING — unused imports (os, sys, json, random) ─────────────────

# ─── Bug 2: INDENTATION error ────────────────────────────────────────────────
def calculate_area(length, width):
    area = length * width
      return area


# ─── Bug 3: SYNTAX error — missing colon ─────────────────────────────────────
def is_even(number)
    return number % 2 == 0


# ─── Bug 4: TYPE_ERROR — string + int ────────────────────────────────────────
def greet_user(name):
    age = 25
    message = "Hello " + name + " you are " + age + " years old"
    return message


# ─── Bug 5: LOGIC error — wrong operator ─────────────────────────────────────
def is_positive(number):
    if number < 0:          # should be > 0
        return True
    return False


# ─── Bug 6: IMPORT error — wrong module name ─────────────────────────────────
from collections import OrderedDikt   # typo: should be OrderedDict


# ─── Bug 7: LOGIC error — off-by-one in loop ─────────────────────────────────
def sum_list(numbers):
    total = 0
    for i in range(len(numbers) + 1):   # should be range(len(numbers))
        total += numbers[i]
    return total


# ─── Bug 8: SYNTAX error — missing closing bracket ───────────────────────────
def get_square_roots(numbers):
    return [math.sqrt(n) for n in numbers


# ─── Bug 9: TYPE_ERROR — wrong type comparison ───────────────────────────────
def count_above_threshold(numbers, threshold):
    count = 0
    for n in numbers:
        if n > "threshold":    # comparing int to string literal
            count += 1
    return count


# ─── Bug 10: LOGIC error — returns wrong value ───────────────────────────────
def fahrenheit_to_celsius(f):
    return (f + 32) * 5 / 9   # should be (f - 32) * 5 / 9


# ─── Bug 11: INDENTATION error inside if block ───────────────────────────────
def classify_number(n):
    if n > 0:
        label = "positive"
    elif n < 0:
            label = "negative"   # wrong indentation
    else:
        label = "zero"
    return label


# ─── Bug 12: LINTING — variable defined but never used ───────────────────────
def multiply(a, b):
    unused_variable = 42
    return a * b
