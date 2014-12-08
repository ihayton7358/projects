import time, random

rock = 1
paper = 2
scissors = 3

names = {rock: "rock", paper: "paper", scissors: "scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start ():
    print ("Let's play a game of rock, paper, scissors!")
    while game():
        pass
    scores

def game():
    player = move()
    computer = random.randint(1,3)
    result (player,computer)
    return play_again()
    
def move ():
    while True:
        print  
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move:")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print ("OOps, I didn't understand that. Please enter 1, 2 or 3.")

def result (player, computer):
    print ("1...")
    time.sleep(1)
    print ("2...")
    time.sleep(1)
    print ("3!!!")
    time.sleep(0.5)
    print ("Computer chose {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print ("It's a tie!")
    else:
        if rules[player] == computer:
            print ("You laugh evilly at the computers defeat")
            player_score += 1
        else:
            print ("The computer laughs evilly at your defeat")
            computer_score +=1

def play_again():
    answer = input ("Would you like to play again? y/n:")
    if answer in ("yes","Yes","y","Y"):
        return answer
    else:
        print ("Thanks for playing")
        scores()
        
def scores():
    global player_score, computer_score
    print ("The scores are...")
    print ("Player:", player_score)
    print ("Computer:", computer_score)


if __name__ == '__main__':
    start()
                        
