import random

#constants
TURN_LIMIT = 12

#setup colors
easy_colors = ["red", "blue", "green", "yellow"] 
hard_colors = ["red", "blue", "green", "yellow", "black", "white"]

def main():
    run = True
    while run:
        print("Welcome to Mastermind!")
        hear_rules()
        computer_code = computer_choices()
        turn = 1
        while turn <= TURN_LIMIT:
            player_code = player_choices()
            get_correct_answers(computer_code, player_code)
            if player_code == computer_code:
                turn = TURN_LIMIT
                print("YOU WIN, CONGRATULATIONS!!!")
            else:
                turns_remaining = TURN_LIMIT - turn
                if turns_remaining == 0:
                    print(computer_code)
                    print("Sorry you lost, Better luck next time!")
                else:
                    print(turns_remaining, "turns remaining!")
            turn += 1
        run = play_again()
    
    
    

def hear_rules():
    rules = input("Would you like to see the rules?\n")
    while (rules != "yes") and (rules != "no"):
        rules = input("Please enter yes or no for rules.\n")
    if rules == "yes":
        print("You are trying to break a color code hidden by the computer.")
        print("You will be asked to enter colors, 4 for easy, or 6 for hard.")
        print("You will then be given a list of colors.")
        print("These colors will be black or white, representing correct answers.")
        print("If black, you have a correct color in correct place.")
        print("If white, you have a correct color in the wrong place.")
        print("These are not necessarily given in the correct order.")
        print("You will have 12 guesses to break the code. Good Luck!")

def computer_choices():
    code = []
    for color in range(4):
        rand_numb = random.randint(0, 3)
        code.append(easy_colors[rand_numb])
    return code

def player_choices():
    player_choices = []
    print("Choose 4 colors from red, blue, yellow, or green")
    for choice in range(4):
        player_choice = input("Choice: ")
        while (player_choice != "red") and (player_choice != "blue") and (player_choice != "yellow") and (player_choice != "green"):
            print("Please enter red, blue, yellow, or green")
            player_choice = input("Choice: ")
        player_choices.append(player_choice)
    return player_choices
    
def get_correct_answers(computer, player):
    correct_answers = []
    new_computer = [] 
    new_player = []
    doubles = []
    for index in range(len(computer)):
        if computer[index] == player[index]:
            correct_answers.append("black")
        else:
            new_computer.append(computer[index])
            new_player.append(player[index])
    for index in range(len(new_computer)):
        for i in range(len(new_computer)):
            if new_computer[i] == new_player[index]:
                if new_player.count(new_player[index]) > 1:
                    doubles.append(new_player[index])
                    if doubles.count(new_player[index]) == new_computer.count(new_player[index]):
                        correct_answers.append("white")
                else:
                    correct_answers.append("white")
                    break
    print(correct_answers)
    
def play_again():
    keep_playing = input("Would you like to keep playing?\n")
    while (keep_playing != "yes") and (keep_playing != "no"):
        keep_playing = input("Please enter yes or no.\n")
    if keep_playing == "yes":
        run = True
    else:
        run = False
    return run

        
main()