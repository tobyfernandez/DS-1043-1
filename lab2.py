""" Lab 2 - Module implementing the following functions:
    is_odd  and  is_even  which determine whether a number is odd or even;
    time_elapsed  which determines the amount of time between the calling of the function and the timestamp;
    several functions which determine amounts of space given length, width, and height;
    get_square_color  which determines the color of a chess board;
    prettify_print  which prints the time determined by time_elapsed in an elegant format; and
    justification functions which allow text to be justified in a certain way.
Completed by Tobias Fernandez, ID 1608357 on 2024-09-05 for DS-1043"""

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

def get_square_color(column: int, row: int) -> str:
    """ Prints the color of a square from a chess board given its coordinates, (column, row) """
    if column <= 7 and row <= 7:
        if is_odd(column + row) == True:
            print("black")
        else:
            print("white")
    else:
        print("")

def prettify_time(timestamp) -> str:
    """ Takes the time from the time_elapsed function, calculated from a certain timestamp,
    and prints the time in a more elegant format """
    time = time_elapsed(timestamp)
    days = time[0]
    hours = time[1]
    minutes = time[2]
    seconds = time[3]
    print(math.trunc(days), "days,", math.trunc(hours), "hours,", math.trunc(minutes), "minutes,", math.trunc(seconds) ,"seconds")

def center_justify(content: str, width: int) -> str:
    """ Justifies inputted text (content) to the center given a certain text column width """
    spacing = len(content)
    print(" " * ((width//2) - (spacing//2)), content)

def right_justify(content: str, width: int) -> str:
    """Justifies inputted text (content) to the right given a certain text column width """
    spacing = len(content)
    print(" " * (width - spacing), content)


#Tests of Functions:

#  print(is_odd(-3))
#  print(is_odd(3.14))
#  print(is_even(4))
#  print(is_even(-4.5))
#  print(time_elapsed(0))
#  print(area(2, 3))
#  print(perimeter(2, 3))
#  print(volume(2, 3, 4))
#  get_square_color(0, 7)
#  get_square_color(7, 1)
#  get_square_color(8, 0)
#  prettify_time(0)
#  center_justify("center", 50)
#  right_justify("right", 50)