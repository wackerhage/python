#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#criei uma lista para conseguir dar a funcao shuffle nos simbolos, numeros e letras
password = []
x = 0
y = 0
z = 0
#criei loopings para randomizar a escolha do input e adicionar randomicamente quantas vezes necessario
for x in range(nr_letters):
   random_letter = random.choice(letters)
   password += random_letter
for y in range(nr_symbols):
   random_symbol = random.choice(symbols)
   password += random_symbol
for z in range(nr_numbers):
   random_number = random.choice(numbers)
   password += random_number

#utilizei o shuffle para embaralhar todos os itens e apos isso transformei em string
random.shuffle(password)
password_string = ''.join(password)
print(f"Your password is: {password_string}")
  
   

