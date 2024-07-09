# This is mostly my own work with some elements of GPT for problems I needed help with which I couldn't find on
# the internet such as changing from a coordinate based movement system into algebraic chess notation and vice versa.

import chess  # EVERYTHING IS BUILT UPON USING THIS MODULE


# Function checks if checkmate is present on the board if so the game is ended.
def checkmate(board):
    return board.is_checkmate()


# This function will check to see if any sort of draw is present if so the game is called a draw and reason for draw.
def check_if_draw(board):
    if board.is_stalemate():
        print("Stalemate")
        return True
    if board.is_insufficient_material():
        print("Draw by Insufficient Material")
        return True
    if board.is_seventyfive_moves():
        print("Draw by No progress in 75 moves")
        return True
    if board.is_fivefold_repetition():
        print("Draw by 5 fold repetition")
        return True
    else:
        return False


# Checks if game should be ended
def end_game(mate, draw):
    if mate or draw:
        return True
    else:
        return False


# Converts regular move input into co-ordinate move notation and does the move.
def piece_movement(board):
    try:
        alg_move = input("Enter a move: ")  # Takes the move the user wants to input.

        if alg_move != 'draw' and alg_move != 'hint':
            class_coord_move = board.parse_san(alg_move)  # Converts it into coordinate movement. Currently, a class.
            # Line below converts it into a string to be used for validation and pushing to final board.
            str_coord_move = chess.square_name(class_coord_move.from_square) + chess.square_name(class_coord_move.to_square)
            valid = chess.Move.from_uci(str_coord_move) in board.legal_moves  # Validates move.
            if valid:
                move = chess.Move.from_uci(str_coord_move)
                board.push(move)
                print("")
            else:
                print("Not a valid move!\n")

        elif alg_move == 'draw':
            return alg_move

        elif alg_move == 'hint':
            return alg_move

    except (chess.InvalidMoveError, chess.IllegalMoveError):
        print("Not a valid move!\n")


# Local Multiplayer Game
def local_multiplayer_game():

    # Declaring local variables
    board = chess.Board()
    mate = False
    draw = False

    while not end_game(mate, draw):  # Checks if game is in checkmate or draw if not then turn continues.
        valid = False
        # 'valid' set to false inside the loop so whenever the loop runs initially and when rerunning the player's turn
        # is not continuously skipped due to a previously successful loop.

        while not valid:
            # Self-explanatory it just prints the current chess board.
            print(board)

            user_input = piece_movement(board)  # Function which handles piece movement and conversion

            if user_input == 'draw':
                draw = True
                print("Agreed Draw.")
                break
            elif user_input == 'hint':
                print(board.legal_moves)

            # Checks for draws / checkmate.
            if check_if_draw(board):
                draw = True
                break
            elif checkmate(board):
                print("Checkmate")
                mate = True
                break


    print(board)


local_multiplayer_game()
