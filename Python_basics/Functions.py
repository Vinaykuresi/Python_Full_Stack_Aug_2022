import math

def add(num1, num2):
    sum = num1+num2
    return sum

def hypotenuse_of_rgt_traingle(base, height):
    hypotenuse = math.sqrt(base*base + height*height)
    return hypotenuse

hypotenuse = hypotenuse_of_rgt_traingle(3, 4)

print("Hypotenuse of traingle is : ", int(hypotenuse))

# result1 = add(10, 20)
# result2 = add(result1, 50)

# print("The addition of Two numbers is : ", result1)

# print("The addition of Two numbers is : ", result2)