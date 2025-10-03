print("**************calculatrice avoncee**************\n\n")

operators = ["+","*","/","-"]
jump = False

def calculate(first_num , second_num) : 
    for count in operators :
        print(count)
    operator = input("choose an operator : ")
    match operator :
        case "+" : result = first_num + second_num
        case "-" : result = first_num - second_num
        case "*" : result = first_num * second_num
        case "/" :
            if second_num != 0 :
                result = first_num / second_num 
            else :
                print("impossible, i can't devide by  0 \n")
                jump = True
                return -1
        case _:
            print("u M.F why u re doing this get out of here M.F bad operator \n")
            jump = True
            return -1
    return result


first_num = int(input("enter the first number : "))
second_num = int(input("enter the second number : "))
result = calculate(first_num,second_num)
if jump == False :
    print("result = ",result)
    choice = input(" 'y'repete with second number or 'n' repete normaly : ")
else : 
    choice = "n"

while choice != "stop"  :
    if choice == "n" : 
       first_num = int(input("enter the first number : "))
       second_num = int(input("enter the second number : "))
       result = calculate(first_num,second_num)
       if jump == False :
            print("result = ",result)
            choice = input(" 'y'repete with second number or 'n' repete normaly : ")
       else : 
            choice = "n" 
    elif choice == "y" :
        first_num = result 
        second_num = int(input("enter the second num please : "))
        result = calculate(first_num,second_num)
        if jump == False :
            print("result = ",result)
            choice = input(" 'y'repete with second number or 'n' repete normaly : ")
        else : 
            choice = "n"
    else :
        ("y or n nothing else get out of here")

print("\n\nEND /_\ ")
