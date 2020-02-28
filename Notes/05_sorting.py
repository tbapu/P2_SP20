



# Notes - Sorting
import random

a = 1
b = 2

temp = a
a = b
b = temp
print(a, b)

# Pythonic Way
a, b = b, a  # works only in Python
print(a, b)


# Make a random list of 100 numbers with values 1 to 99

my_list = [random.randrange(1, 100) for x in range(100)]
my_list2 = my_list[:]  # don't forget to make copy like this

print(my_list)


# SELECTION SORT
for cur_pos in range(len(my_list)):
    min_pos = cur_pos  # current dancer is the assumed lowest
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos  # if we find a lower dancer, we update the min_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]  # swap the dancers

print(my_list)


# INSERTION SORT
for key_pos in range(1, len(my_list2)):  # must start at 1
    key_val = my_list2[key_pos]  # key dancer
    scan_pos = key_pos - 1  # look to the dancer's left
    while scan_pos >= 0 and key_val < my_list2[scan_pos]:
        my_list2[scan_pos + 1] = my_list2[scan_pos]  # move the scan_pos left
        scan_pos -= 1
    my_list2[scan_pos + 1] = key_val  # commit the move

print(my_list2)


# Optional Function Parameters
print("Hello", end=" ")  # default end is "\n"
print("World", end="!\n")
print("Hello", "World", sep="Big", end="!!!\n")  # default sep is space

def hello(name, time_of_day="morning"):
    print("Hello", name, "good", time_of_day)

hello("Star", "afternoon")
hello("Mia")
hello("James", time_of_day="evening")


# Lambda Functions
# When you need a function, but don't want to make a function
# Also called anonymous functions


# name = lambda (parameter): (returned)
double_me = lambda x: x * 2
print(double_me(5))

product = lambda a, b: a * b
print(product(4,6))


# Real World Sorting with Python
my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)
my_2d_list = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
print(my_2d_list)


# sort method (changes the list in place)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_2d_list.sort(key=lambda a: a[0])  # first item in list
print(my_2d_list)
my_2d_list.sort(key=lambda a: a[1])  # second item in list
print(my_2d_list)
my_2d_list.sort(reverse=True, key=lambda a: sum(a))
print(my_2d_list)


# Sorted function (returns a new list)
new_list = sorted(my_2d_list, reverse=True, key=lambda x: abs(x[0] - x[1]))
print(new_list)
