
#1. swapping the element positions
list_of_num = [20, 10, 30, 40, -3, -20, 10, -30]

list_of_num[3], list_of_num[0] = list_of_num[0], list_of_num[3]

print(list_of_num)

#2. element exists in a list : 
flag = False
for num in list_of_num:
    if num == 50:
        flag = True

if flag == True:
    print("Exists")
else : 
    print("Not Exists")

if 30 in list_of_num:
    print("Exists")
else:
    print("Not Exists")

#3. count positive and Negative numbers
positive_count = 0
negative_count = 0

for num in list_of_num:
    if num >= 0:
        positive_count += 1
    else:
        negative_count += 1

print("Positive count : ", positive_count)
print("Negative coint : ", negative_count)

