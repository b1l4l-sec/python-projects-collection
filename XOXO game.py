lane1 = [" "," "," "]  
lane2 = [" "," "," "]
lane3 = [" "," "," "]
winner = False
objet = "X"
i = 0

map = [lane1,lane2,lane3]

print(f"{lane1} \n{lane2} \n{lane3}")

while winner == False :
    cordonee = input("entrer votre cordonner (set -1 to exit) : ")   
    if cordonee == "-1" :
        winner = True
    else : 
        cord_lane = int(cordonee[0])-1  #str not int but i transformed str to int
        cord_col = int(cordonee[1])-1

        if i % 2 == 0 :
            objet = "X"                        
        else :
            objet = "O"
            
        selected_lane = map[cord_lane]     
        selected_lane[cord_col] = objet
        i=i+1
        print(f"{lane1} \n{lane2} \n{lane3}")

        for j in range(0,2) :
            if (map[j][0] == "X" and map[j][1] == "X" and map[j][2] == "X") or (map[j][0] == "O" and map[j][1] == "O" and map[j][2] == "O"):
                winner = True
                print(f"the user of {objet} is the winner GG ")

            if (map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X") or (map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O"):
                    winner = True
                    print(f"the user of {objet} is the winner GG ")

            if (map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X") or (map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O"):
                    winner = True
                    print(f"the user of {objet} is the winner GG ")

            if (lane1[0] == "X" and lane2[0] == "X" and lane3[0] == "X") or (lane1[0] == "O" and lane2[0] == "O" and lane3[0] == "O") :
                winner = True
                print(f"the user of {objet} is the winner GG")

            if (lane1[1] == "X" and lane2[1] == "X" and lane3[1] == "X") or (lane1[1] == "O" and lane2[1] == "O" and lane3[1] == "O") :
                winner = True
                print(f"the user of {objet} is the winner GG")

            if (lane1[2] == "X" and lane2[2] == "X" and lane3[2] == "X") or (lane1[2] == "O" and lane2[2] == "O" and lane3[2] == "O") :
                winner = True
                print(f"the user of {objet} is the winner GG")


print("\n************** GOOD BYE TRY LATER ***********************\n")


#WHAT IF I WANTED TO STOP DURING PLAYING THIS GAME 
# I HAVE A SOLUTION TO DO FOLLOW ME 
