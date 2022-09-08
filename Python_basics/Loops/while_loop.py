# thread mill example

initial_no_of_bags = 125

while (initial_no_of_bags > 0):
    print("The number of bags remaining : ", initial_no_of_bags)
    picked_up_bags = int(input("Enter the bags picked up : "))
    if picked_up_bags <= initial_no_of_bags : 
        initial_no_of_bags -= picked_up_bags