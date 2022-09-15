import json

# # person details
person_detail = ["Krishna", 19, "Bsc", "Junior Software Developer"]
print(person_detail[0])

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

print(person_details["name"])
print(person_details["personal_details"]["phone_no"])

person_details["personal_details"]["phone_no"] = 9121817125

#updating dictionary
print(person_details)

#accessing dictionary key
print(list(person_details.keys()))

for key in person_details:
    print(key, " : ", person_details[key])

# accessing only value
for value in person_details.values():
    print(value)

shallow_personal_details = dict()

# recursion -> creating a shallow copy of nested dictionary
def recursion(person_details):
    if(type(person_details) == dict):
        for key in list(person_details.keys()):
            if(type(person_details[key]) != dict):
                shallow_personal_details[key] = person_details[key]
                print(key, " : ", person_details[key])
            if(type(person_details[key] == dict)):
                recursion(person_details[key])


recursion(person_details)

# original Dicitonary
# print(person_details)
print(json.dumps(person_details, indent=4))

print()
# shallow Dictionary
# print(shallow_personal_details)
print(json.dumps(shallow_personal_details, indent=4))








