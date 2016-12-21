import chess
import chess.uci
import chess.svg
import sys
import StringIO

engine = chess.uci.popen_engine("stockfish")
board = chess.Board()
out = StringIO.StringIO()

def print_board(board, flipped=True):
    print(board)
    f = open("chess.svg", "wr")
    f.write(chess.svg.board(board=board, flipped=flipped))

def engine_move(board):
    engine.isready() 
    engine.position(board)
    engine_move = engine.go(movetime=5000)[0]
    board.push(engine_move)
    return board

def player_move(board):
    player_move = raw_input("Enter move: ")
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
