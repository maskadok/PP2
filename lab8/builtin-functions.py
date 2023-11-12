#1
from functools import reduce
def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)
list_numbers = [2, 3, 4]
product = multiply_list(list_numbers)

#2
def count_case(s):
    upper, lower = 0, 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower
sample_string = "Hello World!"
upper_count, lower_count = count_case(sample_string)

#3
def is_palindrome(s):
    return s == s[::-1]
palindrome_test = "radar"
is_palindrome_result = is_palindrome(palindrome_test)

#4
import time
import math
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)
number = 25100
delay_ms = 2123
sqrt_result = delayed_sqrt(number, delay_ms)

#5
def all_true(t):
    return all(t)
test_tuple = (True, True, True)
all_true_result = all_true(test_tuple)