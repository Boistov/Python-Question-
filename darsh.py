def find_relation(name):
    relations = {
        "Darth Vader": "Father",
        "Leia": "Sister",
        "Han": "Brother-in-law",
        "R2D2": "Droid"
    }

    if name in relations:
        return relations[name]
    else:
        return "Wrong"




import random

list1 = []

for _ in range(6):
    random_int = random.randint(10, 30)
    list1.append(random_int)

print(list1)





