from operator import indexOf
from tkinter.messagebox import YES


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(plain_text, shift_amount):
#   cypher_text = ''
#   for letter in plain_text:
#     new_letter = alphabet[alphabet.index(letter) +shift_amount]
#     cypher_text += new_letter
#   print(f"Your encrypted word is {cypher_text}")

# def decode(cypher_text, shift_amount):
#   plain_text = ''
#   for letter in cypher_text:
#     new_letter = alphabet[alphabet.index(letter) - shift_amount]
#     plain_text += new_letter
#   print(f"Your decoded word is {plain_text}")

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ''
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
    
      new_position = position + shift_amount
      end_text += alphabet[new_position] 
    else:
      end_text += char
  print(f"The {cipher_direction}d text is {end_text}")
  


play = True
while play:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  result = input("Type 'yes' to continue playing and 'no' to stop?\n")
  if result == "no":
    play = False

