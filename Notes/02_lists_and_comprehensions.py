



# Notes - 1/30/2020

# LISTS
import random

my_names = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo"]
my_numbers = [5, 9, 12, 6, -3, 6]


# Indexing Lists
print(my_names)  # Whole List
print(my_names[2])  # Cam
print(my_names[-1])  # Flo
print(my_names[:3])  # Abe to Cam
print(my_names[3:5])  # Dan to Eve
print(my_names[:])  # Everybody


# Copy a List
my_copy = my_names  # This is the wrong way!
my_copy.append("Gil")
print(my_copy)
print(my_names)

my_copy = my_names[:]  # Do it this way!
my_names.append("Hal")
print(my_copy)
print(my_names)


# 2D lists
my_2d = [["Peanut", "Butter", "Jelly"], [8, "Hello"], ["Spam", "Eggs"]]
print(my_2d)
print(my_2d[1])  # [8, "Hello"]
print(my_2d[1][1])  # Hello
my_2d[1].append("Bye")
print(my_2d)


# if in
if "Hal" in my_names:
    print("Hal is in my_names")


# LIST FUNCTIONS
print(len(my_names))  # length of the list (not the last index)
print(min(my_numbers))  # lowest value
print(max(my_numbers))  # highest value
print(sum(my_numbers))  # adds all the values

print(min(my_names))  # first in alphabetical order
my_names.append('aaron')  # still not first because it is a lowercase a
print(max(my_names))  # last in alphabetical order


# LIST METHODS
print(my_names.index("Cam"))  # returns the index of "Cam"
my_names.append("Cam")
print(my_names.index("Cam"))  # only sees the first instance
print(my_names.count("Cam"))  # number of instances
print(my_names.count("Mia"))
my_names.append("Deb")
print(my_names)
del my_names[my_names.index("aaron")]  # delets "aaron
print(my_names)
my_names.sort()  # orders in alphabetical order
print(my_names)
my_names.reverse()  # reverses list order
print(my_names)


# MODIFYING LISTS
del my_names[4]
print(my_names)

my_names.pop()  # pops one off the end of the list
print(my_names)

end_of_list = my_names.pop()  # pops OFF and returns
print(my_names)
print(end_of_list)

front_of_list = my_names.pop(0)  # pops by index
print(front_of_list)
print(my_names)


# Concatenation
first = "Francis"
last = "Parker"
print(first + last)  # smooshes them together
print(my_names + my_numbers)  # puts the two lists into one lists


# Iterating Through Lists
list = []
for i in range(10):
    list.append(i)
print(list)

# For each only looks at a copy
for item in list:
    item += 1
    print(item)
print(list)

# Add one to every item in the list using (use an index variable loop)
# This is how we modify a list in a loop
for i in range(len(list)):  # use this method
    list[i] += 1
print(list)

my_list = [x for x in range(10)]
print(my_list)

my_list = [x + 1 for x in range(10)]  # to modify list
print(my_list)