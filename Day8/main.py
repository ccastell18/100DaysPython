from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(ch, num, dir):
  cipher_text = ""
  for char in ch:
    if char in alphabet:
      position = alphabet.index(char)
      new_letter = alphabet[0]
      encode_position = position + num
      decode_position = position - num
      if dir == 'encode':
        new_letter = alphabet[encode_position]
        cipher_text += new_letter
      else:
        new_letter = alphabet[decode_position]
        cipher_text += new_letter
        
  print(f"The {dir}d text is {cipher_text}")

should_continue = True
while should_continue is True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(text, shift, direction)

  keep_going = input("Type yes if you want to continue. Else type no.").lower()

  if keep_going == 'no':
    should_continue = False
