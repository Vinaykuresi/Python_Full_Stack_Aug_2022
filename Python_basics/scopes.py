
# global scope
num = 30

def add():
    # local scope
    num_1 = 20
    print("Addition of Numbers : ", num+num_1)

def sub():
    # local scope
    num_2 = 20
    print("Subtraction of Numbers : ", num-num_2)

add()

sub()

print("Multiplication of Numbers : ", num*num)
