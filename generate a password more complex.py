import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("****************welcome to the password generator*****************")

letters_num = int(input("how many latters u want in ur password : "))
numbers_num = int(input("how many numbers u want in ur password :")) # this the better version of generating password for now 
symbols_num = int(input("how many symbols u want in ur password :"))

password = ""
counter = 0
sizeofpassword = letters_num + numbers_num + symbols_num

while counter < sizeofpassword :
    random_num = random.randint(1,3) 
    match random_num :
        case 1 :
            letter_num = random.randint(0,52)
            password += letters[letter_num]
        case 2 :
            number_num = random.randint(0,9)
            password += numbers[number_num]
        case 3 :
            symbol_num = random.randint(0,8)
            password += symbols[symbol_num]
    counter = counter + 1

print("your password is : ",password)
