'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''

from NBAStats import data

#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)

print(data.pop(0))

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)


def sortz(y):
    return sorted(y, key=lambda x: x[0])

pos = 0
my_list = []
for x in range(1, len(data)):
    pos += 1
    my_list.append([data[x][-1], pos])

for x in range(-10, 0):
    print(x * -1, data[sortz(my_list)[x][1]][2])


#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)

total = 0
for x in range(1, len(data)):
    pos += 1
    if data[x][2] == "Kobe Bryant":
        total += data[x][-1]

print(total)


#4  What player has the most 3point field goals in a single season. (3pts)

pos = 0
my_list = []
for x in range(1, len(data)):
    pos += 1
    my_list.append([data[x][-18], pos])

print(data[sortz(my_list)[-1][1]][2])

#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)

pos = 0
my_list = []
for x in range(1, len(data)):
    pos += 1
    my_list.append([data[x][26], pos])

print(data[sortz(my_list)[-1][1]][2])

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".

# "Who is the oldest player of all time?"

pos = 0
my_list = []
for x in range(1, len(data)):
    pos += 1
    my_list.append([data[x][5], pos])

print(data[sortz(my_list)[-1][1]][2])

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)


pos = 0
my_list = []
for x in range(1, len(data)):
    pos += 1
    my_list.append([data[x][-10], pos])

print("The Person With The Lowest Free Throw Percentage Is", data[sortz(my_list)[0][1]][2])
print("The Person With The Highest Free Throw Percentage Is", data[sortz(my_list)[-1][1]][2])
