
'''
*
**
***
****
*****
'''

rows = int(input("Enter the no of rows : "))

print("Sequence : ", list(range(rows)))
for row in range(rows):
    for col in range(row+1):
        print("*", end="")
    print("\n")

# count = 1
# while (rows > 0):  
#     col = count
#     while((col) > 0):
#         print("*", end="")
#         col -= 1
#     rows -= 1
#     count += 1
#     print("\n")

row = 0
while (row < rows):  
    col = 0
    while(col < row+1):
        print("*", end="")
        col += 1
    row += 1
    # count += 1
    print("\n")


# rows = 5
# count = rows
# while (rows > 0):  
#     col = count
#     while((col) > 0):
#         print("*", end="")
#         col -= 1
#     rows -= 1
#     count -= 1
#     print("\n")

row = 0
while (row < rows):  
    col = 0
    while(col < rows-row):
        print("*", end="")
        col += 1
    row += 1
    print("\n")

# Assignment : 

'''
*****
****
***
**
*
'''

'''
     *
    **
   ***
  ****
 *****
'''
'''
 *****
  ****
   ***
    **
     *
'''

rows = int(input("Enter the no of rows : "))

space = 1
for row in range(rows):
    for col in range(rows - space):
        print(" ", end="")
    for col in range(row+1):
        print("*", end="")
    space += 1
    print()