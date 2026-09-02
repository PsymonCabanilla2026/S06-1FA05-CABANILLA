
# Reflection:
# Using a math library is way easier than writing formulas from scratch because I do not have to create complex math functions on my own.
# Using sqrt() and pow() saved a lot of time and made my program shorter and less confusing.
# Without these built-in functions, calculating the distance formula would take way more lines of code and be very hard to write.


import math

# Step 1: Get input numbers from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Step 2: Calculate using math library functions
x_part = math.pow(x2 - x1, 2)
y_part = math.pow(y2 - y1, 2)
distance = math.sqrt(x_part + y_part)

# Step 3: Display the result
print("The distance between the two points is:", distance)