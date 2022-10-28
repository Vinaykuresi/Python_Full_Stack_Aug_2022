import math

# input
base_of_the_traingle = 3
height_of_the_traingle = 4

# process(Hypotenuse)
hypotenuse = math.sqrt(base_of_the_traingle * base_of_the_traingle + height_of_the_traingle * height_of_the_traingle)
# print(math.pow(base_of_the_traingle, 3))

# process(Area)
area = 1/2*(base_of_the_traingle * height_of_the_traingle)

# output
print("Hypotenuse of the traingle with base : ", base_of_the_traingle, " and height : ", height_of_the_traingle, " is : ", int(hypotenuse))

print("Area of the traingle with base : ", base_of_the_traingle, " and height : ", height_of_the_traingle, " is : ", int(area))