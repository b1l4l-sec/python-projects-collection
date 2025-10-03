import random 

print("************************rock paper scissors game *************************")
winner = False

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)                                        
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while winner == False :
    your_choise = int(input("enter 1 for rock 2 for paper and 3 for scissors :"))
    boot_choise = random.randint(1,3)

    if your_choise == 1 :
        print("you : \n")
        print(rock)

    if boot_choise == 1 :
        print("boot : \n")
        print(rock)

    if your_choise == 2 :
        print("you : \n")
        print(paper)

    if boot_choise == 2 :
        print("boot : \n")
        print(paper)

    if your_choise == 3 :
        print("you : \n")
        print(scissors)

    if boot_choise == 3 :
        print("boot : \n")
        print(scissors)

    for i in range(1,4):
        if your_choise == i and boot_choise == i :
            print("no winner choose again")
            winner = False
    
    if your_choise == 1 and boot_choise == 2 :
        print("you lose")
        winner = True
    
    if your_choise == 1 and boot_choise == 3 :
        print("you win")
        winner = True

    if your_choise == 2 and boot_choise == 1 :
        print("you win")
        winner = True

    if your_choise == 2 and boot_choise == 3 :
        print("you lose")
        winner = True

    if your_choise == 3 and boot_choise == 1 :
        print("you lose")
        winner = True
    
    if your_choise == 3 and boot_choise == 2 :
        print("you win")
        winner = True
