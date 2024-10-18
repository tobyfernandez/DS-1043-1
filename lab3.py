"""Module implementing functions for the lab 2 exercises, as well as FizzBuzz and Ordinal Suffixes
    
Completed by Tobias Fernandez on 2024-09-10 for DS-1043"""

import time
import math
Number = float

def is_odd(number: Number) -> bool:
    """ Returns a Boolean value denoting whether or not the number inputted is odd """
    if type(number) == float:
        return False
    elif number%2 != 0:
        return True
    else:
        return False

def is_even(number: Number) -> bool:
    """ Returns a Boolean value denoting whether or not the number inputted is evem """
    if type(number) == float:
        return False
    elif number%2 == 0:
        return True
    else:
        return False

def time_elapsed(timestamp: int) -> tuple[int, int, int, int]:
    """ Determines the time elapsed from the timestamp given,
    returning a tuple containing the time in days, hours, minutes, and seconds """
    num = time.time() - timestamp
    num1 = num // 86400 #days
    num = num % 86400
    num2 = num // 3600  #hours
    num = num % 3600
    num3 = num // 60    #minutes
    num = num % 60
    num4 = num // 1     #seconds
    return num1, num2, num3, num4

def area(length: Number, width: Number) -> Number:
    """ Returns the area of a shape when given its length and width """
    return length*width

def perimeter(length: Number, width: Number) -> Number:
    """ Returns the perimeter of a shape when given its length and width """
    return length*2 + width*2

def volume(length: Number, width:Number, height: Number) -> Number:
    """ Retuns the volume of a shape when given its length, width, and height """
    return length*width*height

def surface_area(length: Number, width: Number, height: Number) -> Number:
    area = length*width*2 + length*height*2 + width*height*2
    return area

def get_square_color(column: int, row: int) -> str:
    """ Prints the color of a square from a chess board given its coordinates, (column, row) """
    if column <= 7 and row <= 7:
        if is_odd(column + row) == True:
            return str("Black")
        else:
            return str("White")
    else:
        return str("")

def prettify_time(timestamp) -> str:
    """ Takes the time from the time_elapsed function, calculated from a certain timestamp,
    and prints the time in a more elegant format """
    time = time_elapsed(timestamp)
    days = time[0]
    hours = time[1]
    minutes = time[2]
    seconds = time[3]
    return str(math.trunc(days)) + " days, " + str(math.trunc(hours)) + " hours, " + str(math.trunc(minutes)) + " minutes, " + str(math.trunc(seconds)) + " seconds"

def center_justify(content: str, width: int) -> str:
    """ Justifies inputted text (content) to the center given a certain text column width """
    spacing = len(content)
    return str(" " * ((width//2) - (spacing//2))) + str(content)

def right_justify(content: str, width: int) -> str:
    """Justifies inputted text (content) to the right given a certain text column width """
    spacing = len(content)
    return str(" " * (width - spacing)) + str(content)

def fizz_buzz(up_to: Number) -> str:
    """Evaluates every integer from 1 to the up_to number provided, and labels it as FizzBuzz if divisible by 3 and 5,
    as Fizz if divisible only by 3, as Buzz if divisible only by 5, and simply returns the string of the integer if it
    is divisible by neither 3 nor 5"""
    integer = 1
    soda = "" #this string includes all the fizzes, buzzes, and integer values
    while integer <= up_to:
        if integer%3 == 0 and integer%5 == 0:
            soda = soda + str("FizzBuzz ")
        elif integer%3 == 0:
            soda = soda + str("Fizz ")
        elif integer%5 == 0:
            soda = soda + str("Buzz ")
        else:
            soda = soda + str(integer) + " "
        integer = integer + 1
    return soda

def ordinal_suffix(number: Number) -> str:
    """Returns an ordinal number as a string with the appropriate suffix attached"""
    if 11 <= (number % 100) <= 13:
        suffix = 'th'
    elif number % 10 <= 3:
        suffix = ('th', 'st', 'nd', 'rd')[number % 10]
    else:
        suffix = 'th'
    return str(number) + suffix

