import random

the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def start_game():
    name1= input("Player 1! What is your name?  ")
    name2 = input("Player 2! What is your name?  ")
    return [name1,name2]

def choose_marker(names):  
    loop = True
    while loop:
        marker1 = input(f"{names[0]} Choose your marker! X or O   ")
        if marker1 == 'X': 
            marker2 = 'O'
            loop = False
        elif marker1 == 'O': 
            marker2 = 'X'
            loop = False
        else: 
            print('Wrong character! Try again!')
            continue
    
    player1 = [names[0],marker1]
    player2 = [names[1],marker2]
    print(f"{player1[0]} you will play with {player1[1]}")
    print(f"{player2[0]} you will play with {player2[1]}")
    return [player1,player2]
        
def random_player():
    return random.randint(1,2)

def wich_player_begin(players):  
    first = []
    second = []
    if random_player()==1: 
        first = players[0]
        second = players[1]
    else: 
        first = players[1]
        second = players[0]
    return [first, second]    

def winner(orderedPlayers): 
    if ((the_board[1]==the_board[2]==the_board[3]==orderedPlayers[0][1])or
    (the_board[4]==the_board[5]==the_board[6]==orderedPlayers[0][1]) or
    (the_board[7]==the_board[8]==the_board[9]==orderedPlayers[0][1]) or
    (the_board[1]==the_board[4]==the_board[7]==orderedPlayers[0][1]) or 
    (the_board[2]==the_board[5]==the_board[8]==orderedPlayers[0][1]) or 
    (the_board[3]==the_board[6]==the_board[7]==orderedPlayers[0][1]) or 
    (the_board[1]==the_board[5]==the_board[7]==orderedPlayers[0][1]) or 
    (the_board[3]==the_board[5]==the_board[7]==orderedPlayers[0][1])): return orderedPlayers[0][0]
    elif ((the_board[1]==the_board[2]==the_board[3]==orderedPlayers[0][1])or
    (the_board[4]==the_board[5]==the_board[6]==orderedPlayers[1][1]) or
    (the_board[7]==the_board[8]==the_board[9]==orderedPlayers[1][1]) or
    (the_board[1]==the_board[4]==the_board[7]==orderedPlayers[1][1]) or 
    (the_board[2]==the_board[5]==the_board[8]==orderedPlayers[1][1]) or 
    (the_board[3]==the_board[6]==the_board[7]==orderedPlayers[1][1]) or 
    (the_board[1]==the_board[5]==the_board[7]==orderedPlayers[1][1]) or 
    (the_board[3]==the_board[5]==the_board[7]==orderedPlayers[1][1])): return orderedPlayers[1][0]
    elif not(' ' in the_board): return "It's a TIE"
    else: return False

def game_on(winner) :  
    if not winner: return True
    else: return False

def free_spot(index,board):
    if board[index] == ' ': return True
    else: return False

def move(actualPlayer): 
    loop = True
    while loop:
        choice = input(f"{actualPlayer[0]} What's your move? Choose a number (1-9)  ")
        if choice.isdigit(): 
            choice = int(choice)
            if choice in range(1,10):
                if free_spot(choice,the_board):
                    the_board[choice] = actualPlayer[1]
                    display_board(the_board)
                    loop = False
                else: print("It's taken. Try again!")
            else: print('Wrong number. Try again!')
        else: print("It's not a number. Try again!")

def game(orderedPlayers):
    counter = 1
    while game_on(winner(orderedPlayers)):
        if counter % 2 == 1: move(orderedPlayers[0])
        else: move(orderedPlayers[1])
        counter += 1
    print(f"The winner is: {winner(orderedPlayers)}")       

def tic_tac_toe():
    names = start_game()
    players = choose_marker(names)
    orderedPlayers = wich_player_begin(players)
    game(orderedPlayers)

tic_tac_toe()