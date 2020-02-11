



# Notes - 2/10/2020


# Searching and Read/Write Files


# forward slash goes into a directory.  ".." goes 'up' a directory.
# by default, open() opens a file to read.
file = open('resources/super_villains.txt', 'r')
print(file)
file.close()


# Open a file to write with "w"
# Overwrites entire file


# Open a file to append with "a"
file = open('resources/super_villains.txt', 'a')
file.write("Mia the Horrible\n")
file.close()


# Go through the info in the file line by line
file = open('resources/super_villains.txt', 'r')
for line in file:
    print(line.strip().upper())
file.close()  # ends your access to the file


# .strip() method strips out spaces, tabs, returns (\t, \n, etc.)
print("Hi\n".strip())
print("  Hello".strip())


# Better way to open files (syntactic sugar)
with open('resources/super_villains.txt', 'r') as f:
    for line in f:
        print("Hello", line)


# Read data into a list (a.k.a. array)
with open('resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]
print(villains)


# Linear Search


# Python Way
print("VARVARA TEMPEST" in villains)  # in  keyword


# Brute Force Way
i = 0
key = "VARVARA TEMPEST"
while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < (len(villains) - 1):
    print("Found", key,"at position", i)

else:
    print(key, "not found.")


# Make a Function out of it
def linear_search(key, list):
    """
    Searches for key inside of list and returns True if you found it.
    :param key: item to find
    :param list: list to find key in
    :return: bool found (True/False)
    """
    i = 0
    while i < (len(list) - 1) and key.upper() != list[1]:
        i += 1
    if i < (len(list) - 1):
        print("Found", key, "at position", i)
        return True

    else:
        print(key, "not found.")
        return False
print(linear_search("EDGAR THE GRIM", villains))


# Binary Search
villains.sort()  # must be sorted

key = "THEODORA THE WICKED"

lower_bound = 0
upper_bound = len(villains) - 1  # Length in not in index
found = False
while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2  # chops off decimals
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1  # middle_pos includes to middle point
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        find = True

if found:
    print(key, "found at position", middle_pos)
else:
    print(key, "was not found")


# GIFTED FUNCTION
# returns a list of words in each line

import re  # regular expression
def spilt_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

text = "Hello, this is Aaron's phone!"
print(spilt_line(text))  # ['Hello', 'this', 'is', "Aaron's", 'phone']


