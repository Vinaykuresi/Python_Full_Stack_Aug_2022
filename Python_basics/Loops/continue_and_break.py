
count = 0
# should allow paddanger in odd positions
for passager_id in 1001, 1002, 1003, 1004, 1005, 1006, 1007:

     # stop iterations if count is equal to 3
    if count == 3:
        break
        # pass
        
    if passager_id%2 == 1:
        count += 1
    else:
        print("Passangeer sent out : ", passager_id)

'''
break -> stops the iteration
pass -> continues the iteration
'''

print("The number passagers allowed : ", count)