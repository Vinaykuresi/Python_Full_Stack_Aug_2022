

# Sum of all items in a dictionary

shallow_dict = {
    "num1" : 10,
    "num2" : 20,
    "num3" : 50
}

# shallow dictionary
shallow_addition = 0
for num in shallow_dict.values():
    shallow_addition += num

print("Sum of dictionary values : ",shallow_addition)


# nested dictionary
nested_dict = {
    "num1" : 10,
    "num2" : 20,
    "add" : {
        "num4" : 40,
        "add2" : {
            "num5" : 35,
            "num6" : 45
        }
    }
}

addition = 0

def recursion(person_details):
    global addition
    if(type(person_details) == dict):
        for key in list(person_details.keys()):
            if(type(person_details[key]) != dict):
                addition += person_details[key]
            if(type(person_details[key] == dict)):
                recursion(person_details[key])

recursion(nested_dict)

print("Sum of dictionary values : ",addition)

# lenght of the key value pairs in the dictionary
# # dictionary
person_details = {
    "name" : "Krishna",
    "age" : 19,
    "qualifcation" : "Bsc",
    "personal_details" : {
        "designation" : "Junior Software Developer",
        "phone_no" : 9154549566,
        "location" : "Bangalore",
        "additional_details" : {
            "mother" : "Jyothi",
            "father"  : "Raghu",
            "gender" : "male",
            "blood group" : "B+"
        }
    }
}

# 2. Find the size of a Dictionary in Python
# recursion -> creating a shallow copy of nested dictionary
count = 0

def recursion(person_details):
    global count
    if(type(person_details) == dict):
        for key in list(person_details.keys()):
            if(type(person_details[key]) != dict):
                count += 1
            if(type(person_details[key] == dict)):
                recursion(person_details[key])


recursion(person_details)
print("The size of key value pair in Dictionary : ",count)