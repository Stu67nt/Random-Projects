import chess
import chess.svg
import time

board = chess.Board()
move = ""
move_uci = ""


def checkmate(board):
    return board.is_checkmate()


while not checkmate(board):
    valid = False

    while not valid:
        try:
            print(board)
            print(board.legal_moves)
            move_from = input("Enter piece you want to move: ")
            print("If relevant at the end of move to input state what piece you want to promote to. (q,b,k,r)")
            move_to = input("Enter the square you want to move it to: ")
            move_uci = move_from + move_to
            valid = chess.Move.from_uci(move_uci) in board.legal_moves

            if not valid:
                print("Not a valid move!\n")
            else:
                move = chess.Move.from_uci(move_uci)
                board.push(move)
                print("")
        except:
            valid = False
            print("Not a valid move!\n")

print("Checkmate!")
time.sleep(3)