



# Notes - Exceptions (use me sparingly)
# Exception - a condition that results in abnormal pregrom flow
# Exception handling - What we actively do to accommodate exceptions
# Throw/Raise - Exception condition occurs
# Catch - Code handles thrown exception
# Unhandled Exception - Thrown not caught. Program killer




# Divide By Zero (ZeroDivisionError)
x = 2
y = 0
try:
    print(x / y)
except:
    print("Invalid Operation")

# Conversion Error (Value Error)
try:
    int("T")
except:
    print("Number Was Not Valid")

# Handle With a Loop
done = False
while not done:
    try:
        user_input = int(input("Enter an integer: "))
        done = True
    except:
        print("Number is not Valid")

# File Opening (IOError, FileNotFoundError)
try:
    file = open("YaBoi.txt")
except:
    print("Could Not Open File")

# Use Built in Error types for python to check what error ocurred
try:
    # my_file = open("Yagirl.txt")
    # int("Hello")
    print(1 / 0)
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print("Invalid Conversion")
    print(e)
except ZeroDivisionError as e:
    print("Error", e)












