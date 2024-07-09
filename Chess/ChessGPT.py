# Everything here is written by ChatGPT. This acts as a comparison between my skills and it's.
# Any debugging will be done by prompts I input into it.
import chess

def print_board(board):
    print(board)

def main():
    board = chess.Board()

    print("Starting position:")
    print_board(board)

    while not board.is_game_over():
        move = None
        while move not in board.legal_moves:
            try:
                move_str = input(f"{'White' if board.turn == chess.WHITE else 'Black'} to move: ")
                move = chess.Move.from_uci(move_str)
            except Exception as e:
                print(f"Invalid move: {e}")
                continue
            if move not in board.legal_moves:
                print("Illegal move, please try again.")

        board.push(move)
        print_board(board)

    result = board.result()
    print(f"Game over: {result}")

if __name__ == "__main__":
    main()