import chess


def start(board, move):
    try:
        if chess.Move.from_uci(move) not in board.legal_moves:
            print("This move is IMPOSSIBLE, try another one.")
        elif chess.Move.from_uci(move) in board.legal_moves:
            board = make_move(board, move)
    except chess.InvalidMoveError:
        print("Oops!  That was no valid number.  Try again...")
    return board


def make_move(board, move):
    board.push(chess.Move.from_uci(move))
    print(board)
    return board


if __name__ == "__main__":
    b = chess.Board()
    print(b)
    while not b.is_game_over():
        move = input("Move >>> ")
        b = start(b, move)
