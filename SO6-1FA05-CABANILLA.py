
import math

# Reflection:
# Using the math library makes the distance calculation easier
# because I do not have to create the math functions myself.
# The sqrt() and pow() functions make the code shorter,
# easier to understand, and faster to write.

# Get the coordinates of the two points from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the squared differences of the coordinates
x_difference = math.pow(x2 - x1, 2)
y_difference = math.pow(y2 - y1, 2)

# Calculate the distance using the distance formula
distance = math.sqrt(x_difference + y_difference)

# Display the final result
print("The distance between the two points is:", distance)
