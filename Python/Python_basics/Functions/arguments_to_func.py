
# pass by value
def add(num1, num2):
    num1 = 30
    # sum = num1 + num2
    # print("Sum of the numbers : ", sum)

num_1 = 10
num_2 = 20

print(num_1)

add(num_1, num_2)

print(num_1)

# pass by reference
fruits = ["apples", "oranges", "dragon"]

def add_fruits(fruit_basket):
    fruit_basket.append("kiwi")

print(fruits)

add_fruits(fruits)

print(fruits)