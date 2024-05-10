import random

lists = True
for i in range(len(list1)):
    if list1[i] != list2[i]:
        lists = False
        break

print(" not equal?")
if lists:
    print("equal.")
