



# Notes - Formatting Numbers

import random


# round function round(n, decimal digits)
print(round(32323.1415, 2))

# format method (string method)
a = 2342439
b = 342.2342434
print("My Number is {}".format(a))  # {} is the formatted number "a"
print("My Number is {:.3f}".format(b))  # {:.3f} 3 decimals as a float
print("My Number is {:,}".format(a))  # {:,} with commas
print("My Number is {} and {}".format(a, b))  # places them sequentially unless otherwise specified
print("My Number is {1:.3f} and {0:,}".format(a, b))  # otherwise specified with index


# order:spaceholder+justification+width+commas+precision+datatype+notation
# (Search online for help)

# Fixed Width
for i in range(20):
    c = random.randrange(10000)
    print("${:10}".format(c))  # lines up right side to the "10" index character

# Justification (^ is center < is left > is right)
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:^12}dollars".format(c))

# Adds Commas
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:12,}".format(c))


# precision (f float, d dec/int, b binary)
for i in range(20):
    c = random.random()
    print("{:<11.5f}".format(c))

for i in range(20):
    c = random.randrange(1000)
    print("{:b}".format(c))  # b for binary
for i in range(20):
    c = random.randrange(1000)
    print("{:f}".format(c))  # f for float
for i in range(20):
    c = random.randrange(1000)
    print("{:d}".format(c))  # d for dec/int

# scientific notation
for i in range(20):
    c = random.random()
    print("{:.2e}".format(c))  # scientific notation to two decimals

