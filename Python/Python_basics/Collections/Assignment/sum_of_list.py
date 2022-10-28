
list_of_num = [2,3,16,12,-3,2,5]

# maximum number
max_num = 0
for num in list_of_num : 
    if num > max_num:
        max_num = num

print("Maximum number : ", max_num)

# sum of numbers in the list
list_sum = 0
for num in list_of_num:
    list_sum += num

print("sum of numbers : ", list_sum)

# reverse a list
list_reverse = []
print("Original List : ", list_of_num)
for postion in range(len(list_of_num), 0, -1):
    index = postion - 1
    print("index : ", index)
    list_reverse.append(list_of_num[index])
    # list_reverse.append(list_of_num[postion-1])

print("Reverse of the list : ", list_reverse)

# second largest number in the array 
largest_num = min(list_of_num)
second_largest = None

for num in list_of_num:
    if num > largest_num:
        second_largest = largest_num
        largest_num = num
    else:
        if second_largest < num:
            second_largest = num

print("Second largest number : ", second_largest)



