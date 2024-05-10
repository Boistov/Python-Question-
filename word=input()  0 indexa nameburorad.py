












#word=input()
#for i in range(1, len(word)):
#    print(word[i], end="")



#def calculate_basketball(a, b):

#    total = (a * 2) + (b * 3)
#    return total

#point1 = int(input())
#point2 = int(input())

#sum = calculate_basketball(point1, point2)
#print(sum)







#def check_lists(list1, list2):

#    if len(list1) != len(list2):
#        return False

#    for i in range(len(list1)):
#        if list1[i] != list2[i]:
#            return False

#   return True

#list_a = input()
#list_b = input()

#print(check_lists(list_a, list_b))








#def sum_of(n):
#    if n == 1:
#        return 1
#    else:
#        return 1 / n + sum_of(n - 1)

#n = int(input("Enter ->"))
#sum = (n)
#print(sum)





#import datetime

#time1 = input()
#time2 = input()
#try:
#    a = datetime.datetime.strptime(time1, "%H:%M:%S")
#    b = datetime.datetime.strptime(time2, "%H:%M:%S")

#    time_delta = end_time - start_time

#    total_seconds = time_delta.total_seconds()
#    hours_passed = total_seconds / 3600  # 3600 seconds in an hour

#    print(f"Hours passed between {time1} and {time2}: {hours_passed:.2f} hours")
#except ValueError:# print("Invalid time format. Please use HH:MM:SS.")






#numbers = [1,2, 3, 4, 6, 7, 8, 10]

#n1 = sum(range(1, 11))
#n2 = sum(numbers)

#total = n1 - n2

#print(total)








#from datetime import datetime

#year= input()
#month = input()
#a1 = input()

#total = a + a1

#n = month + (total // 12)
#sum = total % 12
#print(sum)




# Print the result



def squared(num):
    result = ""
    for i in num:
        squared = int(i) **2
        squared +=str(squared)
    return  result

number = input("Enter:")
result = squared(number)
print(result)


