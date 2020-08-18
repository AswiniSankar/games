import random
player1=input()
player2=input()
PlayerOne =player1
PlayerTwo =player2
player1score = 0
player2Score = 0


diceOne = [1, 2, 3, 4, 5, 6]
diceTwo = [1, 2, 3, 4, 5, 6]

def playDiceGame():

    for i in range(5):
      
        random.shuffle(diceOne)
        random.shuffle(diceTwo)
    firstNumber = random.choice(diceOne) 
    SecondNumber = random.choice(diceTwo)
    return firstNumber + SecondNumber

print("welcome to the Dice game\n")
n=int(input("how many times you both are want to play\n"))
for i in range(n):

    player1Number = random.randint(1, 100) 
    player2TossNumber = random.randrange(1, 101, 1) 
    if( player1Number > player2TossNumber):
        print(player1,"won the toss")
        player1Score = playDiceGame()
        player2Score = playDiceGame()
    else:
       print(player2,"won the toss")
       player2Score = playDiceGame()
       player1Score = playDiceGame()

    if(player1Score >player2Score):
        print (player1," is winner of dice game. " ,player1,"'s Score is:", player1Score, player2,"'s score is:", player2Score, "\n")
    else:
        print(player2, "is winner of dice game.", player2,"'s Score is:", player2Score, player1,"'s score is:", player1Score, "\n")



