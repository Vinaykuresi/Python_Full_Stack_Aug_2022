
num_tuple = (1, 2, 3, 4, 5)
print(type(num_tuple))

# random access
print(num_tuple[2])

# random write
# num_tuple[2] = 10

#unpacking the elements
num1, num2, num3, num4, num5 = num_tuple

print(num2)

# length of the list
print(len(num_tuple))

# append some value to the tuple
num_tuple = num_tuple + (6,)
print(num_tuple)