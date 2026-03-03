print("Let's play Rock Paper and Scissors")
while True:
    player1= input("Enter your choice ")
    player2 = input("Enter your choice ")
    while input == "Rock" or "Paper" or "Scissors":
        if player1 == "Rock" and player2 == "Scissors":
            print("Player 1 is Winner")
            break            
        elif player1 == "Paper" and player2 == "Scissors":
            print("Player 2 is Winner")
            break            
        elif player1 == "Rock" and player2 == "Paper":
            print("Player 1 is Winner")
            break            
        elif player1 == "Scissors" and player2 == "Rock":
            print("Player 2 is Winner")
            break  
        elif player1 == "Paper" and player2 == "Rock":
            print("Player 2 is Winner")
            break
        elif player1 == player2:
            print("Match is draw")        
    new = input("Do you want a new game,Y or N: ")
    if new == "Y":
        continue
    else:
        print("Game Over")
        break
   
    

    




