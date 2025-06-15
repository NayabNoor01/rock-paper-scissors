import sys
import random
wins=0
losses=0
ties=0
print("ROCK,PAPER,SCISSORS")
while True:
    print("wins",wins,"losses",losses,"ties",ties)
    while True:
       player1=input("Enter rock,paper or scissors >>  ")
       if player1=='Quit':
        print("The game Ends")
        sys.exit()
       elif player1=='Rock' or player1=='Paper' or player1=='Scissors':
        break
    if player1=='Rock':
        print("Rock verses ...")
    elif player1=='Paper':
        print("Paper verses ...")
    elif player1=='Scissors':
        print("Scissors verses ...")
   
    player2=random.randint(1,3)
    if player2==1:
       computermove='Rock'
       print("Rock")
    if player2==2:
       computermove='Paper'
       print("Paper")
    if player2==3:
       computermove='Scissors'
       print("Scissors")
       # first condition
    if player1==computermove:
        print("Its a tie")
        ties=ties+1
        #second condition
    elif player1=='Rock' and computermove=='Scissors':
        print("Player1 wins")
        wins=wins+1
    elif player1=='Scissors' and computermove=='Rock':
        print("Computer wins")
        losses=losses+1
        #third conditiion
    elif player1=='Paper' and computermove=='Rock':
        print("Player1 wins")
        wins=wins+1
    elif player1=='Rock' and computermove=='Paper':
        print("computer wins")
        losses=losses+1
        # 4th condition
    elif player1=='Rock' and computermove=='Scissors':
        print("Player1 wins")
        wins=wins+1
    elif player1=='Scissors' and computermove=='Paper':
        print("Computer wins")
        losses=losses+1
    elif player1=='Paper' and computermove=='Scissors':
        print("Player1 wins")
        wins=wins+1
  
  
    
        
    
    
        

   
