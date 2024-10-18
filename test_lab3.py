from lab3 import is_even, is_odd, time_elapsed, area, perimeter, volume, get_square_color, prettify_time, center_justify, right_justify, fizz_buzz, ordinal_suffix

import time
import math

#determining the time to test time-related functions:
num = (time.time())
num1 = num // 86400
num = num % 86400
num2 = num // 3600
num = num % 3600
num3 = num // 60
num = num % 60
num4 = num // 1
time_since = (num1, num2, num3, num4)
days = time_since[0]
hours = time_since[1]
minutes = time_since[2]
seconds = time_since[3]


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(2.5) == False
print(test_is_even())

def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(2.5) == False
print(test_is_odd())

def test_time_elapsed():
    assert time_elapsed(0) == time_since
print(test_time_elapsed())

def test_area():
    assert area(2,2) == 4
print(test_area())

def test_perimeter():
    assert perimeter(2, 2) == 8
print(test_perimeter())

def test_volume():
    assert volume(1, 1, 1) == 1
print(test_volume())

def test_get_square_color():
    assert get_square_color(0,0)
print(test_get_square_color())

def test_prettify_time():
    assert prettify_time(0) == str(math.trunc(days)) + " days, " + str(math.trunc(hours)) + " hours, " + str(math.trunc(minutes)) + " minutes, " + str(math.trunc(seconds)) + " seconds"
print(test_prettify_time())

def test_center_justify():
   assert center_justify("a", 7) == "   a"
print(test_center_justify())

def test_right_justify():
    assert right_justify("a", 7) == "      a"
print(test_right_justify())

def test_fizz_buzz():
    assert fizz_buzz(5) == "1 2 Fizz 4 Buzz "
print(test_fizz_buzz())

def test_ordinal_suffix():
    assert ordinal_suffix(1) == "1st"
    assert ordinal_suffix(2) == "2nd"
    assert ordinal_suffix(11) == "11th"
    assert ordinal_suffix(21) == "21st"
print(test_ordinal_suffix())