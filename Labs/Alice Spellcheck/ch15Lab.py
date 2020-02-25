'''
Tashi Bapu - 2020
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("dictionary.txt")
dictionary_list = []
for word in file:
    dictionary_list.append(word.strip())
print(dictionary_list)
file.close()


print("--- Linear Search ---")

file = open("AliceInWonderLand200.txt")
dictionary = open("dictionary.txt")
words = []
line_num= 0

for line in file:
    line_num += 1
    words = split_line(line.strip())
    for word in words:
        found = False
        is_it_there = 0
        while not found:
            for w in dictionary_list:
                if w == word.upper():
                    is_it_there += 1
            if is_it_there == 0:
                print("Found On Line", line_num)
                print(word.upper())
            found = True
file.close()
dictionary.close()


print("--- Binary Search ---")

file = open("AliceInWonderLand200.txt")
dictionary = open("dictionary.txt")
line_num = 0
words = []

for line in file:
    line_num += 1
    words = split_line(line.strip())
    for word in words:
        found = False
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print(line_num)
            print(word.upper())
file.close()
dictionary.close()


# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
print("--- Challenge ---")

land = open("AliceInWonderLand.txt")
land_words = []
line_num = 0

for line in land:
    words = split_line(line.strip())
    for word in words:
        land_words.append(word.upper())
land_words.sort()

glass = open("AliceThroughTheLookingGlass.txt")


for line in glass:
    line_num += 1
    words = split_line(line.strip())
    for word in words:
        found = False
        lower_bound = 0
        upper_bound = len(land_words) - 1
        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if land_words[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif land_words[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print(line_num)
            print(word.upper())
land.close()
glass.close()