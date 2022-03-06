the_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def start_game():
    global name1 
    name1= input("Player 1! What is your name?  ")
    print(f'Hi {name1}! You will play whit X!')
    name2 = input("Player 2! What is your name?  ")
    print(f'Hi {name2}! You will play whit O!')
    print(f"{name1} will start. Let's play! Have fun!")

    
def game():
    win1 = False
    win2 = False
    counter = 1
    while not (win1 or win2):
        if counter % 2 == 1:
            choice = input(f"{name1} it's your turn! Choose a number! (0-8)")
            if choice.isdigit():
                choice = int(choice)


            else:
                choice = input("Your input is invalid. Please try again.  ")
            

start_game()
game()
display_board(the_board)
