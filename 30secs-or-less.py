import operator
import time
import sys

a = [1, 2, 3, 4, 5]


def all_unique(lst):
    return len(lst) == len(set(lst))


# Memory - check memory usage of an object


variable = 30
print(sys.getsizeof(variable))

# Byte size - returns the length of a string in bytes


def byte_size(string):
    return(len(string.encode('utf-8')))


# Print a string N times

n = 2
s = "Programming"
# print(s * n)

# Compact


def compact(lst):
    return list(filter(bool, lst))


# Count by
array = [['1', '2'], ['3', '4'], ['5', '6']]
transposed = zip(*array)
print(transposed)

# Get vowels


def get_vowels(string):
    return [letter for letter in string if letter in 'aeiou']


# Decapitalize
def decapitalize(str):
    return str[:1].lower() + str[1:]


# Flatten

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

# Chained function call


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 4, 5

print((subtract if a > b else add)(a, b))


# Merge two dictionaries

def merge_two_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c


def merge_dictionaries(a, b):
    return {**a, **b}


def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]


# Time spent


start_time = time.time()

a = 1
b = 2
c = a + b
print(c)

end_time = time.time()
total_time = end_time - start_time


# Try else
try:
    2 * 3
except TypeError:
    print("An exception was raised")

else:
    print("Thank god, no exceptions were raised")


# Most frequent
def most_frequent(list):
    return max(set(list), key=list.count)


def sayHi():
    return "hi"

# Calculator


action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": sayHi,
}

print(action['**']())
