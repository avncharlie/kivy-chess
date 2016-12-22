import chess
import chess.uci
import chess.svg
import sys

engine = chess.uci.popen_engine("stockfish")
board = chess.Board()

def print_board(board, flipped=True):
    print(board)
    f = open("chess.svg", "w+")
    f.write(chess.svg.board(board=board, flipped=flipped))

def engine_move(board):
    engine.isready() 
    engine.position(board)
    engine_move = engine.go(movetime=1000)[0]
    board.push(engine_move)
    return board

def player_move(board):
    player_move = input("Enter move: ")
    board.push_san(player_move)
    return board

def main():
    engine.uci()
    engine.ucinewgame()
    
    while True:
        engine_move(board)
        print_board(board)
        player_move(board)        
        print_board(board)

main()
