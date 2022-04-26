#This assignment is to create a tic-tac-toe game in a 3x3 square
#Author: David Larsen

def main():
    print('Welcome to Tic-Tac-Toe!')
    player = next_player("")
    board = create_board()
    while not (winning(board) or draw(board)):
        display_board(board)
        next_move(player, board)
        player = next_player(player)
    display_board(board)
    print("That was fun! Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-|-|-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-|-|-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def winning(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def next_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    while board[square - 1] == 'x' or board[square - 1] == 'o':
        square = int(input(('Oops! That square is already taken. Please choose a square that has not already been chosen. ')))

    else:
        board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()