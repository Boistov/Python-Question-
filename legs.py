def legs_calculate(chickens, cows, pigs):
    sum_legs = 0

    for  i in range(chickens):
        sum_legs += 2
    for i in range(cows):
        sum_legs += 4
    for i in range(pigs):
        sum_legs += 4
    return sum_legs

chickens = int(input())
cows = int(input())
pigs = int(input())

sum_legs = legs_calculate(chickens, cows, pigs)
print(sum_legs)












def calculate_list(list1, list2):
    return list(set(list1) - set(list2))


list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
difference_result = calculate_list_difference(list1, list2)
print(difference_result)
