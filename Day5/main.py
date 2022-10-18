import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

list = []
password = ''

print("Welcome to the password generator!\n")
letter = int(input("How many letters would you like? "))
number = int(input("How many numbers would you like? "))
symbol = int(input("How many symbols would you like? "))

for x in range(0, letter):
  x = letters[random.randint(0, len(letters) -1)]
  list.append(x)

for x in range(0, number):
  x = numbers[random.randint(0, len(numbers) -1)]
  list.append(x)

for x in range(0, symbol):
  x = symbols[random.randint(0, len(symbols) -1)]
  list.append(x)

random.shuffle(list)

for x in list:
  password += x



print(password)