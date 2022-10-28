
num_list = [2, 3, 4, 5, 2, 4, 6, 7, 2, 3]

print("List : ", num_list)

print("Set : ", set(num_list))

num_set = {10, 20, 10, 5, 2, 30, 40, 20, 10, 30, 25, 40}

# intersection
print(set(num_list) & num_set)

# union
print(set(num_list) | num_set)

# subet of A
print(set(num_list) - num_set)
