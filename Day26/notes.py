# list comprehension
numbers = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#
# new_list.append(add_1)

# refactor
# new_list = [new_item for n in list]

new_list = [n+1 for n in numbers]
print(new_list)