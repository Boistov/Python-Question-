def check_list(num, target):

    for i in num:
        if i == target:
            return True
    return False

my_list = [1, 2, 3, 4, 5]
list1 = int(input())

result = check_list(my_list,list1)
print(result)
