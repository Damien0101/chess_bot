import numpy as np
import os


def create_board():
    board = np.full((8, 8), '. ', dtype=object)

    black_pieces = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR']
    white_pieces = ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']

    board[0], board[7] = white_pieces, black_pieces
    board[1] = ['wP'] * 8
    board[6] = ['bP'] * 8
    
    return board


def display_board(board):
    print('         Chess Game\n')

    for i, row in enumerate(board,start=1):
        print(f'{i}   ' + ' '.join(row))
        print()
    print()
    print('    A  B  C  D  E  F  G  H')
    print()


def update_board(board, current_player):
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    
    while True:
        piece_to_move = input('which piece do you want to move? ').upper()
        move = input('where do you want to move this piece? ').upper()

        if len(piece_to_move) != 2 or len(move) != 2:
            print("invalid input, use format like A2.")
            continue

        from_col = dic.get(piece_to_move[0], -1)
        from_row = int(piece_to_move[1]) - 1 if piece_to_move[1].isdigit() else -1

        to_col = dic.get(move[0], -1)
        to_row = int(move[1]) - 1 if move[1].isdigit() else -1

        print(from_col, to_col)
        print(piece_to_move[0], move[0])

        if not (0 <= from_col < 8 and 0 <= from_row < 8 and 0 <= to_col < 8 and 0 <= to_row < 8):
            print("invalid move, out of range.")
            continue

        if board[from_row][from_col][0] != current_player:
            print("choose a valid piece for your side.")
            continue

        if not check_move(board, from_col, from_row, to_col, to_row, piece_to_move, move):
            print('invalid pawn move')
            continue


        board[to_row][to_col] = board[from_row][from_col]
        board[from_row][from_col] = '. '
        break

    return board


def check_move(board, from_col, from_row, to_col, to_row, piece_to_move, move):
    if board[from_row][from_col] == 'wP':
        if to_col == from_col:
            if to_row - from_row == 1 and board[to_row][to_col] == '. ':
                return True
            if from_row == 1 and to_row - from_row == 2 and board[from_row + 1][from_col] == '. ' and board[to_row][to_col] == '. ':
                return True

        if abs(to_col - from_col) == 1 and to_row - from_row == 1 and board[to_row][to_col][0] == 'b':
            return True

    if board[from_row][from_col] == 'bP':
        if to_col == from_col:
            if from_row - to_row == 1 and board[to_row][to_col] == '. ':
                return True
            if from_row == 6 and from_row - to_row == 2 and board[from_row - 1][from_col] == '. ' and board[to_row][to_col] == '. ':
                return True

        if abs(to_col - from_col) == 1 and from_row - to_row == 1 and board[to_row][to_col][0] == 'w':
            return True
    return False


def is_clear_path(board, from_row, from_col, to_row, to_col):
    pass


def main():
    board = create_board()
    current_player = 'w'

    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')

        display_board(board)
        print(f"{'Black' if current_player == 'b' else 'White'}'s turn")
        board = update_board(board, current_player)
        current_player = 'w' if current_player == 'b' else 'b' 


main()
