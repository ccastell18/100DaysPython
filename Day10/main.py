import math

def add(a, b):
  return a+b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def divide(a, b):
  return a/b

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": divide
}

def calculator():
  is_calculating = True
  num1 = float(input("What is the first number? "))

  while is_calculating is not False:

    num2 = float(input("What is the second number? "))
    for symbol in operations:
      print(symbol)

    operation_symbol = input("Pick a symbol from the list above: ")

# if operation_symbol == "+":
#   answer = add(num1, num2)
# elif operation_symbol == "=":
#   answer = sub(num1, num2)
# elif operation_symbol == "*":
#   answer = mult(num1, num2)
# else:
#   answer = divide(num1, num2)
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    again = input("Type 'y' to continue calculating or 'n' to start a new calculation. " )

    if again == 'y':
      num1 = answer
      continue

    else:
      is_calculating  = False
      calculator()

calculator()
      