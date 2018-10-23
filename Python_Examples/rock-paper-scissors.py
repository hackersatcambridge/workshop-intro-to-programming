# A rock-paper-scissors game
import random

class Computer:
    def __init__(self, name):
        self.name = name
        self.moves = ["r", "p", "s"]
        self.move = ""
    def makeMove(self):
        rn = random.randint(0, 2)
        self.move = self.moves[rn]
        return self.move

#number of rounds
rounds = 3
current_round = 0
user_score = 0
computer_score = 0

#Initialise the computer
computer = Computer("Master")

while(current_round < rounds):
    user_input = input("Your move (r, p or s?): ")
    while(user_input not in ["r", "p", "s"]):
        user_input = input("Please choose from (r, p or s): ")
    computer_move = computer.makeMove()
    print(computer.name + "'s Move: " + computer_move)

    if(user_input == computer_move):
        print("Draw! Replay the move!")
    elif(user_input == "r"):
        if(computer_move == "p"):
            print(":( the computer won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
        else:
            print(":) You won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
    elif(user_input == "p"):
        if(computer_move == "s"):
            print(":( the computer won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
        else:
            print(":) You won that round!")
            current_round = current_round + 1
            user_score = user_score + 1
    else:
        if(computer_move == "r"):
            print(":( the computer won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
        else:
            print(":) You won that round!")
            current_round = current_round + 1
            user_score = user_score + 1

print("Computer: ", computer_score)
print("User: ", user_score)



    