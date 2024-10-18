"""Lab 4
Module implementing very basic statistics and probablility functions.
Completed by Tobias Fernandez on 2024-9-17 for DS-1043"""

import math
import random
from ast import Index

Number = int | float
Sequence = list | tuple


def my_max(numbers: Sequence) -> Number:
    """Examines a list or tuple and returns the highest value within it"""
    numbers = tuple(numbers)
    if len(numbers) < 1:
        raise ValueError
    else:
        index = 0
        highest = numbers[0]
        while index < len(numbers):
            if numbers[index] > highest:
                highest = numbers[index]
            index = index + 1
        return highest

def my_min(numbers: Sequence) -> Number:
    """Examines a list or tuple and returns the lowest value within it"""
    if len(numbers) < 1:
        raise ValueError
    else:
        numbers = tuple(numbers)
        index = 0
        lowest = numbers[0]
        while index < len(numbers):
            if numbers[index] < lowest:
                lowest = numbers[index]
            index = index + 1
        return lowest


print(my_min([4, 5, 6]))

def my_sum(numbers: Sequence) -> Number:
    """Examines a list or tuple and returns the sum of all its elements"""
    if len(numbers) < 1:
        raise ValueError
    else:
        index = 0
        sum = 0
        while index < len(numbers):
            sum = sum + numbers[index]
            index = index + 1
        return sum

def my_average(numbers: Sequence) -> Number:
    """Returns the average of the values contained in the sequence"""
    if len(numbers) < 1:
        raise ValueError
    else: return my_sum(numbers) / len(numbers)


def my_median(numbers: Sequence) -> Number:
    """Returns the median of the values contained in the sequence"""
    if len(numbers) < 1:
        raise ValueError
    else:
        numbers = list(numbers)
        numbers.sort()
        length = len(numbers)
        if length % 2 != 0:
            median = numbers[length//2]
            return median
        else:
            median = (numbers[length//2] + numbers[length//2 - 1]) / 2
            return median


def my_mode(numbers: Sequence) -> Number:
    """Returns the mode of the values contained in the sequence"""
    if len(numbers) < 1:
        raise ValueError
    else:
        frequency = dict()  #Keys are numbers being counted for frequency
        count = 0
        for n in numbers:
            for j in numbers:
                if n == j:
                    count = count + 1
                    frequency[n] = count
            count = 0
        inverted_frequency = {value: key for key, value in frequency.items()} #keys are now frequency of numbers
        return inverted_frequency[my_max((inverted_frequency))]

def roll_dice(amount: Number, type: Number) -> tuple:
    """Rolls the requested 'amount' of dice with the number of faces specified by 'type' and returns
    the results"""
    dice_remaining = amount
    results = ()
    while dice_remaining > 0:
        results = results + (random.randint(1,type),)
        dice_remaining = dice_remaining - 1
    return results



random.seed()