MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

count = True
money = 0

def show_resources() :
    print(f"water : {resources['water']}ml") 
    print(f"milk : {resources['milk']}ml")
    print(f"coffee : {resources['coffee']}g")
    print(f"money : ${money}")

def are_resources_enough(drink_base):
    for counter in drink_base :
        if drink_base[counter] > resources[counter] :
            print(f"Sorry there is no enough {counter}")
            return False
    return True

def total_of_coins():
    quarters = int(input("how many quarters : "))
    dimes = int(input("how many dimes : "))
    nickels = int(input("how many nickels : "))
    pennies = int(input("how many pennies : "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total

def are_coins_enough(coins_base) :
    if payement < coins_base :
        print("Sorry no enough payment")
        return False
    return True

def rduice_resorces(drink_base):
    for counteur in resources :
        resources[counteur] -= drink_base[counteur]

def give_change(x,y):
    change = round(x - y,2)
    print(f"ur change is : ${change}")
    print(f"take ur {choice} please, SEE U LATER ")

while count :
    choice = input("What would u like? (espresso/latte/capuccino) : ")
    if choice == "off" :
        count = False 
    elif choice == "report" :
        show_resources()
    else : 
        drink = MENU[choice]
        drink_base = drink["ingredients"]
        coins_base = drink["cost"]
        if are_resources_enough(drink_base):
            payement = total_of_coins()  
            if are_coins_enough(coins_base):
                give_change(payement,coins_base)
                money+= coins_base
                rduice_resorces(drink_base)

    
