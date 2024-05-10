
#my_list = [1, 2, 3, 5, 4, 5, 3, 2]
#minimum = 0

#for i in range(1, len(my_list)):
 #   if my_list[i] < my_list[minimum]:
#        minimum = i

#print( minimum)

#my_list = [1, 2, 3, 5, 4, 5, 3, 2]
#minimum = min(my_list)
#print(minimum)



my_list = [1, 2, 3, 5, 4, 5, 3, 2]

minimum = my_list[0]

for num in my_list:
    if num < minimum:
        minimum = num

print(minimum)
