import random


#def __init__(self):
        #self.cells = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display(board):
    print(" %s | %s | %s " %(board[1], board[2], board[3]))
    print("-----------")
    print(" %s | %s | %s " %(board[4], board[5], board[6]))
    print("-----------")
    print(" %s | %s | %s " %(board[7], board[8], board[9]))

def input_Player_Move():
    #Lets the player type whether to be "O" or "X"
    #Returns a list with the player's letter as the first item, and the computer's letter as second
    letter = ' '
    while not (letter == 'X' or letter == '0'):
        print('Do you want to be X or 0?')
        letter = input().upper()

    if letter == 'X':
        return ['X','0']
    else:
        return ['0','X']

def who_Goes_First():
    #Randomly selects the player to start
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
        
def play_Again():            
    print('Play Again? (yes or no)')
    return input().lower().startswith('y')

def make_Move(board, letter, move):
    board[move] = letter
        
def is_Winner(board, player):
    if board[1] == player and board[2] == player and board[3] == player:
        return True
    if board[4] == player and board[5] == player and board[6] == player:
        return True
    if board[7] == player and board[8] == player and board[9] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    if board[3] == player and board[6] == player and board[9] == player:
        return True
    if board[1] == player and board[5] == player and board[9] == player:
        return True
    if board[3] == player and board[5] == player and board[7] == player:
        return True
    return False

def board_Copy(board):
    dup_Board = []
    for i in board:
        dup_Board.append(i)

    return dup_Board
    
def is_Space_Free(board, move):
    return board[move] == ' '

def get_Player_Move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_Space_Free(board, int(move)):
        print("Please Choose your next move? (1-9) -> ")
        move = input()
    return int(move)
    
def choose_Random_Move(board, movesList):
    #Returns a valid move from the passed board
    #Returns none if there is no valid move
    possible_Moves = []
    for i in movesList:
        if is_Space_Free(board, i):
            possible_Moves.append(i)

    if len(possible_Moves) != 0:
        return random.choice(possible_Moves)
    else:
        return None
    
def get_Computer_Move(board, computer_Move):
    #takes input as board and computer's move, and determines where to move next and return that move
    if computer_Move == 'X':
        player_Move = '0'
    else:
        player_Move = 'X'

    #Check for computers win, first checks if computer can win in his next move
    for i in range(1,10):
        dup = board_Copy(board)
        if is_Space_Free(dup, i):
            make_Move(dup, computer_Move, i)
            if is_Winner(dup, computer_Move):
                return i

    #Check for playerss win, first checks if player can win in his next move
    for i in range(1,10):
        dup = board_Copy(board)
        if is_Space_Free(dup, i):
            make_Move(dup, player_Move, i)
            if is_Winner(dup, player_Move):
                return i

    #Play Corner
    move = choose_Random_Move(board, [1,3,7,9])
    if move != None:
        return move

    #Plat center
    if is_Space_Free(board, 5):
        return 5

    #Play sides
    return choose_Random_Move(board,[2,4,6,8])

def is_Board_Full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_Space_Free(board, i):
            return False
    return True
    
print('KURAMA- Designed by: Dashrath Chauhan @ GEC,DAHOD\n')
print('TIC-TAC-TOE')
while True:
    
    theBoard = [' '] * 10
    player_Move, computer_Move = input_Player_Move()
    turn = who_Goes_First()
    print('The '+turn+' will go first.')
    game_Is_Playing = True

    while game_Is_Playing:
        if turn == 'player':
            display(theBoard)
            move = get_Player_Move(theBoard)
            make_Move(theBoard, player_Move, move)

            if is_Winner(theBoard, player_Move):
                display(theBoard)
                print('Hooray! Yoh have won the game!')
                game_Is_Playing = False
            else:
                if is_Board_Full(theBoard):
                    display(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #Computer's turn
            move = get_Computer_Move(theBoard, computer_Move)
            make_Move(theBoard, computer_Move, move)

            if is_Winner(theBoard, computer_Move):
                display(theBoard)
                print('Computer wins! Yoh lose!')
                game_Is_Playing = False
            else:
                if is_Board_Full(theBoard):
                    display(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'player'
        
    if not play_Again():
        break
                



    
