
import random
random.seed()

def bubble_sort(data: list, reverse=False):
    """Compares each adjacent pair of elements in a list and swaps
    when out of order, repeating until returning a sorted list"""
    length = len(data)
    for loop in range(length):
        for pair in range(0, length - loop - 1):
            if (not reverse and data[pair] > data[pair+1]) or (reverse and data[pair] < data[pair+1]):
                data[pair], data[pair+1] = data[pair+1], data[pair]
    return data

def merge(left, right, reverse):
    """Merges two sorted lists into a single list, reversing the order if needed"""
    merged = []
    lindex = 0
    rindex = 0
    while lindex < len(left) and rindex < len(right):
        if (left[lindex] <= right[rindex] and not reverse) \
        or (left[lindex] >= right[rindex] and reverse):
            merged.append(left[lindex])
            lindex += 1
        else:
            merged.append(right[rindex])
            rindex += 1
    merged.extend(left[lindex:])
    merged.extend(right[rindex:])
    return merged

def merge_sort(data: list, reverse=False):
    """Splits a list into halves to sort, using merge to split the
    resulting sorted halves. Returns a single sorted list."""
    if len(data) <= 1: return data

    split_list = lambda lst: (lst[:len(lst) // 2], lst[len(lst) // 2:])
    listx, listy = split_list(data)

    lhalf = merge_sort(listx, reverse)
    rhalf = merge_sort(listy, reverse)

    return merge(lhalf, rhalf, reverse)

def bisect_search(sorted_data:list, value) -> int:
    """Divides sorted_data in half and determines which half the passed
    value should be in. If it is found, returns the index of value. If not found,
    returns -1"""
    if not sorted_data:
        return -1
    amt = len(sorted_data)//2
    l = sorted_data[:amt]
    r = sorted_data[amt:]
    if value == sorted_data[amt]:
        return amt
    elif value < sorted_data[amt]:
        return bisect_search(l, value)
    else:
        result = bisect_search(r, value)
        return amt + result if result != -1 else -1

class Node:
    def __init__(self, value, parent=None):
        self._parent = parent
        self._left = None
        self._right = None
        self._value = value
        self._quantity = 1

    def __repr__(self):
        if self._left is None and self._right is None:
            return f'{self._value}'
        return f'{self._value} ({self._left}, {self._right})'

    def __eq__(self, other):
        return self._value == other

    def __gt__(self, other):
        return self._value > other

    def __lt__(self, other):
        return self._value < other

    def __le__(self, other):
        return self._value <= other

    def __ge__(self, other):
        return self._value >= other

    def insert(self, value):
        if value < self:
            if self._left is None:
                self._left = Node(value, self)
            else:
                self._left.insert(value)
        elif value > self:
            if self._right is None:
                self._right = Node(value, self)
            else:
                self._right.insert(value)
        elif value == self._value:
            self._quantity += 1

    def traverse(self):
        if self._left:
            yield from self._left.traverse()
        yield self._value
        if self._right:
            yield from self._right.traverse()

    def traverse_reverse(self):
        if self._right:
            yield from self._right.traverse_reverse()
        yield self._value
        if self._left:
            yield from self._left.traverse_reverse()

    def __contains__(self, value):
        if value == self._value:
            return True
        elif value < self._value and self._left:
            return value in self._left
        elif value > self._value and self._right:
            return value in self._right
        return False

class Tree:
    def __init__(self, iterable=()):
        self._root = None
        for value in iterable:
            self.insert(value)

    def insert(self, value):
        if self._root is None:
            self._root = Node(value)
        else:
            self._root.insert(value)

    def __iter__(self):
        if self._root:
            yield from self._root.traverse()

    def reverse(self):
        if self._root:
            yield from self._root.traverse_reverse()

    def __contains__(self, value):
        if self._root:
            return value in self._root
        return False

    def __repr__(self):
        return repr(self._root)

