# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:

# F = G * (m1 * m2) / r**2

# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.


done = False
while not done:
    try:
        mass_1 = int(input("Enter \"Mass 1\" in kg: "))
        mass_2 = int(input("Enter \"Mass 2\" in kg: "))
        distance = int(input("Enter \"The Distance Between The Two Objects\": "))
        force = 6.67e-11 * mass_1 * mass_2 / (distance / 2) ** 2
        print("{:.2e}".format(force))
        done = True
    except ValueError:
        print("Please Try Again and Enter In The Correct Format.")
    except ZeroDivisionError:
        print("Please Don't Not Enter As Value Of Negative Or \"0\"")



