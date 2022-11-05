
fruits = ['apple', 'mango', 'banana', 'cherry']

new_fruit_list = []

for fruit in fruits:
    if 'a' not in fruit:
        new_fruit_list.append(fruit)

print(new_fruit_list)

new_fruit_list = [fruit for fruit in fruits if 'a' in fruit]
print(new_fruit_list)

new_fruit_list = [fruit if 'a' in fruit else "orange" for fruit in fruits ]
print(new_fruit_list)
