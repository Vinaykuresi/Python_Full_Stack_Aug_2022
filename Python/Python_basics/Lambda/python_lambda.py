
'''

    Python Lambda : 

        small anonymous function.

        lambda function :

            can take any no of arguments
            But can only have one expression.

        use them as an anonymous function inside another function
'''

add = lambda a : a + 10
print(add(10))

mul_two_nums = lambda a, b : a * b
print(mul_two_nums(10, 20))

def myFunc(num):
    return lambda multiply : num * multiply

ten_multiplied = myFunc(5)
print(ten_multiplied(10))
print(ten_multiplied(15))