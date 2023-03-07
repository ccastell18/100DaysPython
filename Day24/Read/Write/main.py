# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("my_file.txt", mode='w') as file:
#     file.write("More Text")

with open('my_file.txt', mode='a') as file:
    file.write("Even more text")