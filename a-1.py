users = ["Bob", "Tom", "Ken"]
int_numbers = [1, 5]
bob_info = ["Bob", "Dylan", 79]
members = ["Bob", "Tom", "Ken"]
print(members[0])
print(members[1])

bob_info = ["Bob", "Dylan", 79]
print(f"Name: {bob_info[0]} {bob_info[1]}, Age: {bob_info[2]}")

odd_numbers = [1, 3, 5, 7, 9]
for odd in odd_numbers:
    print(odd)
even_numbers = [2, 4, 6, 8]
for number in even_numbers:
    print(number * 2)
users_info = [["Bob", 79],
              ["Tom", 59],
              ["Ken", 61]]
for user in users_info:
    name = user[0]
    age = user[1]
    print(f"Name: {name}, Age: {age}")

bob_info = {"first_name":"Bob", "family_name":"Dylan","age":79}

print(bob_info["first_name"]) # "Bob"
print(bob_info["family_name"]) # "Dylan"
print(bob_info["age"]) # 79

import random

def dice():
    return random.randint(1, 6)
print(dice())