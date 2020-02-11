



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
print(linear_search("Edgar the Grim", villains))


# Binary Search




















