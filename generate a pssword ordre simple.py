import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("****************welcome to the password generater*****************")

letters_num = int(input("how many latters u want in ur password : "))
numbers_num = int(input("how many numbers u want in ur password :"))
symbols_num = int(input("how many symbols u want in ur password :"))  #here is a impel project to generate a password just the beginning

password = ""

for count in range(0,letters_num) :
    letter_num = random.randint(0,52)   # simpel idea and good project 
    password += letters[letter_num]

for count in range(0,numbers_num) :
    number_num = random.randint(0,9)
    password += numbers[number_num]

for count in range(0,symbols_num) :
    symbol_num = random.randint(0,8)
    password += symbols[symbol_num]

print("your password is : ",password)
