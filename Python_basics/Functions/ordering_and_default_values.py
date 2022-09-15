

# positions
def add(num1, num2):
    print(num1)
    print(num2)


add(10, 20)

print()

# keywords
def add(num1, num2):
    print(num1)
    print(num2)

add(num2=10, num1=20)

print()

# default
def add(num1, num2=20):
    print(num1)
    print(num2)

add(10)

# variable argument count
def add(num1, num2, *num3):
    print(num1)
    print(num2)
    print(num3)

add(10, 20, 30, 40)


