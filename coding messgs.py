letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
choice = 'y'

"""
def encode() :
    mssg_encoded = ""
    mssg_to_encode = input("enter ur message please  : ").lower()  
    num_jump = int(input("enter the shift number : "))
    for letter in mssg_to_encode :
        position = letters.index(letter)
        new_pos = position + num_jump
        mssg_encoded += letters[new_pos]
    print("the result is : ",mssg_encoded)

def decode() :
    mssg_decoded = ""
    mssg_to_decode = input("enter ur message please  : ").lower()
    num_jump = int(input("enter the shift number : "))
    for letter in mssg_to_decode :
        position = letters.index(letter)
        mssg_decoded += letters[position-num_jump]
    print("the result is : ",mssg_decoded)

while(choice == "yes") :
    type = input("enter 'encode' or 'decode' : ")
    match type :
        case "encode" : encode()
        case "decode" : decode()
        case _: print("Error, choose juste encode or decode********** ")    
    choice = input("to restart enter 'yes', to end enter 'no' : ")
"""
# this is one of the projects that i worked on a& i found it too funny :>    let's see ...........
def caesor():
    mssg_analysed = ""
    type = input("enter 'encode' or 'decode' : ")
    mssg_to_analyse = input("enter ur message please  : ").lower()
    num_jump = int(input("enter the shift number : "))
    for letter in mssg_to_analyse :
        position = letters.index(letter)
        match type :
            case "encode"  : 
                new_pos = position + num_jump
            case "decode" : 
                new_pos = position - num_jump
            case _: print("choose just encode or decode M.F")
        mssg_analysed += letters[new_pos]
    print("the final result is ",mssg_analysed)

while choice == 'y' :
    caesor()
    choice = input("to restart enter 'y', to end enter 'n' : ")

#print("END /_\ ")


    


